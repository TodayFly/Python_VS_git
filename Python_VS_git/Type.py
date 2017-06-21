# coding=utf-8

#
# python 数据类型和符号
#
from Const import Separate

# 列表
List1 = ['a','b','c'] * 2

# 元组
Tuple1 = ('a','b','c')

# 集合
Set1 = set("abcdefg")
Set2 = set("efghijk")
Setx = Set1 & Set2 # 交集
Sety = Set1 | Set2 # 并集
SetZ = Set1 - Set2 # 差集

# 字典
Dict1 = {'name':'Yin','home':'wuhan'}

# Funtcion
def TypeFun():
    '''文档字符串,可以用print TypeFun.__doc__ 或 help(TypeFun) 来输出该文档字符串
    :return:
    '''
    Separate()
    print(">>In Type.py")
    print "*List1 = {0}".format(List1)
    print "*Set 1 and 2 {0}、{1}".format(Set1,Set2)
    print "交集{0} 并集{1} 差集{2}".format(Setx,Sety,SetZ)
    print "*Dict1 = {0}".format(Dict1)