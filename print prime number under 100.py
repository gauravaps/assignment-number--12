# write a python scipt to print all prime number under 100.
from stringprep import in_table_c12
'''start=int(input("inter starting value")) 
end=int(input("enter a end value"))
for i in range(start,end+1):
    if i>2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)'''

s=50
for i in range(1,s+1):
    if i>2:

        for j in range(2,i):

            if i%j==0:

                break
        else:
            print(i)                