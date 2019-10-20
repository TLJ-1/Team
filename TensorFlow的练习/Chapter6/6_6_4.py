import tensorflow as tf
global_step=tf.Variable(0,trainable=False)
initial_learning_rate=0.1

learning_rate=tf.train.exponential_decay(initial_learning_rate,global_step=global_step,decay_steps=10,decay_rate=0.9)   #定义递减的学习率
opt=tf.train.GradientDescentOptimizer(learning_rate)

add_global=global_step.assign_add(1)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(learning_rate))
    for i in range(21):
        g,rate=sess.run([add_global,learning_rate])
        #g对应 add_global,是迭代次数，rate是经过一次迭代后当次学习率
        print(g,rate)
