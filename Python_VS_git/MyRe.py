# coding=utf-8

# 正则表达式
import  re

# 方法 findall search  sub，先抓大，再抓小
print '>>Test for findall'+'*'*80
ReCode="hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse"
print "ReCode = {0}".format(ReCode)
# 模式
# . 匹配任意字符，\n除外
a='xy123'
b=re.findall('x..',a) # xy1
# * 匹配前一个字符0次或n次

# ? 匹配前一个字符0次或1次

# .* 贪心算法，尽可能多
b=re.findall('xx.*xx',ReCode)
print b
# .*? 非贪心算法,尽可能少
b=re.findall('xx.*?xx',ReCode)
print b
# （） 括号内的数据作为结果返回
b=re.findall('xx(.*?)xx',ReCode)
print b
# re.S .可以匹配\n
ReCode2='''hadkfalifexxIxxfasdjifja134xxlovexx23345s
dfxxyouxx8dfse'''
b=re.findall('xx(.*?)xx',ReCode2,re.S)
print b

# search 找到一个就停止
print '\n>>Test for search'+'*'*80
s2='asdfxxIxx123xxlovexxdfd'
f=re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
print f

# 
print '\n>>Test for sub'+'*'*80
s3='123abcssfadfafa123'
output=re.sub('123(.*?)123','123%d123'%789,s3)
print output

# 匹配数字
print '\n>>(\d+)'+'*'*80
a='asdfasf123456789asdf780as'
b=re.findall('(\d+)',a)
print b