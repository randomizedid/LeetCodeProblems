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
 
#Reverse Integer
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

# I find this problem to be of particular interest: There is a car with a fixed capacity, and an array of trips in the form [numPassengers, from, to].
# The goal is to find out if the car can complete all the trips without exceeding the capacity. The solutions implies building a difference array.
def carPooling(trips, capacity):
    arr = [0] * (max(trip[2] for trip in trips) + 1)
    for (value, left, right) in trips:
        arr[left] += value
        arr[right] -= value

    curr = 0
    for i in range(len(arr)):
        curr += arr[i]
        if curr > capacity:
            return False
    return True

# 3Sum (9747 ms and 17.9 MB)
def ThreeSum(nums):
    nums.sort()
    ans = []
    for i in range(0, len(nums)-2):
        left = i+1
        right = len(nums)-1
        while(left<right):
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left+=1
            elif sum == 0:
                if [nums[i], nums[left], nums[right]] not in ans:
                    ans.append([nums[i], nums[left], nums[right]])
                left+=1
            else:
                right-=1
    return ans

# The two following functions are a solutions I copied from the user "granola" for the problem Number of Islands.
# I find it a smart solution without using graphs.
def NumberOfIslands(grid):
    islands = 0
    for i in range(len(grid)):  
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands += 1
                part_of_island(i,j,grid)
    return islands

def part_of_island(i, j,grid):
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
        return
    else:
        grid[i][j] = '0'
    part_of_island(i,j+1,grid)
    part_of_island(i,j-1,grid)
    part_of_island(i+1,j,grid)
    part_of_island(i-1,j,grid)

# Maximum Subarray
def MaximumSubarray(nums):
    curr = ans = nums[0]
    for i in range(1, len(nums)):
        curr = max(nums[i], curr+nums[i])
        ans = max(ans, curr)

    return ans

# Roman to Integer (runtime error)
def romanToInteger(s):
    newdic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    sum = i = 0
    while i<len(s)-1:
        if(s[i:i+2]) in newdic:
            sum+=newdic[s[i:i+2]]
            i+=2
        else:
            sum+=newdic[s[i]]
            i+=1
    return sum

s = "MCMXCIV"
print(romanToInteger(s))