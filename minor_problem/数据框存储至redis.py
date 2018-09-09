# -*- coding=utf-8 -*-
from pandas import Series, DataFrame
import pandas as pd
import redis

# 造数据
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

# 获取redis连接
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# r.set("frame", frame)
# a = r.get("frame")

# 存储
r.set("frame", frame.to_msgpack(compress='zlib'))
# 读取
a = pd.read_msgpack(r.get("frame"))
print(a)
