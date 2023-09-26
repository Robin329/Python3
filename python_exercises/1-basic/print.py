import sys
import inspect
from builtins import print as _print
from sys import _getframe

def main():
    print("==============================")
    print(2 + 3)  # addition(+)
    print(3 - 1)  # subtraction(-)
    print(2 * 3)  # multiplication(*)
    print(3 / 2)  # division(/)
    print(3 ** 2)  # exponential(**)
    print(3 % 2)  # modulus(%)
    print(3 // 2)  # Floor division operator(//)

    # Checking data types

    print(type(10))  # Int
    print(type(3.14))  # Float
    print(type(1 + 3j))  # Complex
    print(type('Asabeneh'))  # String
    print(type([1, 2, 3]))  # List
    print(type({'name': 'Asabeneh'}))  # Dictionary
    print(type({9.8, 3.14, 2.7}))  # Set
    print(type((9.8, 3.14, 2.7)))  # Tuple
    print(type(3 / 2))


def print_version():
    print("==============================")
    print(sys.version)
    print(sys.version_info)
    print("Platform: %s" % sys.platform)


def print_info():  # 定义一个打印行数和函数名的函数
    print("==============================")
    frame = inspect.currentframe()  # 获取当前的栈帧对象
    info = inspect.getframeinfo(frame)  # 获取栈帧对象的信息
    print(f"File: {info.filename}")  # 打印文件名
    print(f"Line: {info.lineno}")  # 打印行号
    print(f"Function: {info.function}")  # 打印函数名

# sys模块中的_getframe函数会返回一个frame实例，它有下列属性：
# ‘clear’, ‘f_back’, ‘f_builtins’, ‘f_code’, ‘f_globals’, ‘f_lasti’, ‘f_lineno’, ‘f_locals’, ‘f_trace’, ‘f_trace_lines’, ‘f_trace_opcodes’
# 其中 ‘f_lineno’ 可以返回_getframe函数执行时所在行的行数。
# _getframe函数的参数为整型时会返回_getframe(int)所在int层级的属性。
# __main__：如果为本文件的print，则显示《__main__》，其它导入文件的，则显示 《文件名》
#
# 自定义print函数
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} : '        # 注此处需加参数 1。
    return _print(f"{__name__}:{s}", *arg, **kw)

def print_test():
    str1 = "world"
    str2 = "..."
    print("-- hello ", str1, " ", str2, " --")


if __name__ == '__main__':
    main()
    print_version()
    print_test()
    print_info()
