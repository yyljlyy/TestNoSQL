# This Python file uses the following encoding: utf-8
import string
from django.shortcuts import render
import pymongo

__author__ = 'lee'

client = pymongo.MongoClient('localhost', 27017)
db = client['test']
collection = db['persion']


def testInsert(request):
    c1 = collection.count
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
    c2 = collection.count
    print c1
    return render(request, 'index.html', {'reslut': "添加之前数量: " + str(c1) + '\n' + "添加之后数量: " + str(c2)})


def testDelete(request):
    reslut = collection.delete_many({'name': 'Jasper'})
    reslut2 = collection.delete_one({'name': 'Jasper baby'})
    ret = reslut.deleted_count
    ret2 = reslut2.deleted_count
    return render(request, 'index.html', {'reslut': '删除多个数量: ' + str(ret) + '删除一个数量: ' + str(ret2)})


def testfind(request):
    con = collection.find({}).batch_size(500)
    x = []
    for c in con:
        x.append(c)
    return render(request, 'index.html', {'reslut': x})


def testMapduce(request):
    map = "function(){emit(this.age,this.name);}"
    reduce = "function(key,values){ var ret={age:key,names:values}; return ret;}"
    final = "function(key,rval){if(key==0){rval.msg=\"a new life,baby!\";}return rval}"
    res = collection.map_reduce(map, reduce, "t_age_names", {'limit': 2, 'finalize': final})
    x = []
    for k in db[res['result']].find():
        print x.append(k)
    return render(request, 'index.html', {'reslut': x})


def testUpdate(request):
    # 数字用-----$inc 字符用-----$set
    res = collection.update_one({'name': 'Jasper ss'}, {'$set': {'name': 'Jasper Lee'}})
    r1 = res.matched_count
    r2 = res.modified_count
    res1 = collection.update_many({'name': 'Jasper'}, {'$set': {'name': 'Jasper Lee s'}})
    r3 = res1.matched_count
    r4 = res1.modified_count
    return render(request, 'index.html',
                  {'reslut': '单条修改 matched: ' + str(r1) + 'modified: ' + str(r2) + '多条修改 matched: ' + str(r3) + 'modified: ' + str(r4)})


def testRemove(request):
    res = collection.remove({'name': 'Jasper'})
    x = ''
    if res['ok'] == 1:
        x = '是的'
    num = res['n']
    return render(request, 'index.html', {'reslut': '是否删除：' + x + '\n' + '删除数量：' + str(num)})


def testSave(request):
    post = {'name': 'xxxxxxxxx', 'age': 21, 'sex': '男'}
    csave = collection.save(post)
    if csave != 0:
        x = '是的'
    return render(request, 'index.html', {'reslut': '是否删除 ：' + x})