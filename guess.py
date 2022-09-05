import random
start = input ("请决定随机数开始值：")
start = int (start)
end = input ("请决定随机数末尾值：")
end = int (end)
number = random.randint(start , end)
i = 0
while True:
    user = input ("请猜一个数字：")
    i = i + 1
    user = int (user)
    if user > number:
        print ("你猜的数字比答案大哦！")
    elif user < number:
        print ("你猜的数字比答案小哦！")
    else:
        print ("终于猜对了！")
        print ("这是你猜的第",i,"次哦")
        break
    print ("这是你猜的第",i,"次哦")