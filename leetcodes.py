#Count Special Quadruplets (773 ms and 13.5 MB)
def CountSpecialQuadruplets(nums):
    count = 0
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-2):
            for k in range (j+1, len(nums)-1):
                sum = nums[i] + nums[j] + nums[k]
                count += nums[k+1:].count(sum)
    return count

#Count Good Triplets (1081 ms and 13.5 MB)
def CountGoodTriplets(arr, a, b, c):
    count = 0
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            if abs(arr[i]-arr[j]) <= a:
                for k in range(j+1, len(arr)):
                    if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        count += 1
    return count
 
#Revere Integer
def ReverseInteger(x):
        sum = 0
        if x > 0:
            while x>0:
                dig = x%10
                sum = sum*10 + dig
                x = x//10
        else:
            x = -x
            while x>0:
                dig = x%10
                sum = sum*10 + dig
                x = x//10
            sum = -sum
        if sum > 2**31 or sum<-2**31:
            return 0
        else:
            return sum

def MinimumAverageDifference(nums):
    prefix = [nums[0]]
    les = 10000
    ind = 0
    for i in range(1, len(nums)):
        prefix.append(prefix[i-1]+nums[i])
    
    for i in range(0, len(nums)-1):
        avg1 = int(prefix[i]/(i+1))
        avg2 = int((prefix[-1]-prefix[i])/(len(nums)-(i+1)))
        diff = abs(avg1 - avg2)
        if diff < les:
            les = diff
            ind = i
                    
    return ind

num = [4,2,0]
print(MinimumAverageDifference(num))