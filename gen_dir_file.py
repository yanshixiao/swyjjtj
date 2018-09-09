# -*- encoding:utf8 -*-
# 生成10w文件，文件内容随机数

import os
import random
import multiprocessing
import time

base_path = "E:/testdir/rantxt/"

# 删除文件夹下文件
for root, dirs, files in os.walk(base_path, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    # for name in dirs:
    #     os.rmdir(os.path.join(root, name))


folder = os.path.exists(base_path)
if not folder:
    os.makedirs(base_path)
else:
    print("已存在")

os.chdir(base_path)


def mktxt(file_num):
    for i in range(file_num):
        file_name = str(i+1) + ".txt"
        with open(file_name, 'w') as file:
            file.write(str(random.random()))


if __name__ == "__main__":
    start = time.time()
    p = multiprocessing.Process(target=mktxt, args=(100000,))
    p.start()
    end = time.time()
    print(end-start)
