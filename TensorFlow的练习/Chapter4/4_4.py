#图相当于计算任务，reset/get_default_graph
import tensorflow as tf
import numpy as np
c=tf.constant(0.0)  #默认图里面建立的

g=tf.Graph() #建立新的图
with g.as_default():
    c1=tf.constant(2.0)
    print(c1.graph)  #新的图
    print(g)   #与c1一样的图
    print(c.graph)   #原始默认的图

g2=tf.get_default_graph()  #获得原始默认图
print(g2)

tf.reset_default_graph()  #重新见一张图，第三张图
g3=tf.get_default_graph()
print(g3)

#获取张量，通过名字得到相应的元素，get_tensor_by_name(name)
print(c1.name)
t=g.get_tensor_by_name(name="Const:0")
print (t)
"一般需要使用元素名字的时候，将其打印出来如：print（c1.name）"

#获取节点op的操作  get_operation_by_name
a=tf.constant([[1.0,2.0]])
b=tf.constant([[1.0],[3.0]])

tensor1=tf.matmul(a,b,name='exampleop')  #tf.matmul(a,b,name) 矩阵a b相乘
print(tensor1.name,tensor1)
test=g3.get_tensor_by_name("exampleop:0")
print(test)

print(tensor1.op.name)
testop=g3.get_operation_by_name("exampleop")
print(testop)

with tf.Session() as sess:
    test