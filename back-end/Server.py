"""
    Micro Server For CAUP Front End
"""
import os, math, json
from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    stl_file = request.files['file']
    stl_file.save(os.path.join('./', 'temp.stl'))
    with open(os.path.join('./', 'parsed.stl'), 'w') as out_file:
        with open(os.path.join('./', 'temp.stl'), 'r') as in_file:
            for line in in_file:
                if 'vertex' in line:
                    numbers = line.strip().split()
                    for i in range(1, 4):
                        numbers[i] = str(round(float(numbers[i]), 2))
                    out_file.write('    ' + ' '.join(numbers) + '\n')
                elif 'facet normal' in line:
                    numbers = line.strip().split()
                    for i in range(2, 5):
                        numbers[i] = str(round(float(numbers[i]), 2))
                    out_file.write(' '.join(numbers) + '\n')
                else:
                    out_file.write(line)
    return send_from_directory('./', 'parsed.stl')

@app.route('/min-max', methods=['GET'])
def min_max():
    MAX = [0, -9999, -9999, -9999]
    MIN = [0, 9999, 9999, 9999]
    with open(os.path.join('./', 'parsed.stl'), 'r') as file:
        for line in file:
            if 'vertex' in line:
                numbers = line.strip().split()
                for i in range(1, 4):
                    MAX[i] = max(MAX[i], float(numbers[i]))
                    MIN[i] = min(MIN[i], float(numbers[i]))
    json_body = {}
    json_body['x-max'] = MAX[1]
    json_body['y-max'] = MAX[2]
    json_body['z-max'] = MAX[3]
    json_body['x-min'] = MIN[1]
    json_body['y-min'] = MIN[2]
    json_body['z-min'] = MIN[3]
    return json.dumps(json_body)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
