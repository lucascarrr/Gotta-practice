#Jump Game

def canJump(nums: list[int]) -> bool:
    n = len(nums)
    arr = [False] * n
    arr[0] = True
    
    for i in range (1, n):
        for j in range (i-1, -1, -1):
            if arr[j] and j+nums[j] >= i:
                arr[i] = True 
                break 
    
    return arr[-1];

    

print(canJump([3,0,8,2,0,0,1]))
