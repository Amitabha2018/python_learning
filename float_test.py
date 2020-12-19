#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2020-12-19 15:26'

#float 浮点数的特点，导致它在计算机内运算时，结果不是那么精确，会有四舍五入的差。

print(0.35+0.11)

'''
if 嵌套,if 和 else 里，各自再嵌套if else
'''

'''
1、如果身体体能指数 energy 大于等于 80，就是容易改造，在此前提下：

a) 如果身体体能指数大于等于 90，1小时改造完毕。

b) 如果身体体能指数大于等于 80，1天改造完毕。

2、如果身体体能指数小于 80，就是不易改造，在此前提下：

a) 如果身体体能指数小于 60， 改造不了。

b) 如果身体体能指数大于等于 60 小于 80，希望渺茫。
(注意，缩进时，Tab和空格不要混用哦！一定注意)

'''


energy=65

if energy>=80:
    print('容易改造')

    if energy>=90:
        print('1小时改造完毕')
    #当代码执行到这一行的时候 说明energy已经在80到90之间了
    #所以我们就不需要再使用elif 来判断了
    else:
        print('1天改造完毕')

else:
    print('不易改造')

    if energy<60:
        print('改造不了')
   #当代码执行到这一行的时候 说明energy已经在60到80之间了
    #所以我们就不需要再使用elif 来判断了
    else:
        print('希望渺茫')

print('结束')