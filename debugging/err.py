"""如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。"""
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()

'''出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。 '''
