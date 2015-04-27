# coding = utf-8
__author__ = 'lee'
import mongo

client = mongo.Collection('192.168.2.54', 27017)
db = client['test']
collection = db['persion']


def testInsert(request):
    collection.insert_one({'name': 'Jasper', 'age': 21, 'sex': '男'})
    posts = [{'name': 'Jasper Lee', 'age': 21, 'sex': '男'},
             {'name': 'Jasper Json', 'age': 22, 'sex': '男'},
             {'name': 'Jasper Wston', 'age': 23, 'sex': '男'},
             {'name': 'Jasper Lily', 'age': 23, 'sex': '女'},
             {'name': 'Jasper Lucy', 'age': 24, 'sex': '女'},
             {'name': 'Jasper yy', 'age': 25, 'sex': '女'},
             {'name': 'Jasper ss', 'age': 25, 'sex': '男'},
             {'name': 'Jasper rtt', 'age': 23, 'sex': '男'},
             {'name': 'Jasper Lisa', 'age': 22, 'sex': '女'},
             {'name': 'Jasper Jack', 'age': 21, 'sex': '男'},
             {'name': 'Jasper Wston', 'age': 25, 'sex': '女'},
             {'name': 'Jasper baby', 'age': 26, 'sex': '男'},
             {'name': 'Jasper Angel', 'age': 21, 'sex': '女'}]
    collection.insert_many(posts)
    return


def testDelete(request):
    reslut = collection.delete_many({'name': 'Jasper'})
    reslut2 = collection.delete_one({'name': 'Jasper baby'})
    ret = reslut.delete_count
    ret2 = reslut2.delete_count
    return ret, ret2


def testfind(request):
    con = collection.find({}).batch_size(500)
    for c in con:
        print c


def testMapduce(request):
    map = "function(){emit(this.age,this.name);}"
    reduce = "function(key,values){ var ret={age:key,names:values}; return ret;}"
    final = "function(key,rval){if(key==0){rval.msg=\"a new life,baby!\";}return rval}"
    res = collection.map_reduce(map, reduce, "t_age_names", {'limit': 2, 'finalize': final})
    print res
    for k in db[res['result']].find():
        print k


def testUpdate(request):
    #数字用-----$inc 字符用-----$set
    res = collection.update_one({'name': 'Jasper ss'}, {'$set': {'name': 'Jasper Lee'}})
    print res.matched_count
    print res.modified_count
    res1 = collection.update_many({'name': 'Jasper'}, {'$set': {'name': 'Jasper Lee s'}})
    print res1.matched_count
    print res1.modified_count

def testRemove(request):
    res = collection.remove({'name': 'Jasper'})
    print res['ok']
    print res['n']

def testSave(request):
    post = {'name': 'xxxxxxxxx', 'age': 21, 'sex': '男'}
    collection.save(post)
