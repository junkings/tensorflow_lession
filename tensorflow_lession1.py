# encoding: utf8
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def showImage(_image, _labels):
	# _iamge 图像源文件 是 mnist.train.images[100]
	# _labels 类别标签 是 mnist.train.labels[100]
	test_image = _image.reshape((28, 28))
	print(_labels)
	plt.imshow(test_image, cmap='gray')
	plt.show()


def sample_test():
	# 加载数据 mnist 手写体识别图像资料
	mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

	#
	x = tf.placeholder("float", [None, 784])
	W = tf.Variable(tf.zeros([784, 10]))
	b = tf.Variable(tf.zeros([10]))

	y = tf.nn.softmax(tf.matmul(x, W) + b)
	y_ = tf.placeholder("float", [None, 10])
	cross_entropy = -tf.reduce_sum(y_*tf.log(y))

	train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

	init = tf.initialize_all_variables()

	sess = tf.Session()
	sess.run(init)

	for i in range(1000):
		batch_xs, batch_ys = mnist.train.next_batch(100)
		sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})

	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
	print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

if __name__ == "__main__":
	sample_test()
