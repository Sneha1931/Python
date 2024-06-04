# for i in "Sneha":
#     #print(i)
#     #print(type(i))
#      print(i,end="\n")
# for i in range(11):
#      print(i)
# sum=0     
# for k in range(1,6):
#     cube=k*k*k
#     sum+=cube
# print(cube)
# print(sum)
# sum=0
# i=0
# while i<=5:
#     sum+=i*i
#     i+=1

# print(sum)

#=0
# while(i<10):
#     if(i==5):
#         continue
#     print(i)
#     i+=1      This leads to an infinite loop
# i = 0
# while (i<10):
#     i+=1
#     if(i==5):
#         continue
#     print(i)  

n=int(input())
# sum=0
# for i in range(0,n+1):
#     sum+=i
# print(sum/n)
sum=0
for i in range(1,n+1):
    square=i*i
    sum+=square
print(sum)    
    