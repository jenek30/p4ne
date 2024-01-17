from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x):
    return x.value

list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['C'][1:]))
list_y1 = list(map(getvalue, sheet['D'][1:]))

pyplot.title('Мой график')
pyplot.xlabel('Годы')
pyplot.ylabel('Относительная температура/Активность солнца')
pyplot.plot(list_x, list_y)
pyplot.plot(list_x, list_y1)

pyplot.show()