ls=[23,True,'Sneha']
sa=[23,True,'Sneha',[2.4,False]]
print(sa)
print(ls)
print(type(ls))

#Indexing
ls=['a','b','c','d'] 
print(ls[1])
print(ls[-1])
print(ls[0],ls[-2])

#list manipulation
ls[1]='s'
print(ls)

#ls.append(adds in last)
ls.append(23)
print(ls)

#ls.insert(insertd at any index) 
ls.insert(3,'me')
print(ls)

#del(for deleting particular indexes)
del(ls[3])
print(ls)

#list slicing
print(ls[2:4])

#len function
for i in range(len(ls)): 
    print(ls[i])

a=[1,5,24,45,34,0]
maximum = -1
for i in a:
    if maximum < i:
        maximum = i
print(maximum)    

print(max(a))
print(min(a))

for i in a:
    print(a)

for i in a:
    if i < len(a):
        print(i)    

#split function
s=input()
print(s)   
print(s.split())  
print(s.rstrip())   