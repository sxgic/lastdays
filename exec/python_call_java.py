#!/usr/bin/python
# -*- coding: utf-8 -*-

import jpype
import os
print(os.path.abspath('.'))
jarpath = os.path.join(os.path.abspath('.'), 'test.jar') #test.jar的路径 不确定的话，打印下。 踩过坑 在test.jar前面多加了\\导致报错 不需要加\\,会自动拼接的
print(jarpath)
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jarpath)
Test = jpype.JClass('com.Test')
# 或者通过JPackage引用Test类
# com = jpype.JPackage('com')
# Test = com.Test
t = Test()
res = t.run("hello world")
print (res)
jpype.shutdownJVM()
