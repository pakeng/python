# 测试IO
def read_text(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            print(line.strip())


def write_text(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('测试的写入内容')
        f.write('又一行')
        f.write('\n')
        f.write('end line')


def write_append_text(path):
    with open(path, 'a', encoding='utf-8', errors='ignore') as f:
        f.write('\nappend test text')


if __name__ == '__main__':
    read_text('../res/readtextfile.txt')
    # write_text('../res/writetestfile.txt')
    print('------测试的读取内容---------')
    read_text('../res/writetestfile.txt')
    write_append_text('../res/writeAppendTextFile.txt')
    read_text('../res/writeAppendTextFile.txt')

# 写入的时候编码方式跟随电脑当前的编码方式，如果需要保存特定的编码要传入编码名称

