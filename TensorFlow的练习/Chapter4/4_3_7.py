"""import tensorflow as tf

#演示作用域与操作符的受限范围

with tf.variable_scope("scope1") as sp:
    var1=tf.get_variable("v",[1])

print("sp:",sp.name)
print("var1",var1.name)"""
#图相当于计算任务，reset/get_default_graph
import tensorflow as tf
import numpy as np
c=tf.constant(0.0)  #默认图里面建立的

g=tf.Graph() #建立新的图
with g.as_default():
    c1=tf.constant(0.0)
    print(c1.graph)  #新的图
    print(g)   #与c1一样的图
    print(c.graph)   #原始默认的图

g2=tf.get_default_graph()  #获得原始默认图
print(g2)

tf.reset_default_graph()  #重新见一张图，第三张图
g3=tf.get_default_graph()
print(g3)
