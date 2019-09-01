import tensorflow as tf
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a=np.random.random((2,16))
print(a)


# # img = tf.constant([
# #     [[0.0, 4.0], [0.0, 4.0], [0.0, 4.0], [0.0, 4.0]],
# #     [[1.0, 5.0], [1.0, 5.0], [1.0, 5.0], [1.0, 5.0]],
# #     [[2.0, 6.0], [2.0, 6.0], [2.0, 6.0], [2.0, 6.0]],
# #     [[3.0, 7.0], [3.0, 7.0], [3.0, 7.0], [3.0, 7.0]]
# # ])
# # img = tf.reshape(img, [1, 4, 4, 2])
# img=tf.constant([[-1.0,-1.0,-1.0],  [0,0,0],  [1.0,1.0,1.0],
#                                     [-2.0,-2.0,-2.0], [0,0,0],  [2.0,2.0,2.0],
#                                     [-1.0,-1.0,-1.0], [0,0,0],  [1.0,1.0,1.0]],)
#
# img = tf.reshape(img,shape = [3, 3, 3, 1])
#
#
# with tf.Session() as sess:
#     print("image:")
#     image = sess.run(img)
#     print(image)
