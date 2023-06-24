def a(grid):
    lst=[]
    x=grid.__len__()
    for i in range(x):
        for j in grid[i]:
            lst.append(j)
    lst.sort()
    ans=lst[0]
    n=lst.__len__()
    for i in range(1,n):
        if lst[i]!=lst[i-1]:
            ans=ans+lst[i]
    print(ans)
a([[1,1,1],[1,1,1],[1,1,1]])