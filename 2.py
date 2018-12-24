# -*- coding: utf-8 -*
'''
对“民营上市 A股 剔除ST 研发 13前上市 多期DID 未在自贸区.xlsx”文件，
其Pridt列为形如xxxx-xx-xx的日期，
现需要新建一列Life，只保留Pridt的年份，不要后面的月和日的信息。
'''

import pandas

f = pandas.read_excel(r'./data/民营上市 A股 剔除ST 研发 13前上市 多期DID 未在自贸区.xlsx')
pridt = f.Pridt.tolist()

for i in range(len(pridt)):
	f.iloc[i, 17] = str(pridt[i])[:4]

f.to_excel(r'./data/民营上市 A股 剔除ST 研发 13前上市 多期DID 未在自贸区_result.xlsx',sheet_name='sheet1')