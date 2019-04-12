#! /usr/bin/python
# -*- coding: utf-8 -*-

import xlrd

class mingcheng(object):

    def shujv(self):
        shujv=[]
        f = xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\kuangjia\data\xuexiao.xls')
        sheet = f.sheets()[0]
        hang = sheet.nrows
        for i in range(1,hang):
            shujv.append(sheet.row_values(i))
        return shujv

if __name__ == '__main__':
    a = mingcheng()
    print(a.shujv())