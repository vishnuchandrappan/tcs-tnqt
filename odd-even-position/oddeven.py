num = int(input())                  # reding the number & converting it to integer
result = 0                          # variable to store the result
while( num > 0 ):                   #
    lastDigit = num % 10            # ODD POSITION DIGIT any positive number % 10 gives the lastDigit of the number. % being mod operator is used for finding remainder
    result  += lastDigit            # odd position value is added to the result variable
    num = int( num/10 )             # for getting other digits, we need to eliminate the last one. num/10 eleminates the last digit. converting to int is necessary
    if( not num ):                  # similar to if(num == 0)
        break                       # the above condition is true when there is odd number of digits
    lastDigit = num % 10            # EVEN POSITION DIGIT
    result -= lastDigit             # even position value is SUBTRACTED from the result
    num = int( num/10 )
print(result)                       # print the result
