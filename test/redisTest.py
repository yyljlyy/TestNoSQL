import redis

__author__ = 'lee'

import unittest

r = redis.StrictRedis(host='localhost', port='6379', db=0)


class MyTestCase(unittest.TestCase):

    def test_RedisSet(self):
        # r.set('man', 'Jasper')
        # print r.lpush('lists', 'l1')
        # print r.lpush('lists', 'l2')
        # print r.lpush('lists', 'l3')
        # print r.llen('lists')
        # print r.lrange('lists', 0, -1)
        # print r.lset('lists', 1, 'w1')
        # print r.lrange('lists', 0, -1)
        # print r.lpop('lists')


        r.hset(
            'infos', 'man', 'Jasper')
        r.hset('infos', 'age', 11)
        print r.hget('infos', 'man')
        print r.hget('infos', 'age')
        r.hmset('info', {'name': 'Japser', 'age': 12, 'password': 'woaini'})
        print r.hmget('info', 'name', 'age', 'password')
        print r.hkeys('info')
        self.assertEqual('Jasper', r.get('man'))


if __name__ == '__main__':
    unittest.main()
