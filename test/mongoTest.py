# coding=utf-8
import pymongo

__author__ = 'lee'

import unittest

client = pymongo.MongoClient('localhost', 27017)
db = client['test']


class MyTestCase(unittest.TestCase):
    def test_mongo(self):
        # db.create_collection('persion')
        collection = db['persion']

        x = 1
        while x <= 100:
            collection.insert_one({'name': 'Jasper', 'age': 24 + x - 21, 'sex': '男'})
            collection.insert_one({'name': 'Lee', 'age': 100 - x + 2, 'sex': '女'})
            x += 1
        #
        # posts = [{'name': 'Jasper Lee', 'age': 21, 'sex': '男'},
        #          {'name': 'Jasper Json', 'age': 22, 'sex': '男'},
        #          {'name': 'Jasper Wston', 'age': 23, 'sex': '男'},
        #          {'name': 'Jasper Lily', 'age': 23, 'sex': '女'},
        #          {'name': 'Jasper Lucy', 'age': 24, 'sex': '女'},
        #          {'name': 'Jasper yy', 'age': 25, 'sex': '女'},
        #          {'name': 'Jasper ss', 'age': 25, 'sex': '男'},
        #          {'name': 'Jasper rtt', 'age': 23, 'sex': '男'},
        #          {'name': 'Jasper Lisa', 'age': 22, 'sex': '女'},
        #          {'name': 'Jasper Jack', 'age': 21, 'sex': '男'},
        #          {'name': 'Jasper Wston', 'age': 25, 'sex': '女'},
        #          {'name': 'Jasper baby', 'age': 26, 'sex': '男'},
        #          {'name': 'Jasper Angel', 'age': 21, 'sex': '女'}]
        # print collection.insert_many(posts)
        # con = collection.find({}).batch_size(500)
        # for c in con:
        #     print c
        # reslut = collection.delete_one({'name': 'Jasper baby'})
        # reslut = collection.delete_many({'name': 'Lee'})
        # print reslut.deleted_count
        # con = collection.find({}).batch_size(500)
        # for c in con:
        #     print c
        # map = "function(){emit(this.age,this.name);}"
        # reduce = "function(key,values){ var ret={age:key,names:values}; return ret;}"
        # final = "function(key,rval){if(key==0){rval.msg=\"a new life,baby!\";}return rval}"
        # res = collection.map_reduce(map, reduce, "t_age_names", {'limit': 2, 'finalize': final})
        # print res
        # for k in db[res['result']].find():
        #     print k


        # res = collection.update({'name': 'Jasper ss'}, {'name': 'Jasper Lee'})
        #
        # res1 = collection.update_many({'name': 'Jasper'}, {'$set': {'name': 'Jasper Lee s'}})
        # print res1.matched_count
        # print res1.modified_count
        # print "----------------------------------------------------------------------"
        # for c in collection.find().batch_size(500):
        #     print c
        # for c in collection.find().batch_size(500):
        #      print c
        # res = collection.remove({'name': 'Jasper'})
        # print "-----------------------------------"
        # print res['ok']
        # for c in collection.find().batch_size(500):
        #      print c
        post = {'name': 'xxxxxxxxx', 'age': 21, 'sex': '男'}
        collection.save(post)
        for c in collection.find().batch_size(500):
            print c

if __name__ == '__main__':
    unittest.main()
