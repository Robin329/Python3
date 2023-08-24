import sys


def main():
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
    print(sys.version)
    print(sys.version_info)
    print("Platform: %s"%sys.platform)

def print_test():
    str1 = "world"
    str2 = "..."
    print("-- hello ",str1," ", str2, " --")

if __name__ == '__main__':
    main()
    print_version()
    print_test()
