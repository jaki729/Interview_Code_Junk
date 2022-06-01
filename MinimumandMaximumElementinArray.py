https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
def getMinMax( a, n):
    if(n%2==0):
        mx=max(a[0],a[1])
        mn=min(a[0],a[1])
        i=2
    else:
        mx=mn=a[0]
        i=1
    while(i<n-1):
        if a[i]<a[i+1]:
            mx=max(mx,a[i+1])
            mn=min(mn,a[i])
        else:
            mx=max(mx,a[i])
            mn=min(mn,a[i+1])
        i+=2
    return (mn,mx)
