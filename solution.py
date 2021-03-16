import sys
###Max fun of arrays

xy = input().split(' ')
xy=int(xy[0])

#print(xy)
def frog_sort(a,b):
    c= [0]*len(a)
    d= [*range(len(a))]
    for i in range(len(a)):
        c[i]=[0]*3
        c[i][0]=a[i]
        c[i][1]=b[i]
        c[i][2]= d[i]
    
    return real_sort(c,0)

def real_sort(c,myn):
    if not c:
        return 0
    
    
    min1 = c[0]
    min1= min1[0]
    min_i = 0 
    for ij in range(len(c)):
        if c[ij][0]<min1:
            min1 = c[ij][0]
            min_i = ij
    
    pivot = c[min_i][2]
    
    c.pop(min_i)
    for xx in c:
        
        if xx[2]<= pivot:
            while xx[2] <=pivot:
                xx[2] += xx[1]
                myn += 1

    return myn + real_sort(c,0)


        

def new_para():
    x = input().split(' ')
    x=int(x[0])
    b=input().split(' ')
    c=input().split(' ')
    
    for i in range(x):
        b[i] = int(b[i])
        c[i]= int(c[i])
    
    print(frog_sort(b,c))
    
    
for ijk in range(xy):
    new_para()
