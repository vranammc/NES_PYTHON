import string

def palindrome(X):
    #удаление лишних символов и регистра
    X = ''.join(char.lower() for char in X if char.isalnum())
    return X == X[::-1]

X = "А роза упала на лапу Азора"
if palindrome(X):
    print("TRUE")
else:
    print("FALSE")
