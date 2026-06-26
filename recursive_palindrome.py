def isPalindrome(str):
    if len(str) == 0:
        return True
    if str[0] != str[len(str)-1]:
        return False
    return isPalindrome(str[1:-1])

print(isPalindrome('rain'))
print(isPalindrome('malayalam'))
print(isPalindrome('radar'))
print(isPalindrome('english'))