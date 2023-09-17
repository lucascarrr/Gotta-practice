# jump game 2

def jump(nums: list[int]) -> int:
    n = len(nums)
    arr = [0] * n   
    arr[0] = 0
        
    for i in range(1,n):
        for j in range (i-1, -1, -1):
            if (nums[j] >= i-j):
               arr[i] = arr[j]+1 
    
    print(arr)
    return arr[n-1]

print(jump([2,3,0,1,4]))
