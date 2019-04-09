"""
    Parse Execel texts to Element-UI Cascader for Vue
"""
import xlrd

class CascadeCreater:
    """
        User CascadeCreater to create cascade in Element-UI for Vue with easy
    """
    def __init__(self):
        self.options = {}

    def add_child(self, area_p, province_p, name_p, layer):
        """
            Add a child to the dict tree
        """
        if layer == 0:
            self.options[area_p] = {}
            self.add_child(area_p, province_p, name_p, 1)
        elif layer == 1:
            self.options[area_p][province_p] = []
            self.add_child(area_p, province_p, name_p, 2)
        else:
            self.options[area_p][province_p].append(name_p)


    def output(self):
        with open('./cascader.txt', 'w') as file:
            tab = '  '
            file.write('options: [{\n')
            for area, list_1 in self.options.items():
                file.write(tab + 'value: \'' + area + '\',\n')
                file.write(tab + 'label: \'' + area + '\',\n')
                file.write(tab + 'children: [{\n')
                for province, list_2 in list_1.items():
                    file.write(tab*2 + 'value: \'' + province + '\',\n')
                    file.write(tab*2 + 'label: \'' + province + '\',\n')
                    file.write(tab*2 + 'children: [{\n')
                    for name in list_2:
                        file.write(tab*3 + 'value: \'' + name + '\',\n')
                        file.write(tab*3 + 'label: \'' + name + '\'\n')
                        if name != list_2[-1]:
                            file.write(tab*2 + '}, {\n')
                    file.write(tab*2 + '}]\n')
                    if province != list(list_1.keys())[-1]:
                        file.write(tab + '}, {\n')
                file.write(tab + '}]\n')
                if area != list(self.options.keys())[-1]:
                    file.write('}, {\n')
            file.write('}]\n')


if __name__ == '__main__':

    BOOK = xlrd.open_workbook('./data.xls')
    SHEET = BOOK.sheet_by_index(0)
    LENGTH = 271

    cascade = CascadeCreater()
    pre_area = ''
    pre_province = ''

    for row in range(1, LENGTH):
        area = SHEET.cell_value(rowx=row, colx=1)
        province = SHEET.cell_value(rowx=row, colx=2)
        name = SHEET.cell_value(rowx=row, colx=3) + ' ' + str(int(SHEET.cell_value(rowx=row, colx=0)))

        if pre_area == area:
            if pre_province == province:
                cascade.add_child(area, province, name, 2)
            else:
                cascade.add_child(area, province, name, 1)
        else:
            cascade.add_child(area, province, name, 0)
        pre_area = area
        pre_province = province

    cascade.output()
