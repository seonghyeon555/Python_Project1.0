# def say(msg="Hello"): #初始资料
#     print(msg)
# say("HELLO")
# say()#呼叫初始定义资料

def divide(n1,n2):
    result=n1/n2
    print(result)
divide(2,4)
divide(n2=2,n1=4)#呼叫函数，以参数名称对应资料

#无限参数 无限参数以tuple资料处理
def say(*msgs): #*开头
    for msg in msgs:
        print(msg)

say("HELLO","WILLIAM","TEE")

def power(base,exp=0):
    print(base**exp)
power(3,2)
power(4)

def avg(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    print(sum/len(numbers))

avg(6,6,6)