def checkPalindrome(inputString):
    revString = inputString[::-1]
    if (inputString == revString):
        return True
    else:
        return False
