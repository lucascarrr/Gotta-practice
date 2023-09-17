# Longest Palindromic Substric
def longestPalindrome(s:str) -> str:
    string_len = len(s)
    storage = [[1] * string_len for _ in range(string_len)]
    
    for j in range (1, string_len):
        i = j-1
        if (s[i] == s[j]): storage[i][j] = 1 
        else: storage[i][j] = 0

    max_tupe = (0,0)
    for a in range (2, string_len):
        for i in range (string_len-a):
            j = i+a
            if (s[i] == s[j] and storage[i+1][j-1] == 1): 
                storage[i][j]=1 
                if (j-i) > (max_tupe[1]-max_tupe[0]): max_tupe=(i,j)
            else: storage[i][j]=0

    for e in storage:
        print(e)
    print(max_tupe)          
    return s[max_tupe[0]:max_tupe[1]+1]

str = "noonmadam"
print(f"Longest Palindromic Substring in {str} is {longestPalindrome(str)}") #answer is bb
