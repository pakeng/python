def say_hello():
    print("hello world")
    # 测试list数据结构
    class_mates = ['BOb', 'Michael', 'Tracy']
    print(class_mates)
    # 追加元素
    class_mates.append('Vito')
    print(class_mates)
    # 测试插入元素
    class_mates.insert(4, 'Yy')
    print(class_mates)
    # 测试删除元素
    class_mates.pop(1)
    print(class_mates)
    print("删除之后的1位置元素", class_mates[1])
    # 测试替换元素
    class_mates[2] = "---new mata-data ---"
    print(class_mates)
    # 测试元素中插入列表
    class_mates_mata = ['sublist', 'sublist-data']
    class_mates.append(class_mates_mata)
    print(class_mates)


# 测试tuple数据结构
def test_tuple():
    print('Test tuple')
    class_mates = ['Bob', 'Xiao A']
    tuple_data = ('tuple1', 'tuple2', class_mates)
    print(tuple_data)
    # 获取数量
    print('元素 tuple1 的数量是 ', tuple_data.count('tuple1'))
    print('元素 tuple0 的数量是 ', tuple_data.count('tuple0'))
    # 测试tuple指向不可变
    tuple_data[2].append('Xiao B')
    print(tuple_data)


# 测试dict
def test_dict():
    print("Test dict")
    class_mates = ['Bob', 'Xiao A']
    tuple_data = ('tuple1', 'tuple2', class_mates)
    dict_data = {"key1": "value1", 1: "value2", 'key3': class_mates, 'key4': tuple_data}
    print(dict_data)
    if 1 in dict_data.keys():
        print(dict_data[1])
    if 2 not in dict_data.keys():
        print('2 not in keys')
    dict_data["key3"].append("ceshi")
    print(dict_data)
    # 测试删除
    dict_data.pop(1)
    print('After delete key = 1, dict_data = ', dict_data)


# 测试set
def test_set():
    print("Test set")
    list_data = ['1', '2', 3]
    set_data = set(list_data)
    print(set_data)
    # 测试添加一个元素
    set_data.add(2)
    print(set_data)
    # 测试删除一个元素 随机弹出一个元素 如果set是空的会抛出一个异常
    mate = set_data.pop()
    print('pop one mata, mata =', mate)
    print(set_data)
    # 测试删除一个元素 如果没有元素会报错
    if '2' in set_data:
        set_data.remove('2')
        print(set_data)
    else:
        print('delete fail key = "2" not in set')
    # 测试 tuple 放入set
    test_tuple_data = ('1', '2')
    test_tuple_data2 = ('3', '4', [1, 2, 3])
    set_data.add(test_tuple_data)
    print(set_data)
    # 测试可知 当元组中有列表或者别的可变对象的时候就无法加入到set中
    # set_data.add(test_tuple_data2)
    print(set_data)


# main方法 程序入口方法
if __name__ == '__main__':
    say_hello()
    test_tuple()
    test_dict()
    test_set()
