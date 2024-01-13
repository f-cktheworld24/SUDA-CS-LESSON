def func1(y,m,d):
    d3={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    d2={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#闰
    if (m not in range(1,13)) or d>31:
        return -1
    days=0
    if (y%4==0 and y%100!=0) or y%400==0:
        for i in range(1,m):
            days+=d2[i]
        days+=d
    else:
        for i in range(1,m):
            days+=d3[i]
        days+=d
    return days
def func2(m,n):
    if m<0 or n<0:
        return None
    else:
        for i in range(m+1):
            if m-i<0:
                return None
            else:
                if i*2+4*(m-i)==n:
                    return i,m-i
def check(lst,i):
    if i==len(lst)-1:
        return True
    elif lst[0]-lst[1]!=lst[i]-lst[i+1]:
        return False
    return check(lst,i+1)
def func3(lst):
    if len(lst)==0 or len(lst)==1:
        return None
    elif len(lst)==2:
        return True
    else:
        lst.sort()
        return check(lst,0)
def func4(lst):
    if not lst:
        return None
    else:
        for i in lst:
            if type(i)!=int:
                return None
        for i in lst:
            if len(lst)%2!=0:
                return lst[len(lst)//2]
            else:
                return round((lst[len(lst)//2]+lst[(len(lst)//2)-1])/2)
def func5(sentence):
    sentence=sentence.lower()
    lst=sentence.split(" ")
    lst2=[]
    if len(lst) not in range(3,12):
        return None
    d={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
    for i in lst:
        lst2.append(str(d[i]))
    return "".join(lst2)
def func6(a,b,c,d):
    s=list()
    for i in range(a,b+1):
        for j in range(c,d+1):
            s.append(i/j)
    return len(set(s))
def adds2(s3,j,n,s2):
    if j==len(s3):
        s3.insert(j,s2)
        return ''.join(s3)
    s3.insert(j,s2)
    return adds2(s3,j+n+1,n,s2)
def func7(s1,s2,n):
    import re
    temp=0
    if n>=len(s1):
        s1+=" "*(n-len(s1))
        return s1+s2
    if len(s1)%n!=0:
        while len(s1)%n!=0:
            s1+=" "
    s3=list(s1)
    return adds2(s3,n,n,s2)
def func8(s):
    import re
    if '<' not in s:
        return s
    l=re.findall("<[^<>]*>",s)
    s2=s
    for i in l:
        j=i.upper()
        temp='['+(j[1:len(j)-1]+'-')+str(len(j[1:len(j)-1]))+']'
        s2=s2.replace(i,temp)
    return s2
if __name__=="__main__":
    print(func8('he defended <_abc>,his decision to <43>'))
    

