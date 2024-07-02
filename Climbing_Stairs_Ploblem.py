#climb the ladder
'''
`you can climb with one or two step
`how many ways when climb N stairs
'''
#solution1
def ladder(N):
    count = 0
    
    def step(n):
        nonlocal count #关键字声明count是函数外的变量，避免创建一个新的局部变量
        
        if n == N:
            count += 1
            return
        
        for i in range(1, 3):
            if n + i <= N:
                step(n + i)
    
    step(0)  # 从0开始爬楼梯
    print(count)

N = int(input())
ladder(N)
#存在递归效率不高，可能运行超时的情况

#solution2
def ladder(N):
    if N == 0:
        return 1
    
    dp = [0] * (N + 1)
    dp[0] = 1  # 到达第0层的方法数为1，即不走
    dp[1] = 1  # 到达第1层的方法数为1，只有一种方法，走一步
    
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[N]

N = int(input())
print(ladder(N))
#彭罗斯阶梯问题
