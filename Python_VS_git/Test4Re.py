# coding=utf-8

# 测试正则表达式,爬取网址的图片
import re
import requests # C:\Python27\Scripts\easy_install.exe requests 方式安装

# 源代码文件为Test4Re.txt
f=open('Test4Re.txt','r')
html=f.read()
f.close()
# 匹配图片网址
pic_url=re.findall('<img src="(.*?)" />',html,re.S)
i=0
for each in pic_url:
    print each
    if each.endswith('.jpg'):
        pic=requests.get(each)
        fp=open('TMP\\'+str(i)+'.jpg','wb') # 写入TMP文件夹，i.jpg
        fp.write(pic.content)
        fp.close()
        i+=1
    else:
        print 'give up'




