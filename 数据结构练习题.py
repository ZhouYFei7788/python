"""
给你两个整数 num1 和num2，返回这两个整数的和。
示例 1:
输入:num1=12，num2=5
输出:17
解释:num1是12，num2是5，它们的和是12+
5=17 ，因此返回 17 。
示例 2:
输入:num1=-10，num2=4
输出:-6
解释:num1+num2=-6，因此返回 -6。
"""
def add(num1, num2):
    """计算二个整数的和"""
    return num1 + num2

num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

print("结果是:", add(num1, num2))