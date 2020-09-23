#while
n=1
sum=0 #纪录累加的结果
while n<=5:#True无限循环
    print("number",n)
    sum=sum+n
    n+=1
print(sum)

#for
for x in[4,1,2]:
    print("list of doc",x)

for c in "hello":
    print("list of word",c)

for y in range(3,6):#range可以定义开头和结尾
    print("list",y)
    sum=sum+y
print(sum)