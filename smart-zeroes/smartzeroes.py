l = list(map(int, input().split(" ")))
maxLength = len(str(l[1]))

while( l[0] < l[1]+1 ):
    digitDifference = maxLength-len(str(l[0]))
    print("0"*digitDifference+str(l[0]),end=' ')
    l[0]+=1
