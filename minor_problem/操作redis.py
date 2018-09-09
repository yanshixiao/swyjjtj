# -*- coding=utf-8 -*-
# 操作Redis

import redis


# 增
def redis_add(r, key, value):
    if key != "":
        r.set(str(key), value)


# 删
def redis_del(r, key):
    if key != "":
        r.delete(str(key))


# 改
def redis_mo(r, key, value):
    if key != "":
        r.set(str(key), value)


# 查
def redis_find(r, key):
    if key != "":
        print(r.get(str(key)))


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)

    #     redis_add(r, 'a', 'test')
    #     redis_find(r, 'a')
    #     redis_mo(r, 'a', 'test_test')
    #     redis_del(r, 'a')