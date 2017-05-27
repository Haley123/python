#!/usr/bin/env python

import requests
import json
import xlwt

items = []
pn = 1
def get_content(pn):
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
           'first': 'true',
            'pn': pn,
            'kd': 'python'
     }
    html = requests.post(url, data).text
    html = json.loads(html)
    for i in range(14):
        item = []
        item.append(html['content']['positionResult']['result'][i]['positionName'])
        item.append(html['content']['positionResult']['result'][i]['companyFullName'])
        item.append(html['content']['positionResult']['result'][i]['salary'])
        item.append(html['content']['positionResult']['result'][i]['city'])
        item.append(html['content']['positionResult']['result'][i]['positionAdvantage'])
        item.append(''.join(html['content']['positionResult']['result'][i]['companyLabelList']))
        item.append(html['content']['positionResult']['result'][i]['firstType'])
        items.append(item)
    return items

def excel_write(items):
    newTable = 'test.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1') 
    headData = ['招聘岗位', '公司', '薪资', '地区', '福利', '提供条件', '工作类型']
    for hd in range(7):
        ws.write(0, hd, headData[hd], xlwt.easyxf('font: bold on'))# 0 行   hd   列


    index=1
    for item in items:
            for i in range(7):
                ws.write(index, i, item[i])
            index +=1
    wb.save(newTable)
    print('创建成功')





if __name__ == '__main__':
    items = get_content(pn)
    excel_write(items)

