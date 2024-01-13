import math
def func1(n):
    if n>=60:
        return True
    else:
        return False
def func2(n):
    base=n//10
    if base<3:
        return base
    if base>=3 and base<5:
        return base+1
    elif base>=5:
        return base+(base//5)*3
def func3(n):
    sum_all=0
    for i in range(1,n):
        if i%2==0:
            print(i)
            sum_all+=i**2
    return sum_all
def func4(k):
    num=0
    for i in range(0,k):
        for j in range(0,k//2+1):
            if i+2*j<k:
                print("i",i,"2*j",2*j,"=",i+2*j)
                num+=1
    return num
def func5(a,b):
    if a%b==0 or b%a==0:
        return True
    else:
        return False
def func6(x):
    l=[]
    while x>0:
        l.append(x%2)
        x//=2
    return l.count(1)
def func7(lst):
    if len(lst)<3:
        return None
    else:
        lst.sort()
        return sum(lst[1:len(lst)])//len(lst)
def func8(lst):
    l=[]
    import math
    control1=1
    for i in lst:
        temp3=i
        if temp3>100 and temp3%100!=0 and temp3<=9999:
            temp=temp3%100
            temp1=temp3//100
            for j in range(2,int(math.sqrt(temp))+1):
                if temp%j==0:
                    control1=0
                    break
            for k in range(2,int(math.sqrt(temp1))+1):
                if temp1%k==0:
                    control1=0
                    break
        if control1 and i>100:
            l.append(i)
    return l
if __name__=="__main__":
    print(func8([2, 203, 9797]))