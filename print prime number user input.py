#print prime number two given number..

start=int(input("enter a starting number"))
end=int(input("enter a ending number"))
for i in range(start,end+1):
    if i>2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)    