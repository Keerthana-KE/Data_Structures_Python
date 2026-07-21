def almost_palindrome(s):
    for i in range(len(s)):
        str=s[:i] + s[i+1:]
        if(str==str[::-1]):
            return True
    return False

s=input("enter a string:")
s=s.replace(" ","").lower()
if(s==s[::-1]):
    print("palindrome")
elif(almost_palindrome(s)):
    print("almost a palindrome")
else:
    print("not a palindrome")