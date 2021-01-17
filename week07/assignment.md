1. 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：list,tuple,str,dict, collections.deque

Ans: 

- 扁平序列: str
- 可變序列: list, dict, collections.deque
- 不可變序列: tuple, str

---

2. 自定义一个 python 函数，实现 map() 函数的功能。

```python
def my_map(func, iterable):

    if not callable(func):
        raise TypeError(f"{type(func)} is not callable")

    try:
        iter(iterable)
    except TypeError as e:
        raise TypeError(f"{type(iterable)} is not iterable")

    for n in iterable:
        yield func(n)
```

---

3. 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

```python
import time

def clock(func):
    def fucntion(*args):
        time0 = time.perf_counter()
        result = func(*args)
        timePass = time.perf_counter() - time0

        print("%s is running for [%0.8fs] time" % (func.__name__, timePass))

        return result
    return fucntion

@clock
def test_function(n):
    return 1 if n <= 1 else test_function(n-1)

test_function(10)
```