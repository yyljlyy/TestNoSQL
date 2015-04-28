from django.shortcuts import render_to_response, render
from mongoengine import connect
import pymongo
import redis

__author__ = 'lee'
r = redis.StrictRedis('192.168.2.54', '6379', 0)


def index(request):
    return render_to_response('index.html')


def getback(request):
    k = request.POST['key']
    v = request.POST['value']
    r.set(k, v)
    return render(request, 'index.html', {'reslut': 'Key= ' + k + 'Value= ' + r.get(k)})


def setvalue(request):
    r.set('redis', 'myredis')
    r.set('redis2', 'myredis2')
    r.set('redis3', 'myredis3')
    r.set('redis4', 'myredis4')
    r.set('redis5', 'myredis5')
    return render(request, 'index.html', {
    'reslut': 'redis=' + r.get('redis') +'\n'+ 'redis2=' + r.get('redis2') +'\n'+ 'redis3=' + r.get('redis3') +'\n'+ 'redis4=' + r.get(
        'redis4') +'\n'+ 'redis5=' + r.get('redis5')})


def getvalue(request):
    print r.get('redis')
    print r.get('redis2')
    print r.get('redis3')
    print r.get('redis4')
    print r.get('redis5')
    return render(request, 'index.html', {
        'reslut': 'redis=' + r.get('redis') +'\n'+ 'redis2=' + r.get('redis2') +'\n'+ 'redis3=' + r.get(
            'redis3') +'\n'+ 'redis4=' + r.get(
            'redis4') +'\n'+'redis5=' + r.get('redis5')})


def delvalue(request):
    print r.delete('redis')
    print r.delete('redis2')
    print r.delete('redis3')
    print r.delete('redis4')
    print r.delete('redis5')
    print r.exists('redis')
    print r.exists('redis2')
    print r.exists('redis3')
    print r.exists('redis4')
    print r.exists('redis5')
    return render(request, 'index.html', {'reslut': 'sucess'})


def listvalue(request):
    print r.lpush('lists', 'li1')
    print r.lpush('lists', 'li2')
    print r.lpush('lists', 'li3')
    print r.lpush('lists', 'li4')
    print r.lpush('lists', 'li5')
    print r.llen('lists')
    print r.lrange('lists', 0, -1)
    print r.lset('lists', 1, 'w1')
    print r.lrange('lists', 0, -1)
    print r.lpop('lists')
    return render(request, 'index.html', {'reslut': r.lrange('lists', 0, -1)})


def mapvalue(request):
    r.hset('infos', 'man', 'Jasper')
    r.hset('infos', 'age', 11)
    print r.hget('infos', 'man')
    print r.hget('infos', 'age')
    r.hmset('info', {'name': 'Japser', 'age': 12, 'password': 'woaini'})
    print r.hmget('info', 'name', 'age', 'password')
    print r.hkeys('info')
    return render(request, 'index.html', {'reslut': r.hkeys('info') + r.hmget('info', 'name', 'age', 'password')})