#! /usr/bin/python
# -*- coding: utf-8 -*-

import xlrd

class moer_data(object):

    def shujv(self):
        shujv = []
        f = xlrd.open_workbook('')
        sheet = f.sheets()[0]
        row = sheet.nrows
        for i in range(row):
          shujv.append(sheet.row_values(i))
        return shujv

