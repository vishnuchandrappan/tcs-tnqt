s=raw_input()
l = [s.upper()]
d = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
decimalValue=0
i=0
while(len(l[0])>0):
    lastDigit = l[0][-1]
    if (lastDigit in d):
        decimalValue += d[lastDigit]*(17**i)
    else:
        decimalValue += int(lastDigit)*(17**i)
    i+=1
    l[0] = l[0][:-1]

print(decimalValue)


'''
every line begining with
    >> is code
    # is inline comment
    all others are comments.

>>s=raw_input()

    reading the base-17 value to varibale 's'
    In python, string is immutable. Which means, it cannot be altered.
    so we store the string as first element of a list.
    list is nothing but array.


>>l = [s.upper()]
    converting the string to upper case with string.upper()
    this is similar to l[0] = s or initializing an array with one string


>>d = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
    dictionary in python


    The logic behind problem is similar to
    OCTAL to DECIMAL conversion (replace 8 with 17)
    or
    BINARY to DECIMAL conversion (replace 2 with 17)
    or
    HEXA-DECIMAL to DECIMAL conversion (replace 16 with 17) (preffered - since we need to take care of A,B,C,D,E and F)


>>decimalValue=0                  # variable to store the decimal equivalent
>>i=0                             # variable for determining the power of 17.

>>while(len(l[0])>0):
>>    lastDigit = l[0][-1]        # l[0] is our string. l[0][-1] will give the last charecter. Search for 'python slicing' for more information
>>    if (lastDigit in d):        # 'in' operator is used to find if an element is present in list,dictionary,set etc..
>>        decimalValue += d[lastDigit]*(17**i)       # if A,B,C,D,E,F or G
>>    else:
>>        decimalValue += int(lastDigit)*(17**i)     # ** is called exponent operator 17**2 is square of 17.         TIP: for finding sqaure root use NUMBER**(0.5)
>>    i+=1                        # (try to find significance of this statement)
>>    l[0] = l[0][:-1]            # string slicing. [:-1] will eliminate the last charecter from the string

>> print(decimalValue)


'''
