# This Python file uses the following encoding: utf-8
# coding=utf-8

from django.shortcuts import render

__author__ = 'lee'
import memcache

mc = memcache.Client(['localhost:11211'], debug=1)


def mtestSet(request):
    mc.set('name', 'Jasper')
    mc.set('age', 11)
    mc.set('sex', '男')
    return render(request, 'index.html', {'reslut': 'name:' + mc.get('name') + '\n' + 'sex:' + mc.get('sex')})


def mtestGet(request):
    return render(request, 'index.html',
                  {'reslut': 'name: ' + mc.get('name') + '\n' + 'age: ' + str(mc.get('age')) + '\n' + 'sex: ' + mc.get('sex')})


def mtestAdd(request):
    mc.add('password', 'woaini', 0)
    return render(request, 'index.html', {'reslut': 'password: ' + mc.get('password')})


def mtestAppend(request):
    mc.append('name', 'Lee')
    return render(request, 'index.html', {'reslut': 'name: ' + mc.get('name')})


def mtestDelete(request):
    delete = mc.delete('password')
    if delete == 1:
        x = '成功删除'
    return render(request, 'index.html', {'reslut': x})


def mtestGetMulti(request):
    return render(request, 'index.html', {'reslut': mc.get_multi(['name', 'age', 'password', 'sex'])})


def mtestIncr(request):
    mc.set('num', 1)
    nnum = mc.incr('num', 2)
    return render(request, 'index.html', {'reslut': '原始值: ' + str(mc.get('num')) + 'Incr 2: ' + str(nnum)})


def mtestDecr(request):
    mc.set('num', 5)
    nnum = mc.decr('num', 2)
    return render(request, 'index.html', {'reslut': '原始值: ' + str(mc.get('num')) + 'Decr 2: ' + str(nnum)})


def mtestReplace(request):
    age = mc.get('age')
    mc.replace('age', 12)
    return render(request, 'index.html', {'reslut': '修改前age: ' + str(age) + '修改后age: ' + str(mc.get('age'))})


def mtestStats(request):
    ms = mc.get_stats()
    return render(request, 'index.html', {'reslut': ms})

    # def mtest(request):
    # return render(request, 'index.html', {'reslut': 'name' + mc.get('name')})