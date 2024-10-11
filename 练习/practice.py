print("hello world!")
a=10
print("指数演示",a**a)
print("整除演示",a//3)
name="我是岳兴彦"
print(name+",一个正在学习python是小菜")
age=19
height=170
print("年龄%d,身高%d"%(age,height))
web="bilibili"
print(f"现在正在宿舍观看{web}学习python")
#number=input("请告诉我你的学号")
#print(number)



#演示for循环打印九九乘法表
x=1
for x in range(1,10):
    i=1
    while i<=x:
        print("%d*%d=%d"%(i,x,i*x),end=' ')
        i+=1
    print("\n")


#列表练习
list_prac=[1,2,3,4,5,"上山打老虎"]
print(list_prac)
for i in range(6):
    print(list_prac[i],end=" ")
print(type(list_prac))