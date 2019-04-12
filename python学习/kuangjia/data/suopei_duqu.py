#! /usr/bin/python
# -*- coding: utf-8 -*-

import xlrd

class suopei_shujv(object):

    def duqu_shujv(self):
        shujv=[]
        f=xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\kuangjia\data\suopei.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1,num):
            shujv.append(sheet.row_values(i))
        return shujv

if __name__ == '__main__':
    a=suopei_shujv()
    print(a.duqu_shujv())