
- [python 快速入门](#python-%e5%bf%ab%e9%80%9f%e5%85%a5%e9%97%a8)
  - [python简介](#python%e7%ae%80%e4%bb%8b)
  - [python版本](#python%e7%89%88%e6%9c%ac)
  - [基本的数据类型](#%e5%9f%ba%e6%9c%ac%e7%9a%84%e6%95%b0%e6%8d%ae%e7%b1%bb%e5%9e%8b)
  - [容器](#%e5%ae%b9%e5%99%a8)
    - [Lists](#lists)
  - [字典](#%e5%ad%97%e5%85%b8)
  - [集合](#%e9%9b%86%e5%90%88)
  - [元组](#%e5%85%83%e7%bb%84)
  - [函数](#%e5%87%bd%e6%95%b0)
  - [类](#%e7%b1%bb)
  - [参考资料](#%e5%8f%82%e8%80%83%e8%b5%84%e6%96%99)

# python 快速入门

## python简介

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

1. Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。

2. Python 是交互式语言： 这意味着，您可以在一个 Python 提示符 >>> 后直接执行代码。

3. Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。

## python版本
python目前支持两个大的版本Python, 2.7 and 3.5. 令人疑惑的是python的2和3的版本不兼容，因此使用2的版本的代码在3中可能会出现不兼容的现象，目前推荐使用python 3+的版本作为开放和学习。

## 基本的数据类型

像大多数语言一样，Python具有许多基本类型，包括整数，浮点数，布尔值和字符串。这些数据类型以其他编程语言所熟悉的方式运行。

**数值：** 
整数和浮点数可以像其他语言一样使用：

```
x = 3
print(type(x)) # Prints "<class 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"
```
python不像其他编程语言，其不支持x++和x--这种操作。

**布尔值：**

不同于其他编程语言，python使用英文代替(||, &&等):

```
t = True
f = False
print(type(t)) # Prints "<class 'bool'>"
print(t and f) # Logical AND; prints "False"   与
print(t or f)  # Logical OR; prints "True"     或
print(not t)   # Logical NOT; prints "False"   非
print(t != f)  # Logical XOR; prints "True"
```

**字符串**
python对字符串的支持是很强大的:

```
hello = 'hello'    # 单引号
world = "world"    # 双引号也可
print(hello)       # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw12)  # prints "hello world 12"
```

## 容器

Python包含几种内置的容器类型: lists, dictionaries, sets和tuples.

### Lists


列表与数组的Python等效，但可调整大小，并且可以包含不同类型的元素：

```
xs = [3, 1, 2]    # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])     # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [3, 1, 'foo']"
```

**切片:** 除了一次访问一个列表元素，Python还提供了简洁的语法来访问子列表。这称为切片

```
nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"
```

**循环:** 

```
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
```


如果要访问循环体内每个元素的索引，请使用内置的枚举函数enumerate：

```
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
```

**列表推导式(List comprehensions):**

列表推导式可以将循环这种方式表达的更为简洁，如下所示: 

```
# 构建1-10的列表
l1 = [x for x in range(1,11)]

# 可以对迭代的元素进行操作
l2= [x*x for x in range(1,11)]

# for循环后跟if语句
l3 = [i for i in range(1,11) if i % 2 == 0]

# 嵌套列表合成单个列表 [[1,2],[3,4]] -> [1,2,3,4]
l = [[1,2],[3,4]]
l4 = [j for i in l for j in i]
```

## 字典

字典是是无序的键值对（key:value）集合，等同于c++中的unordered_map哈希表。同一个字典内的键必须是互不相同的。
其形式为 :键：值

```
# 创建字典
d = {'cat': 'cute', 'dog': 'furry'}  
# 获取key值
print(d['cat'])       # Get an entry from a 
# 查询key是不是在字典中
print('cat' in d)     
# 新增key:value
d['fish'] = 'wet'     # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
# 如果没有key，则报错，所以一般不直接进行取值操作
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
# 使用get获取key值，如果key不存在，则赋予默认值
print(d.get('monkey', 'N/A')) 
# 删除元素
del d['fish']      
```

**迭代**

迭代字典很简单，和列表差不多:

```
d = {'person': 2, 'cat': 4, 'spider': 8}
# 注意这种遍历的是key的值
for animal in d:          #key
    legs = d[animal]      #value
    print 'A %s has %d legs' % (animal, legs)
# Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"

# 如果想直接获得键值对, 使用iteritems:

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)
# Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"
```

**字典的表达式**

```
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print even_num_to_square  # Prints "{0: 0, 2: 4, 4: 16}"

```

## 集合
集合，也就是没有顺序的，同时所有的元素都不相同的集合。A set is an unordered collection of distinct elements，用英文更好的表达其含义。集合同样是用花括号创建：

```
animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"
```

集合的循环很列表一致：

```
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)
# Prints "#1: fish", "#2: dog", "#3: cat"
```

## 元组

元组是（不可变的）有序值列表。元组在很多方面类似于列表。最重要的区别之一是，元组可以用作字典中的键和集合的元素，而列表则不能。这是一个简单的示例：

```
# 使用括号
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
```

## 函数

python函数的定义使用def:

```
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))
# Prints "negative", "zero", "positive"

```

## 类

类的定义很简单，如下所示的基本结构: 
```
class Greeter(object):

    # 构造函数
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # 方法
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"
```

更多内容参考我的github: :https://github.com/yqtaowhu

## 参考资料

- [Python Numpy Tutorial](http://cs231n.github.io/python-numpy-tutorial/#numpy)
- [Python 快速入门教程](https://blog.csdn.net/taoyanqi8932/article/details/52588699)