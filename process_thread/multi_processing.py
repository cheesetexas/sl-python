from multiprocessing import Process
import os

'''multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：'''
#  子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getppid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getppid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process ends.')

'''
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动,
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
'''
