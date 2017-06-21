# coding=utf-8

import pickle
mylist=["how","do","you","do"]
File1=file('Object.pkl','wb')
pickle.dump(mylist,File1,True) # 将对象存储到文件你们序列化
File1.close()
File2=file('Object.pkl','rb') # 恢复数据
mylist_bak=pickle.load(File2)
File2.close()
print mylist_bak

