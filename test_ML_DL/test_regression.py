from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf


# 加载 训练集 和 测试集
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 归一化
train_images = train_images/255.0
test_images = test_images/255.0

# 定义网络模型
model = tf.keras.models.Sequential([
    #  把 三维向量 转换为 二维向量
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # 定义一个 有128的 神经元的网络层 激活函数为 relu
    tf.keras.layers.Dense(128, activation='relu'),
    # dropout 率 为 0.2
    tf.keras.layers.Dropout(0.2),
    # 定义一个 有128的 神经元的网络层 激活函数为 relu
    tf.keras.layers.Dense(128, activation='relu'),
    # dropout 率 为 0.2
    tf.keras.layers.Dropout(0.2),
    # 定义一个 有128的 神经元的网络层 激活函数为 relu
    tf.keras.layers.Dense(128, activation='relu'),
    # dropout 率 为 0.2
    tf.keras.layers.Dropout(0.2),
    # 定义 10 个 输出 激活函数 为 softmax
    tf.keras.layers.Dense(10, activation='softmax')
])

# 定义 损失函数 学习率
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 训练网络
model.fit(train_images, train_labels, batch_size=1000, epochs=50)
# 在测试集上验证
model.evaluate(test_images,  test_labels, verbose=2)









# digit_test = train_images[4]
# print(train_images.ndim)
# digit_test1 = train_images[4, 14:, 14:]
# digit_test2 = train_images[4, :-14, :-14]
#
# plt.imshow(digit_test, cmap=plt.cm.binary)
# plt.show()
# plt.imshow(digit_test1, cmap=plt.cm.binary)
# plt.show()
# plt.imshow(digit_test2, cmap=plt.cm.binary)
# plt.show()
# l = [1, 2, 3, 4]
# print(l)
# l = np.array(l)
# print(l)

# # 等差数列
# b = np.linspace(1, 10, 10)
# # 等比数列
# b = np.logspace(1, 4, 4)
# print(b)
# a = np.arange(0, 10, 1).reshape(-1, 1) + np.arange(6)
# print(a)

# ll = np.array([[1, 3], [3, 4], [4, 5], [6, 7], [3, 4]])
# ll = np.array(list(set(tuple(t) for t in ll)))
# print(ll)

# print(ll)

# a = np.arange(1, 10).reshape(3, 3)
# b = np.arange(21, 30).reshape(3, 3)
# c = np.arange(51, 60).reshape(3, 3)
# print(np.stack((a, b), axis=0))
# print(np.stack((a, b), axis=2))
# print(np.stack((a, b, c)))

# x = np.array([12, 48, 45])
# print(x.ndim)

















