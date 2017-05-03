# -*- coding:utf-8 -*-
import urllib,re
import xlwt
#获取所有源码
def getdata():
    url_list=[]
    for i in range(1,40):
        url='http://furhr.com/?page={}'.format(i)
        try:
            html=urllib.urlopen(url).read()
            #print html
        except Exception as e:
            print e
            continue
            #正则表达式
        page_list=re.findall(r'<tr><td>\d+</td><td>\d+</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',html)
       # print page_list[0][0]
        url_list.append(page_list)
    return url_list

#创建EXCL
def excel_write():
    newTable='test123.xls'#表格名称
    wb=xlwt.Workbook(encoding='utf-8')#创建文件。设置编码
    ws=wb.add_sheet('test1')#创建表
    headData=['公司名称','电话','地址']
    for colnum in range(0,3):
        ws.write(0,colnum,headData[colnum],xlwt.easyxf('font:bold on'))#行，列
    #wb.save(newTable)#保存
    #print'创建成功'

    #写入数据
    index=1
    for item in items:#银行信息
        for j in range(0,len(item)):
            for i in range(0,3):
                print item[j][i]
                ws.write(index,i,item[j][i])
            index +=1
        wb.save(newTable)

items=getdata()
excel_write()


