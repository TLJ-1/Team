"""import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("MNIST.data/",one_hot=True)
import pylab

tf.reset_default_graph()   #重置图
#定义占位符：输入变量的载体，函数的参数
x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])

#构建模型,正向结构
W=tf.Variable(tf.random_normal([784,10]))
b=tf.Variable(tf.random_normal([10]))   #为什么定义的W、b维度不同
    #定义输出节点
pred=tf.nn.softmax(tf.matmul(x,W)+b)

#定义反向结构
cost=tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred),reduction_indices=1))
    #定义学习率
learning_rate=0.01
    #梯度下降优化器
optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#训练模型并输出中间状态参数 ？中间状态参数为啥
training_epochs=25
batch_size=100
display_step=1

#开始训练前要初始化全体变量,启动session（）
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    #启动循环
    for epoch in range(training_epochs):
        avg_cost=0.
        total_batch=int(mnist.train.num_examples/batch_size) #计算训练集总共的批次

        for i in range(total_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)  #???
            c=sess.run([optimizer,cost],feed_dict=({x:batch_xs,y:batch_ys}))

            #计算平均loss值
            avg_cost += c/total_batch
        if(epoch+1) % display_step==0:
            print("Epoch:",'%04d' % (epoch+1),"cost","{:.9f}".format(avg_cost))

    print("Finished!") """
# -*- coding: utf-8 -*-

# TF之LiR：基于tensorflow实现手写数字图片识别准确率

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
print(mnist)

# 设置超参数
lr = 0.001  # 学习率
training_iters = 100  # 训练次数
batch_size = 128  # 每轮训练数据的大小，如果一次训练5000张图片，电脑会卡死，分批次训练会更好
display_step = 1

# tf Graph的输入
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# 设置权重和偏置
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 设定运行模式
pred = tf.nn.softmax(tf.matmul(x, w) + b)  #
# 设置cost function为cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(pred), reduction_indices=1))
# GD算法
optimizer = tf.train.GradientDescentOptimizer(lr).minimize(cost)

saver=tf.train.Saver()
model_path ="log/521model.ckpt"
# 初始化权重
init = tf.global_variables_initializer()
# 开始训练
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(training_iters):  # 输入所有训练数据
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples / batch_size)
        for i in range(total_batch):  # 遍历每个batch
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs, y: batch_ys})  # 把每个batch数据放进去训练
            avg_cost == c / total_batch
        if (epoch + 1) % display_step == 0:  # 显示每次迭代日志
            print("迭代次数Epoch:", "%04d" % (epoch + 1), "下降值cost=", "{:.9f}".format(avg_cost))
    print("Optimizer Finished!")

    # 测试模型
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.equal_mean(tf.cast(correct_prediction), tf.float32)
    print("Accuracy:", accuracy_eval({x: mnist.test.image[:3000], y: mnist}))

###保存模型
save.path=saver.save(sess,model_path)
print("Model saved in file: %s" % save_path)
