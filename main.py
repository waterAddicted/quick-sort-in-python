from array import *

def partitie(x,l,r):
    i = l - 1
    
    pivot = int(x[r])
    
    for j in range(l,r):
        if x[j] < pivot:
            i += 1
            aux = x[j]
            x[j] = x[i]
            x[i] = aux
    aux = x[i+1]
    x[i+1] = x[r]
    x[r] = aux
    return int(i+1)
 





def quick_sort(x,l,r):
    if l<r:
        
        pivot=int(partitie(x,l,r))
        print("aici") 
        quick_sort(x, l, int(pivot - 1))
        quick_sort(x, int(pivot + 1), r)
        

n=int(input("Lungimea vectorului"))
x=array('i',[])
for i in range(0,n):
    k = int(input())
    x.append(k)
print(x)
quick_sort(x,0,int(n-1))  
print(x)
