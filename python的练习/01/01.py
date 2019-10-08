#生成200个激活码（优惠卷）

#coding=utf-8
import random
import string

number=200
length=12  #激活码的长度

def make():
    activation_code = string.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',length)).replace(" ","")
    return activation_code
"""string.join（）:
    random.sample()：随机生成激活码，random.sample(range(),length)
    replace()
"""

#创建字典
a={1:make()}

#判断激活码是否重复
def judge():   #
    new_made=made()
    for k in a:
        if a[k]!=new_made:
            return new_made
        else:
            judge()

for i in range(1,number):
    a[i]=judge()

for j in a:
    print('%4d' %(j),'   '  ,a[j] )
