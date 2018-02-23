nums=[2,7,11,15]
target=9
d=[]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if (nums[i]+nums[j])==9:
            print [i,j]
print nums
