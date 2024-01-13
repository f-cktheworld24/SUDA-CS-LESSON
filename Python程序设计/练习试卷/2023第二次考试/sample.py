
def func1(num):
    a=format(num,'b')
    return a.count('1')


def func2(lst):
    counter=0
    for j in range(len(lst)):
        for i in range(j):
            if lst[i]==lst[j]:
                counter+=1
    return counter

def func3(lst):
    l=[i for i in lst if isinstance(i,str)]
    l2=[i for i in lst if isinstance(i,float)]
    l3=[i for i in lst if isinstance(i,int)]
    l.sort(reverse=True)
    l2.sort(reverse=True)
    l3.sort(reverse=True)
    return l+l2+l3


def func4(text):
    l=text.split(' ')
    return {i:l.count(i) for i in l} if text else {}


def func5(s,n):
    if n>=10:
        n%=10
    s1=''.join([chr(i) for i in range(ord('a'),ord('z')+1)]*2)
    s2=''.join([chr(i) for i in range(ord('A'),ord('Z')+1)]*2)
    s3=''
    for i in s:
        if i in s1:
            s3+=s1[(s1.index(i)+n)]
        elif i in s2:
            s3+=s2[(s2.index(i)+n)]
        else:
            s3+=i
    return s3


def func6(s):
    import re
    a=re.findall('[0-9]{3,4}-[0-9]{7,8}',s)
    return a


def func7(lst):
    temp=999
    l=[[0 for i in range(len(lst))] for j in range(len(lst[0]))]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            l[i][j]=lst[j][i]
            if i==j and lst[i][j]<temp:
                temp=lst[i][j]
    for i in range(len(l)):
        for j in range(len(l[0])):
            l[i][j]-=temp
    return l


def func8(L):
    l=[]
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i][0]<L[j][0] and L[i][1]==L[j][1]:
                
                l.append(L[j])
            elif L[i][0]<L[j][0] and L[i][1]<L[j][1]:
                #print("L[i]",L[i],"(L[j]",L[j])
                l.append(L[j])
            elif L[i][0]==L[j][0] and L[i][1]<L[j][1]:
                
                l.append(L[j])
    for i in range(len(L)-1,0,-1):
        for j in range(i-1,-1,-1):
            if L[i][0]<L[j][0] and L[i][1]==L[j][1]:
                
                l.append(L[j])
            elif L[i][0]<L[j][0] and L[i][1]<L[j][1]:
                #print("L[i]",L[i],"(L[j]",L[j])
                l.append(L[j])
            elif L[i][0]==L[j][0] and L[i][1]<L[j][1]:
                
                l.append(L[j])
    l2=[i for i in L if i not in l]
    l2.sort(key=lambda x:x[0])
    return l2
def func9(a,b):
    if a==[]:
        return []
    result={}
    for i in range(len(b)-1):
        for j in range(i+1,len(b)):
            result[b[i]+b[j]]=j
    while sum(b) not in list(result.keys()):
        for i in list(result.keys()):
            if result[i]==len(b)-1:
                continue
            for j in range(result[i]+1,len(b)):
                result[i+b[j]]=j
    return [i for i in a if i in result.keys()]
def func10(str1,str2):
    d=dict(zip([chr(i) for i in range(ord("A"),ord('H')+1)]+[str(i) for i in range(1,9)],[i for i in range(1,9)]*2))
    x2=max(d[str1[0]],d[str2[0]])
    x1=min(d[str1[0]],d[str2[0]])
    y2=max(d[str1[1]],d[str2[1]])
    y1=min(d[str1[1]],d[str2[1]])
    if x2-x1>=y2-y1:
        d=y2-y1+x2-x1-(y2-y1)
    else:
        d=x2-x1+y2-y1-(x2-x1)
    return d
def func11(lst):
    if lst==[]:
        return []
    lst2=[i for i in lst if i]
    length=len(lst2)
    temp=0
    length2=length
    while length2!=0:
        temp+=1
        length2//=10
    for i in range(1,length+1):
        temp2=str(i)
        if temp>1:
            temp2=format(temp2,'0>'+str(temp)+'s')
        lst2[i-1]=temp2+'-'+lst2[i-1]
    return lst2
if __name__=='__main__':
    print(func1(15))
    print(func2([1,2,3]))
    print(func3([3, 'python', 1.1]))
    print(func4(''))
    print(func5('abc1122def', 15))
    print(func6('vw1122  abc  a'))
    print(func7([[4, 5], [6, 7]]))
    print(func8([(42, 11), (49, 46), (89, 33), (89, 96), (13, 1), (89, 11), (45, 39), (23, 5)]))
    print(func9([11,6,5,7,8,4],[1,2,3]))
    print(func10("E8","A1"))
    print(func11(["28", "38", "48", "68", "", "12", "12", "4", "126", "8", "12"]))