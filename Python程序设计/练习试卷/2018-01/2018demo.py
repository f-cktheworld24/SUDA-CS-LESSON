def func1(x):
    if x>=0:
        return 5*x
    elif x<0:
        return 3*abs(x)+1
def func2(x):
    if x>=10:
        return 10
    elif x>=8 and x<10:
        return 8*(x**3)
    elif x>=3 and x<8:
        return 3*x**2
    elif x>=0 and x<3:
        return x+1
    elif x<0:
        return abs(x)
def func3(m,n):
    res=0
    if m<0 or n<0 or m>n:
        return None
    else:
        for i in range(m,n+1):
            if i %2==1:
                res+=i
        return res
def func4(m,n):
    l=[]
    for i in range(m,n+1):
        while i!=0:
            temp=i%10
            l.append(temp)
            i=i//10
    return l.count(2)
def func5(n):
    if n<0:
        return None
    elif n==0:
        return [1,0,0]
    else:
        count=0
        lt=[]
        while n!=0:
            lt.append(n%10)
            n//=10
            count+=1
        return [count,sum(lt),max(lt)]
def func6(m,n):
    if m<=0 or n<=0:
        return None
    else:
        m2=m
        lt=[]
        while m!=0:
            lt.append(m%10)
            m//=10
        if lt[-1]+n>=10:
            temp=0
            lt[-1]=(lt[-1]+n)%10
            for i in lt[::-1]:
                temp=(temp+i)*10
            return temp//10
        elif lt[-1]+n<10:
            temp=0
            lt[-1]=(lt[-1]+n)
            for i in lt[::-1]:
                temp=(temp+i)*10
            return temp//10
        elif m2<100:
            return m2
def func7(k,lst):
    if k>=len(lst):
        lst.reverse()
        return lst
    else:
        l3=lst[:k]
        l3.reverse()
        l3+=lst[k:]
        return l3
def func8(v,lst):
    lt=[[] for i in range(len(lst))]
    lt2=[]
    lt3=[]
    for i in range(len(lst)):
        temp=i
        temp2=lst[i]
        while temp2!=0:
            lt[temp].append(temp2%10)
            temp2//=10
    for j in lt:
        lt2.append(sum(j)/len(j))
    for k in range(len(lst)):
        if lt2[k]>=v:
            lt3.append(lst[k])
    lt3.sort(reverse=True)
    return lt3
def func9_1(num,l):
    if num==0:
        return l
    l.append(num%10)
    return func9_1(num//10,l)
def func9(num):
    l=[]
    # while num!=0:
    #     l.append(num%10)
    #     num//=10
    # return l
    return func9_1(912,l)
if __name__=="__main__":
    print(func9(921))