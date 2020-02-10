# -*- coding: utf-8 -*-
import xlrd

data_list = []  # 新建个空列表，来乘装所有的数据
wb = xlrd.open_workbook("/Users/xuanxu/Desktop/10.18日计.xlsx")  # 打开excel
sh = wb.sheet_by_name("Sheet0")  # 获取工作簿
header = sh.row_values(0)  # 获取标题行数据
for i in range(1, 2):  # 跳过标题行，从第二行开始取数据
    d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
    data_list.append(d)
print(data_list)


