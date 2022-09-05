import random
number = random.randint(1,100)
while True:
    user = input ("请猜一个数字：")
    user = int (user)
    if user > number:
        print ("你猜的数字比答案大哦！")
    elif user < number:
        print ("你猜的数字比答案小哦！")
    else:
        print ("终于猜对了！")
        break