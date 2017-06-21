# coding=utf-8

from Const import Separate

class Base:
    def __init__(self,para): # 构造
        self._name=para
    def sayself(self): # function
        print(">>In function sayself\nclass name = {0}".format(self._name))
    def doit(self):
        print(r">>In function doit\n")
        for i in range(0,3): # for
            print("class data [{0}] = {1}".format(i,i*i)) # format

class Derivate(Base):
    def sayself(self):
        print(">>In function sayself-derived class\nclass name = {0}".format(self._name))

def ClassFun():
    Separate()
    h_base = Base("base class")
    h_base.sayself();
    h_base.doit()
    h_derivate = Derivate("derivate class");
    h_derivate.sayself()



