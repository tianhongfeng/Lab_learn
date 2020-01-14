import keras
from keras.datasets import mnist


# 获取手写数字 图片和标签
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


