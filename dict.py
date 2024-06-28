d={"name":"Sneha","followers":50,"online":{"data":True}
}
"""
keys: name ,followers,online
values:"Sneha",50,True

"""
for i in d.keys():
    print(d[i])
# print(d)    
# print(type(d))
# print(type(d.keys()))
# print(d.values())
# print(d["online"])
# print(d["followers"])
# print(d["online"]["data"])
# d['sports']='Badminton'
# print(d)
#print(d["name"][1])
# d.update({"hobby":"painting"}) 
# print(d)
#del d["name"][0]
#print(d)
def ping(n):
    if(n%2==0):
        return True
    return False
def printing(num):
    val=ping(num)
    if(val==True):
        print("Number is even")
    else:
        print("Number is odd")

number=int(input())
printing(number)
 
    