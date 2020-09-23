# break强制结束循环
# n=1
# while n<5:
#     if n==3:
#         break
#     n+=1
# print(n)
#
# #continue直接进入下一个循环
# n=0
# for x in[0,1,2,3,4]:
#     if x%2==0:
#         continue
#     n+=1
# print(n)
#
# #else或者
# n=1;
# while n<5:
#     print("var N is :",n)
#     n+=1
# else:
#     print(n)
#
# for c in "Hello":
#     print("String:",c)
# else:
#     print(c)


#输入整数找出平方根
n=input("输入一个整数:")
n=int(n)
for i in range(n):
    if i*i==n:
        print("整数平方根",i)
        break #强制结束回圈
else:
    print("没有找到整数的平方根")

