# coding=utf-8
__author__ = 'lee'
import memcache
import unittest

mc = memcache.Client(['localhost:11211'], debug=0)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(mc.set('name', 'Jasper'), True)
        # self.assertEqual(mc.set('age', 11), True)
        # self.assertEqual(mc.set('sex', '男'), True)
        # mc.append('name', '_woaini')
        # print mc.get_multi(['name', 'age', 'password', 'sex'])
        # de = mc.delete('password')
        # print de
        # print de.real
        # print mc.get('name')
        # print mc.get('sex')
        # ms = mc.set('num', 1)
        # print ms
        # md = mc.incr('num', 2)
        # print md
        # mc.decr('num', 1)
        # print mc.get('num')
        ms = mc.get_stats()
        print ms

if __name__ == '__main__':
    unittest.main()
