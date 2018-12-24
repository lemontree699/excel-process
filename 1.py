# -*- coding: utf-8 -*
'''
对PRI_Basic.xlsx文件，在City这一列的所有城市中，
如果判断出是长三角的26个城市之一，则在后面一列对应标1，不是则标0。
'''

import pandas

citys = ['上海市', '南京市', '无锡市', '常州市', '苏州市', '南通市', '盐城市', '扬州市', '镇江市', '泰州市', '杭州市', '宁波市','嘉兴市','湖州市','绍兴市','金华市','舟山市','台州市','合肥市','芜湖市','马鞍山市','铜陵市','安庆市','滁州市','池州市','宣城市']
f = pandas.read_excel(r'./data/PRI_Basic.xlsx')
column = f.City.tolist()
# print(len(f))
# print(column[5])

for i in range(2,len(column)):
	validate = column[i] in citys
	if(validate):
		f.iloc[i, 11] = 1
	else:
		f.iloc[i, 11] = 0

f.to_excel(r'./data/PRI_Basic_result.xlsx',sheet_name='sheet1')