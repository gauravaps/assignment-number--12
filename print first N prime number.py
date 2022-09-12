# write a python script to print first N prime number.
start=int(input("enter starting value"))
end=int(input("enter end value"))
for i in range(start,end+1):
    if i>2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)    