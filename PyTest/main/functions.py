# 测试函数


# 平方函数
def power(x):
    if not isinstance(x, (int, float)):
        raise TypeError("customer TypeError Msg")
    return x*x


# 测试多返回值
def multi_return(x, y):
    return y, x


# 测试默认参数
def power_n(x, n=2):
    if not isinstance(x, (int, float)):
        raise TypeError("error x type")
    result = x
    while n > 1:
        result *= x
        n = n-1
    return result


# 测试可变参数
def calc(*params):
    result = 1
    for x in params:
        result *= x
    return result


# 测试关键字参数
def key_word_params(x, n=1, *list_var, **kwargs):
    result = x
    print("n = ", n)
    print("list_var", list_var)
    print("kwargs = ", kwargs)
    return power_n(x, n)


# trim 字符串去除前后空格
def trim(str_):
    if len(str_) == 0:
        return str_
    if str_[0] == ' ':
        # 前部有空格
        return trim(str_[1:])
    elif str_[-1] == ' ':
        # 尾部有空格
        return trim(str_[:-2])
    return str_


# trim测试方法
def test_trim():
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')


# 迭代查找list中的最大和最小值
def find_max_min(list_):
    if len(list_) == 0:
        return None, None
    if not list_:
        return None, None
        # raise TypeError("param len should not zero")
    # 初始化最大和最小值 默认是第一个元素
    max_ = min_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    return min_, max_


# 测试 find_max_min 方法
def test_find_max_min():
    if find_max_min([]) != (None, None):
        print('测试失败!')
    elif find_max_min([7]) != (7, 7):
        print('测试失败!')
    elif find_max_min([7, 1]) != (1, 7):
        print('测试失败!')
    elif find_max_min([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')


# 程序主入口
if __name__ == '__main__':
    print(power(2))
    a, b = multi_return(1, 2)
    print(a, b)
    assert (power_n(2) == 4)
    assert (power_n(2, 3) == 8)
    params_ = (6, 2, 3, 4)
    result_ = calc(*params_)
    print(result_)
    result_ = key_word_params(2, *params_, *params_)
    print(result_)
    test_trim()
    test_find_max_min()

