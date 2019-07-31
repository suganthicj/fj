x11,y11=map(str,input().split())

for p in range(len(x11)):
    if x11[p]==y11:
        print(p+1)
        break
