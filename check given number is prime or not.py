# write a python script to checl whether number is prime or not ..

n=int(input("enter a number"))

if 2>n:
    print("number is not prime ")
else:    
    for i in range(2,n):
        if n%i==0:
            print("number is not prime")
            break

    else:
        print("number is prime")

'''n=9
while 2>n:
    print("number is not prime")
else:  
    for i in range(2,n):
        if n%i==0:
            print("number is not prime")
            break

    else:
        print("number is prime")
'''