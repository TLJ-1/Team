import tensorflow as tf

"""var1=tf.Variable(1.0,name='firstvar')
print("var1:",var1.name)

get_var1=tf.get_variable("firstvar",[1],intializer=tf.constant_initializer(0.4))
print("get_var1=",get_var1.name)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("var1=",var1.eval())
    print("get_var1",get_var1.eval())
#var1=tf.Variable(2.2,name='firstvar')"""

with tf.variable_scope("text1",):  #作用域text1
	var1=tf.get_variable("firstvar",shape=[2],dtype=tf.float32)

with tf.variable_scope("text2"):
	    var2=tf.get_variable("firstvar",shape=[2],dtype=tf.float32)

print("var1:",var1.name)
print("var2:",var2.name)


