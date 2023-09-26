
def compare():
    flag0 = 1 == 1
    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = 1 and 2
    flag4 = 2 and 0
    flag5 = 1 or 0
    flag6 = not  (1 == 2)
    print("flag0 =",flag0)
    print("flag1 =", flag1)
    print("flag2 =", flag2)
    print("flag3 =", flag3)
    print("flag4 =", flag4)
    print("flag5 =", flag5)
    print("flag6 =", flag6)

def Fahrenheit():
    f = float(input('Please enter temperature in Fahrenheit: '))
    c = (f - 32) / 1.8
    print('Fahrenheit: %.1f => Celsius: %.1f' % (f, c))
    print(f'{f:.1f}:Fahrenheit => {c:.1f}:Celsius')

def radius_circle():
    radius = float(input('Please enter the radius of the circle:'))
    perimeter = 2 * 3.1416 * radius
    area = 3.1516 * radius
    print('perimeter:%.2f' % perimeter)
    print('area:%.2f' % area)

def leap_year():
    year = int(input("Please input year:\n"))
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    print('is leap:',is_leap)

if __name__ == '__main__':
    compare()
    Fahrenheit()
    radius_circle()
    leap_year()