n = int(input())
nums = list(map(int,input().split()))

sum = 0

for i in range(n) :
    for j in range( i+1, n ) :
        sum += abs( nums[i]-nums[j] )

print (sum * 2)