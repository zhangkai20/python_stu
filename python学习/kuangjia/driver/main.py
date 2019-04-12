#! /usr/bin/python
# -*- coding: utf-8 -*-

from kuangjia.report.baogao import baogao

def run(aa):
    baogao(aa)

with open('回归.txt','r') as f:
    a = f.readlines()
    if len(a) == 1:
        run('*')
    else:
        run(a)