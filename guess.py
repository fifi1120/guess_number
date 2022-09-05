import random
number = random.randint(1,100)
i = 0
while True:
    user = input ("请猜一个数字：")
    i = i + 1
    user = int (user)
    if user > number:
        print ("你猜的数字比答案大哦！")
        print ("这是你猜的第",i,"次哦")
    elif user < number:
        print ("你猜的数字比答案小哦！")
        print ("这是你猜的第",i,"次哦")
    else:
        print ("终于猜对了！")
        break
print ("这是你猜的第",i,"次哦")