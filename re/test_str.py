# coding:utf-8

import re
# string = "index"
# print string.index('nde')


rule1 = re.compile('^(?=.\*\d)(?=.\*[a-z])(?=.\*[A-Z]).{8,10}$')
rule2 = re.compile('^\d{4}-\d{1,2}-\d{1,2}')



print rule1.findall('3B2%4A#cb')

print rule2.findall('2018-11-3')