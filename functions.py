temp1=[23,45,22]
def f_c(temp1):
    return((temp1-32)*(5/9))
# print(f_c(temp1))
#  for i in (f_c(temp)):
#      print(i))
#      print(temp[i])
for i in temp1:
    print(f_c(i))


def length(ls):
    count=0
    for i in ls:
        count+=1
    return count
ls=[1,3,2,4,9,56,34,45]
for i in range(length(ls)):
    print(ls[i])

a=[True,54,34,56]
print("\n",length(a))   

def mini(b):
    x=11000
    for i in b:
        if i < x:
            x=i
    return x

lo=[2,5,12,34,100,-1]
print(mini(lo))  
print(min(lo))
print(sum(lo))

def power(a,b):
    return a**b

print(power(2,10))
print(pow(2,10))     