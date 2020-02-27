- [python 面试常见问题总结](#python-%e9%9d%a2%e8%af%95%e5%b8%b8%e8%a7%81%e9%97%ae%e9%a2%98%e6%80%bb%e7%bb%93)
  - [python函数——形参中的：*args和**kwargs](#python%e5%87%bd%e6%95%b0%e5%bd%a2%e5%8f%82%e4%b8%ad%e7%9a%84args%e5%92%8ckwargs)
  - [Python是如何进行内存管理的？](#python%e6%98%af%e5%a6%82%e4%bd%95%e8%bf%9b%e8%a1%8c%e5%86%85%e5%ad%98%e7%ae%a1%e7%90%86%e7%9a%84)
  - [python  _init__和 _new__的区别](#python-init%e5%92%8c-new%e7%9a%84%e5%8c%ba%e5%88%ab)
  - [闭包](#%e9%97%ad%e5%8c%85)
  - [装饰器](#%e8%a3%85%e9%a5%b0%e5%99%a8)
  - [深拷贝和浅拷贝的区别是什么？](#%e6%b7%b1%e6%8b%b7%e8%b4%9d%e5%92%8c%e6%b5%85%e6%8b%b7%e8%b4%9d%e7%9a%84%e5%8c%ba%e5%88%ab%e6%98%af%e4%bb%80%e4%b9%88)
  - [说明os,sys模块不同，并列举常用的模块方法？](#%e8%af%b4%e6%98%8eossys%e6%a8%a1%e5%9d%97%e4%b8%8d%e5%90%8c%e5%b9%b6%e5%88%97%e4%b8%be%e5%b8%b8%e7%94%a8%e7%9a%84%e6%a8%a1%e5%9d%97%e6%96%b9%e6%b3%95)
  - [参考资料](#%e5%8f%82%e8%80%83%e8%b5%84%e6%96%99)


# python 面试常见问题总结

## python函数——形参中的：*args和**kwargs

args 是 arguments 的缩写，表示位置参数；kwargs 是 keyword arguments 的缩写，表示关键字参数。

- args: 表示的就是将实参中按照位置传值，多出来的值都给args，且以**元组**的方式呈现
- kwargs: 表示的就是形参中按照关键字传值把多余的传值以字典的方式呈现

```
# 1,2,3以元组方式进行传值， x=1,y=2以字典方式传值
def f_compose_args(*args, **kwargs):
    print(args, kwargs)
f_compose_args(1,2,3, x=1, y=2)
```


## Python是如何进行内存管理的？

1. 对象的引用计数机制

    Python内部使用引用计数，来保持追踪内存中的对象，所有对象都有引用计数。 引用计数增加的情况： 1，一个对象分配一个新名称 2，将其放入一个容器中（如列表、元组或字典） 引用计数减少的情况： 1，使用del语句对对象别名显示的销毁 2，引用超出作用域或被重新赋值 sys.getrefcount( )函数可以获得对象的当前引用计数 多数情况下，引用计数比你猜测得要大得多。对于不可变数据（如数字和字符串），解释器会在程序的不同部分共享内存，以便节约内存。

2. 垃圾回收

    1，当一个对象的引用计数归零时，它将被垃圾收集机制处理掉。 2，当两个对象a和b相互引用时，del语句可以减少a和b的引用计数，并销毁用于引用底层对象的名称。然而由于每个对象都包含一个对其他对象的应用，因此引用计数不会归零，对象也不会销毁。（从而导致内存泄露）。为解决这一问题，解释器会定期执行一个循环检测器，搜索不可访问对象的循环并删除它们。

3. 内存池机制

    Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统。 1，Pymalloc机制。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。 2，Python中所有小于256个字节的对象都使用pymalloc实现的分配器，而大的对象则使用系统的malloc。 3，对于Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。

##  python  _init__和 _new__的区别

```
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        instance = object.__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age

p = Person("Wang", 33)

# 结果
in __new__
in __init__
```

1. __init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。

2. __new__ 通常用于控制生成一个新实例的过程。它是类级别的方法。

可以通过__new__实现单例模式:
```
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2) 
```
更多参考: [Python面试之理解__new__和__init__的区别](https://zhuanlan.zhihu.com/p/35943253)


## 闭包
闭包，顾名思义，就是一个封闭的包裹，里面包裹着自由变量，就像在类里面定义的属性值一样，自由变量的可见范围随同包裹，哪里可以访问到这个包裹，哪里就可以访问到这个自由变量。

```
def adder(x):
    def wrapper(y):
        return x + y
    return wrapper

adder5 = adder(5)
# 输出 15
adder5(10)
# 输出 11
adder5(6)
```
参考: [一步一步教你认识Python闭包](https://zhuanlan.zhihu.com/p/26934085)


## 装饰器
装饰器放在一个函数开始定义的地方，它就像一顶帽子一样戴在这个函数的头上。和这个函数绑定在一起。在我们调用这个函数的时候，第一件事并不是执行这个函数，而是将这个函数做为参数传入它头顶上这顶帽子，这顶帽子我们称之为 装饰器 。

参考: [一篇文章搞懂装饰器所有用法](https://zhuanlan.zhihu.com/p/65968462)


## 深拷贝和浅拷贝的区别是什么？

- 深拷贝是将对象本身复制给另一个对象。这意味着如果对对象的副本进行更改时不会影响原对象。
- 浅拷贝是将对象的引用复制给另一个对象。因此，如果我们在副本中进行更改，则会影响原对象

```
import copy
# 深拷贝
b = copy.deepcopy(a)
# 浅拷贝
c = copy.copy(a)  
```

## 说明os,sys模块不同，并列举常用的模块方法？

os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口。sys模块负责程序与Python解释器的交互，提供了一系列的函数和变量用户操作Python运行时的环境。

```
os.path.join
os.mkdir
sys.argv
sys.exit() 
```




## 参考资料

- [Python面试之理解__new__和__init__的区别](https://zhuanlan.zhihu.com/p/35943253)
- [一步一步教你认识Python闭包](https://zhuanlan.zhihu.com/p/26934085)
- [一篇文章搞懂装饰器所有用法](https://zhuanlan.zhihu.com/p/65968462)

