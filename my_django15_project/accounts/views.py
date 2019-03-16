from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import numpy as np

# Create your views here.
@ensure_csrf_cookie
def home(request):
    return render(request,'accounts/login.html')
def register(request):
    username = request.POST.get('data')
    cat=int(request.POST.get('cat'))
    print(cat,"hiii")
    username=username.split(" ")
    l=[]

    for u in username:
        l.append(int(u))
    if cat==1:
        result=linearprob(l)
        arg={'mdata':result[:7]}
        return render(request,'accounts/hello.html',arg)
    if cat==2:
        print("hello")
        arr = [[0 for i in range(3)] for j in range(4)]
        brr = [0 for i in range(4)]
        #crr=[4068,1752,3429,2130,2854,1591,2203,1423,3017,2333,3923,4817,4876]
        c=len(bin(32-1))-2
        result=func(l,arr,brr,3,4,2,32,c,"")
        arg={'mdata':result}
        return render(request,'accounts/hello.html',arg)
    return render(request,'accounts/hello.html')







def linearprob(l):
    bucket=[0]*40
    col=0
    for i in range(len(l)):
        a=len(l)
        if bucket[l[i]%7]==0:
            bucket[l[i]%7]=l[i]
        else:
            j=l[i]%7
            while True:
                if bucket[j]==0:
                    bucket[j]=l[i]
                    break
                col=col+1
                j+=1
                if j==a:
                    j=0
    for b in range(a):
        print(str(bucket[b])+" ")
    print("total col is "+str(col))
    return bucket





def func(lst,arr,brr,n,nb,g,md,c,s):

    for k in lst:
        x = k % md
        bb = np.binary_repr(x, c)
        y =bb[0:g]
        z = int(y,2)
        if brr[z] < n:
            arr[z][brr[z]]=k
            brr[z] += 1
        else:

            print("bucket no",y, "is full for gain size ", g,"while inserting value",k)
            s="bucket no "+str(y) +" is full for gain size "+str(g)+" while inserting value "+str(k)+"\n"
            g += 1
            nb = 2 ** g
            arr = [[int(0) for i in range(n)] for j in range(nb)]
            brr = [int(0) for i in range(nb)]
            return func(lst,arr,brr,n,nb,g,md,c,"")
    print("gain size:",g,"   ","no of buckets[0-%d]:"%(nb-1),nb)
    s=s+"gain size: "+str(g)+"   "+" no of buckets:"+str(nb)+"\n"
    #print(s)
    print("keys","\t","mod",md,"\t","Binary","   ","Bucket no")
    s=s+"keys"+"\t"+"mod"+str(md)+"\t"+"Binary"+"   "+"Bucket no\n"

    print("-------------------------------------------")
    s=s+"-------------------------------------------\n"
    for i in range(nb):

        for j in range(n):
            if arr[i][j]!=0:

                print(arr[i][j],"\t","%.2d"%(arr[i][j]%md),"        ",np.binary_repr(arr[i][j]%md,c),"   ",i)
                s=s+str(arr[i][j])+" \t"+ str(arr[i][j]%md)+"        "+str(np.binary_repr(arr[i][j]%md,c))+"   "+str(i)+"\n"
    return s
