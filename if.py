#if判断式
#part1
if True:
    print("True 执行")
else:
    print("Fasle 不执行")

#part2
x=input("请输入数字：")
x=int(x)
if x>200:
    print("大于200")
elif x>100:
    print("大于100，小于200")
else:
    print("小于100")

n1=int(input("number1: "))
n2=int(input("number2: "))
op=input("运算：+,-,*,/: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援")


#3.6为止不支援switch