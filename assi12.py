# write a python script to calculate LCM of two number

a=30
b=50
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break
    