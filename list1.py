n=int(input())
ls=[]
for i in range(n):
    p=input().split()
    if(p[0]=='insert'):
        ls.insert(int(p[1]),int(p[2]))
    elif(p[0]=='print'):
        print(ls)
    elif(p[0]=='remove'):
        ls.remove(int(p[1]))
    elif(p[0]=='append'):
        ls.append(int(p[1]))
    elif(p[0]=='sort'):
        ls.sort()
    elif(p[0]=='pop'):
        ls.pop()
    elif(p[0]=='reverse'):
        ls.reverse()