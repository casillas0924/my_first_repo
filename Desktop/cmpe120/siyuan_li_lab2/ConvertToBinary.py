def convertToBinary(a):
    appendingString=""
    while True:
        quotient=a//2
        remainder=a%2
        appendingString=str(remainder)+appendingString
        a=quotient
        if(quotient==0):
            break
    return "0b"+appendingString

def main():
    #input a testing
    print(convertToBinary(25)) #it should be 0b11001

if __name__=='__main__':
    main()