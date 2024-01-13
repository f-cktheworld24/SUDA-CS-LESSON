import re
def func1(num):
    n = 0
    while num//2!=0:
        if num%2==1:
            n+=1
        num//=2
    if num == 1:
        n+=1
    return n


def func2(lst):
    n = len(lst)
    pd = 0
    i = 0
    while i<n-1:
        j = i+1
        while j<n:
            if lst[i]==lst[j]:
                pd+=1
            j+=1
        i+=1
    return pd


def func3(lst):
    lst_str = []
    lst_int = []
    lst_float = []
    for i in lst:
        if type(i)==str:
            lst_str.append(i)
        if type(i)==int:
            lst_int.append(i)
        if type(i)==float:
            lst_float.append(i)
    lst_str.sort(reverse=True)
    lst_float.sort(reverse=True)
    lst_int.sort(reverse=True)
    lst_pd = lst_str+lst_float+lst_float
    return lst_pd


def func4(text):
    lst = list(map(str,text.split()))
    dic = {}
    for i in lst:
        if i in "!@#$%^&*()_+{}:<>?[];',./":
            lst.remove(i)
        else:
            dic[i]=0
    for i in lst:
        if i in dic:
            dic[i]+=1
    return dic


def func5(s,n):
    sr = ""
    if n>=10:
        n%=10
    for i in s:
        if ord("a")<=ord(i)<=ord("z"):
            if ord(i)+n>ord("z"):
                a =ord(i)-26+n
            else:
                a = ord(i)+n
            sr+=chr(a)
        elif ord("A") <= ord(i) <= ord("Z"):
            if ord(i) + n > ord("Z"):
                a = ord(i) - 26 + n
            else:
                a = ord(i) + n
            sr += chr(a)
        else:
            sr+=i
    return sr


def func6(s):
    a = re.findall('\d{3,4}-\d{7,8}',s)
    return a


def func7(lst):
    n = len(lst[0])
    i = 0
    lst_1 = []
    while i < n:
        j =i+1
        lst_1.append(lst[i][i])
        while j<n:
            lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
            j+=1
        i+=1
    for i in range(n):
        for j in range(n):
            lst[i][j]-=min(lst_1)
    return lst


def func8(L):
    lst = []
    a = len(L)
    b = len(L[0])
    i = 0
    while i<a:
        j = 0
        pd = 0
        while j<a:
            if i == j:
                j+=1
                continue
            if L[i][0]>L[j][0] and L[i][1]>L[j][1] and max(L[i])>min(L[j]):
                pd = 1
            j+=1
        if pd ==0:
            lst.append(L[i])
        i+=1
    lst.sort(key=lambda x:x[0],reverse=False)
    return lst
if __name__=='__main__':
    print(func8([(4, 2), (88, 21), (25, 27), (40, 72), (17, 33), (79, 14), (67, 66), (7, 18)]))
    print(func4('Happy I am happy are you happy'))
    pass
