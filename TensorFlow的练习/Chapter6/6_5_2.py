#one_hot试验   总和是1，但是取值不是0|1
import tensorflow as tf

labels=[[0.4,0.3,0.3],[0.3,0.6,0.1]]
logits=[[2,0.5,6],[0.1,0,3]]
result4=tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels,logits=logits)

with tf.Session() as sess:
    print("rel4=",sess.run(result4),"\n")

    """"""