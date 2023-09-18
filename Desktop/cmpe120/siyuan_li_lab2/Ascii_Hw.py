#this file is written for the ascii hw

def convertUpper(a):
    return chr(ord(a)-32)

def convertLower(a):
    return chr(ord(a)+32)

def isAlpha(a):
    number=ord(a)
    return (number in range(65,90))or (number in range(97,122))

def isDigit(a):
    number=ord(a)
    return number in range(48,57)

def isSpecial(a):
    flag1=not isAlpha(a)
    flag2=not isDigit(a)
    flag3=ord(a) in range(33,126)
    return flag1 and flag2 and flag3

def main():
    #testing for convert the character to upper
    character_input=input("please enter a character in lower case")
    character=character_input[0]
    print(convertUpper(character))

    # testing for convert the character to upper
    character_input_lower = input("please enter a character in upper case")
    character_lower = character_input_lower[0]
    print(convertLower(character_lower))

    #testing for whether it is an alphabet
    character_input_alpha=input("please enter a character")
    if isAlpha(character_input_alpha[0]):
        print("it is an alphabet")
    else:
        print("it is not an alphabet")

    #testing for whether it is a digit
    character_input_digit=input("please enter a digit")
    if isDigit(character_input_digit[0]):
        print("it is a digit")
    else:
        print("it is not a digit")

    #testing for whether it is a speical character
    character_input_special=input("please enter a speical character")
    if isSpecial(character_input_special[0]):
        print("it is a speical character")
    else:
        print("it is not a special character")

if __name__=='__main__':
    main()