# -*- coding: utf-8 -*

'''
对“政府补助 合计数.xlsx”文件，
观察Stkcd和Accper两列，如果两列均匹配，
则合并其列Fn05602和列Fn05603中的数据(将金额相加)，
最后生成一个新表。
注意有些项的值为'nan'，即为空值，
需要先检测出来之后置为0。
'''

import pandas
import math

df = pandas.read_excel(r'./data/政府补助 合计数.xlsx')

# 将空值置为0
for i in range(1, len(df['Fn05602'])):
	if math.isnan(df['Fn05602'][i]):
		df['Fn05602'][i] = 0
for i in range(1, len(df['Fn05603'])):
	if math.isnan(df['Fn05603'][i]):
		df['Fn05603'][i] = 0

# 每一列为一个list，是为了之后使用传入等长列表组成的字典来创建DataFrame
stckd = []
accper = []
datasources = []
typrep = []
fn05601 = []
fn05602 = []
fn05603 = []
data = {'Stkcd':stckd, 'Accper':accper, 'DataSources':datasources, 'Typrep':typrep, 'Fn05601':fn05601, 'Fn05602':fn05602, 'Fn05603':fn05603}

# 使用groupby函数，得到的grouped可以通过迭代的方式访问
grouped = df.groupby(['Stkcd', 'Accper'])
for (k1,k2), group in grouped:
	# print(k1,k2)
	# print(group)
	if len(group) == 1:
		stckd.append(k1)
		accper.append(k2)
		datasources.append(group.iloc[0][2])
		typrep.append(group.iloc[0][3])
		fn05601.append(group.iloc[0][4])
		fn05602.append(group.iloc[0][5])
		fn05603.append(group.iloc[0][6])
	else:
		stckd.append(k1)
		accper.append(k2)
		datasources.append(group.iloc[0][2])
		typrep.append(group.iloc[0][3])
		fn05601.append(group.iloc[0][4])
		length = len(group)
		s1 = 0
		for i in range(length):
			s1 += group.iloc[i][5]
		fn05602.append(s1)
		s2 = 0
		for i in range(length):
			s2 += group.iloc[i][6]
		fn05603.append(s2)

# 创建新的DataFrame，然后将其写入excel
new_df = pandas.DataFrame(data)
new_df.to_excel(r'./data/政府补助 合计数_result.xlsx',sheet_name='sheet1')