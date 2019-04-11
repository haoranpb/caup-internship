"""
    A STL Parser
    1. 保留小数点后两位
    2. 输出 X，Y，Z 的最大、最小值
    3. 可能单位推测
    4. 三角形面积计算
"""
import math

def line_length(point1, point2, point3):
    a = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
    b = math.sqrt((point3[0] - point2[0])**2 + (point3[1] - point2[1])**2 + (point3[2] - point2[2])**2)
    c = math.sqrt((point1[0] - point3[0])**2 + (point1[1] - point3[1])**2 + (point1[2] - point3[2])**2)
    return [a, b, c]

def striangle(lines):
    s = (lines[0] + lines[1] + lines[2])/2
    return math.sqrt(s * (s-lines[0]) * (s - lines[1]) * (s - lines[2]))

if __name__ == "__main__":
    MAX = [0, -9999, -9999, -9999]
    MIN = [0, 9999, 9999, 9999]
    with open('../data/output.stl', 'w') as out_file:
        with open('../data/01_Mid.stl', 'r') as in_file:
            for line in in_file:
                if 'vertex' in line:
                    numbers = line.strip().split()
                    for i in range(1, 4):
                        numbers[i] = str(round(float(numbers[i]), 2))
                        MAX[i] = max(MAX[i], float(numbers[i]))
                        MIN[i] = min(MIN[i], float(numbers[i]))
                    out_file.write('    ' + ' '.join(numbers) + '\n')
                elif 'facet normal' in line:
                    numbers = line.strip().split()
                    for i in range(2, 5):
                        numbers[i] = str(round(float(numbers[i]), 2))
                    out_file.write(' '.join(numbers) + '\n')
                else:
                    out_file.write(line)
    print(MAX)
    print(MIN)
