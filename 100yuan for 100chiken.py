"""
question:One Hundred Coins for One Hundred Chickens
Given the following conditions:

A rooster (cock) costs 5 coins each.
A hen costs 3 coins each.
Three chicks cost 1 coin 
You need to use exactly 100 coins to buy exactly 100 chickens. How many roosters, hens, and chicks do you need to buy?

问题：百钱白鸡
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
试用穷举法编程解决此问题
有几种解法？
"""

#方法一

cockprice=5 #价格
henprice=3
chickenprice_3=1
way=0 #方法
for cocknum in range(0,21):
    for hennum in range(0,34):
        for chickennum in range(0,101):
            if cocknum*cockprice+hennum*henprice+chickennum*chickenprice_3==100 and cocknum+hennum+chickennum*3==100: #同时满足一百块和一百只鸡
                way+=1
                print("way",way,":")
                print("cock:",cocknum)
                print("hen:",hennum)
                print("chicken:",chickennum)

#方法二
solutions = []

# 鸡翁x只，鸡母y只，鸡雏z只
for x in range(0, 101):  # 鸡翁数量从0到100
    for y in range(0, 101):  # 鸡母数量从0到100
        z = 100 - x - y  # 鸡雏数量
        if z >= 0 and 5*x + 3*y + z//3 == 100 and z % 3 == 0:
            solutions.append((x, y, z))

print(f"总共有 {len(solutions)} 种解法")
for solution in solutions:
    print(f"鸡翁: {solution[0]} 只, 鸡母: {solution[1]} 只, 鸡雏: {solution[2]} 只")
