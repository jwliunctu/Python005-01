# 屬性

類屬性與對象屬性

類屬性: 內存只有一份

```python
class MyClass:
	pass

a=Myclass
b=Myclass

type(a)
type(b)

id(a)
id(b)

a.__class__()
b.__class__()

class Human2(object):
	#人為約定不可修改
	_age = 0
	
	# 私有屬性
	__fly = False

	# 魔術方法
	# 如 __init__

# 顯示所有子類
().__class__.__base__[0].__subclasses__()
```

# 方法

(三種方法都屬於類)

1. 普通方法: 至少一個self參數
2. @classmethod: 至少一個cls參數，表示該方法的類

    構造函數

    使用情境

    使用子類時，若需要根據自己變量名稱變化，就可引用父類的classmethod

    函數調用類並返回類(前處理)

3. @staticmethod: 由類調用，無參數

    額外處理的邏輯，和類和實例不相干

    沒有帶self和cls

# 屬性處理

__getattribute__()

__getattr__()

# 屬性描述符 property

描述器：實現特定協議(描述符)的類

property 類需要實現 __get__, __set__, __*delete__ 方法*

```python
class Teacher:
	def __init__(self,name):
		self.name = name

	def __get__(self):
		return self.name

	def __set__(self, value):
		self.name = value

pythonteacher = Teacher('yin')
```

```python
class Age(object):
	def __init__(self, default_age = 18):
		self.age_range = range(18, 66)
		self.default_age = default_age
		self.data = {}

	def __get__(self, instance, owner):
		return self.data.get(instance, self.default_age)

	def __set__(self, isinstance, value):
		if vaule not in self.age_range:
			raise ValueError('must be in (18-65)')

		self.data(isinstance) = value

class Student(object):
	age = Age()

if __name__ == '__main__':
	s1 = Student()
	s1.age = 30
	s1.age = 100
```

# 新式類

object 和 type 都屬於type 類 (class 'type')

type 類 由 type  元類自身創造的。 object 類是由元類 type 創建

object 的父類為空，沒有繼承任何類

type 的父類為 object 類 (class 'object')

# 類的繼承

單一繼承

多重繼承

菱形繼承 (鑽石繼承)

繼承機制 MRO

MRO的C3算法

# 設計模式

設計原則：SOLID

單一責任原則 The Single Responsibility Principle

開放式封閉原則 The Open Closed Principle

里氏替換原則 The Liskov Substitution Principle

依賴倒置原則 The Dependency Inversion Principle

接口分離原則 The Interface Segregation Principle

單例模式

1. 對象只存在一個實例
2. __init__ 和 __new__ 的區別:
    - __new__ 是實例創建之前被調用，返回該實例對象，是靜態方法
    - __init__ 是實例對象創建完成後被調用，是實例方法
    - __new__ 先被調用 __init__ 後被調用
    - __new__ 的返回值(實例)將傳遞給 __init__ 方法的第一個參數, __init__ 給這個實例設置相關參數

# 元類

元類是類的模板，用來創建類的類

```python
def hi():
	print('Hi metaclass')

Foo = type('Foo',(),{'say_hi':hi})
foo = Foo
foo.say_hi()
```

# Mixin模式

在程序運行過程中重新定義類的繼承，即動態繼承