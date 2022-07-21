def TowerofHanoi(n,src,aux,dest):
    if n==1:
        print('Moved',n,'from',src,'to',dest)
        return

    TowerofHanoi(n-1,src,dest,aux)
    print('Moved',n,'from',src,'to',dest)
    TowerofHanoi(n-1,aux,src,dest)

print('Enter the numbers of disk: ')
n=int(input())
TowerofHanoi(n,'src','aux','dest')