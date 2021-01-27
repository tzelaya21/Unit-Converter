#from array import *
#arr = []
#arr1 = []

"""for x in range(3):
    for i in range(3):
        var1 = int(input("Enter your array item: "))
        arr1.append(int(var1))
        #print(type (var1))
        #int(input("Enter your array item: "))

    arr.append(arr1)
    arr1 = []

for x in range(3):
    for i in range(3):
        print (arr[x][i], end=' ')

    print()"""
#print("Enter a number to check if its a palindrom number or not.")
#n = int(input("Enter a number: "))
x = int(input("Enter a number which will be the lower bound of the range: "))
y = int(input("Enter a number which will be the upper bound of the range: "))
count1=0
count2=0
for i in range(x,y):
    n=i
    temp = n
    reverse = 0
    while n!=0:
        reverse += (n % 10)
        n = n // 10
        if n!=0:
            reverse = reverse * 10

    if temp == reverse :
        #print(temp," is a palindrom number.")
        count1+=1
    else :
        #print(temp," is not a palindrom number.")
        count2+=1

print("Palindrom numbers between ",x," and ",y," are ",count1)
print("Non-Palindrom numbers between ",x," and ",y," are ",count2)
#a,b,c =12,29,45

#x= repr(a+b+c)
#print(x)
#print(type(x))

#def sumfunc(val1,val2,val3):
#    return val1+val2+val3
#
#print(sumfunc(29,67,53))


