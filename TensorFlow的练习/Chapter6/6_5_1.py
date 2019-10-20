#交叉熵试验
import tensorflow as tf
labels=[[0,0,1],[0,1,0]]
logits=[[2,0.5,6],[0.1,0,3]]

logits_scaled=tf.nn.softmax(logits)
logits_scaled2=tf.nn.softmax(logits_scaled)

result1=tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels,logits=logits)  #计算labels和logits的交叉熵
result2=tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels,logits=logits_scaled)  #计算labels和logits_scaled的交叉熵
result3=-tf.reduce_sum(labels*tf.log(logits_scaled),1)  #与tf.nn.softmax_cross_entropy_with_logits()结果一样

with tf.Session() as sess:
    print("scaled=",sess.run(logits_scaled))
    print("scaled2=",sess.run(logits_scaled2))
    #由line5、6可看出logits_scaled2是对logits softmax后再次softmax（）

    print("rel1=",sess.run(result1),"\n")
    print("rel2=",sess.run(result2),"\n")
    print("rel3=",sess.run(result3),"\n")

"""scaled= [[0.01791432 0.00399722 0.97808844]
 [0.04980332 0.04506391 0.90513283]]
scaled2= [[0.21747023 0.21446465 0.56806517]
 [0.2300214  0.22893383 0.5410447 ]]
rel1= [0.02215516 3.0996735 ] 

rel2= [0.56551915 1.4743223 ] 

rel3= [0.02215518 3.0996735 ] 
交叉熵：表达的是预测样本属于某一类的概率 tf.nn.softmax_cross_entropy_with_logits
"""