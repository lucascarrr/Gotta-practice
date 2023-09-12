# Longest Increasing Subsequence 

sequence = [10, 22, 9, 33, 21, 50, 41, 60, 76, 90]
# output = len (sequence)

def lis(input):
    L = [1] * len(input)

    for i in range (1, len(L)):
        for j in range (0, i):
            if (input[i] > input[j]):
                L[i] = max(L[i], L[j]+1)
    
    maxi = 0
    for e in L:
        maxi = max(maxi, e)

    return maxi


print (lis(sequence))
