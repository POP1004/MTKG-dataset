import pickle

# 加载pkl文件
with open('sorted_icews_images.pkl', 'rb') as file:
    data = pickle.load(file)

# 输出数据内容
print(data)
