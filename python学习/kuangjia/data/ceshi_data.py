#! /usr/bin/python
# -*- coding: utf-8 -*-

import xlrd

class peijianhao(object):

    def peijian(self):
        shujv = []
        f = xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\kuangjia\data\ceshi.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1, num):
            shujv.append(sheet.row_values(i))
        return shujv

class peijianmingxi(object):

    def peijian(self):
        shujv = []
        f = xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\kuangjia\data\ceshi.xls')
        sheet = f.sheets()[1]
        num = sheet.nrows
        for i in range(1, num):
            shujv.append(sheet.row_values(i))
        return shujv

class dingdan(object):

    def dingdan(self):
        shujv = []
        f = xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\kuangjia\data\ceshi.xls')
        sheet = f.sheets()[2]
        num = sheet.nrows
        for i in range(1, num):
            shujv.append(sheet.row_values(i))
        return shujv

class liebiao(object):

    def liebiao(self):
        shujv = []
        f = xlrd.open_workbook(r'C:\Users\zk\Desktop\python学习\kuangjia\data\ceshi.xls')
        sheet = f.sheets()[3]
        num = sheet.nrows
        for i in range(1, num):
            shujv.append(sheet.row_values(i))
        return shujv