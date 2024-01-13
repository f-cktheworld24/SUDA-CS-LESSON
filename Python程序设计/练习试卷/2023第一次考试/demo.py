import math
def func2(a,b,c):
    if (b**2-4*a*c)<0:
        return None
    elif (b**2-4*a*c)>=0:
        return (-b+math.sqrt((b**2-4*a*c)))/2*a
def func3(t):
    def spe(t):
        if t<=30:
            return 0
        elif t>30 and t<=60:
            return 5
        else:
            return t
    def cost_per_day(cost_base,t):
        cost=cost_base
        if t>60 and t<240:
            cost+=(((t-60)//15)+1)*2
        elif t==240:
            cost=29
        elif t>240 and (t-240)%30==0:
            cost+=29+(((t-240)//30))*5
        elif t>240 and ((t-240)%30)!=0:
            cost+=29+(((t-240)//30)+1)*5
        if cost>150:
            cost=150
        return cost
            
    if t>24*60:
        cost_base=(t//(24*60))*150
        cost=cost_base
        t2=t%(24*60)
        if spe(t2)==0:
             pass
        elif spe(t2)==5:
            cost+=spe(t2)
        else:
            cost=cost_per_day(cost_base,spe(t2))
    elif t<=24*60:
        cost_base=0
        cost=cost_base
        if spe(t)==0:
             pass
        elif spe(t)==5:
            cost+=spe(t)
        else:
            cost=cost_per_day(cost_base,t)
    return cost

def func4(f0,f1,num):
    if num==1:
        return f0
    elif num==2:
        return f1
    fn=((-1)**num)*(func4(f0,f1,num-1)+func4(f0,f1,num-2))
    return fn

def func5(lst):
    def search(lst):
        maxlist=[]
        for i in range(len(lst)-1):
            maxlist.append([lst[i]+lst[i+1],i,i+1])
        maxlist2=sorted(maxlist,key=lambda maxlist:(-(maxlist[0]),maxlist[1]))
        return maxlist2[0]

    if len(lst)<2:
        return []
    elif len(lst)==2:
        return lst 
    else:
        while len(lst)!=2:
            n1=search(lst)[1]
            lst[n1]=search(lst)[0]//2
            lst.pop(n1+1)
        return lst
def func6(lst):
    def surplus(lst2):
        lst=[]
        cout=[]
        total=0
        start=0
        for i in range(start,len(lst2)):
            if lst2.count(i)==1:
                lst.append(i)#把所有同样元素去掉确保列表元素各不相同
            elif lst2.count(i)>1:
                total+=1
                start+=1
        for i in range(len(lst)-1):
            cout2=[lst[i]]
            for j in range(i+1,len(lst)):
                if lst[j]>cout2[-1]:
                    cout2.append(lst[j])
                    print(cout2)
            if cout2!=[lst[i]]:
                cout.append(cout2)
        cout3=[x for x in cout2]
        for y in lst:
            if y not in cout3:
                total+=1
        no=0
        control=0
        for k in range(len(cout)-1):
            for l in cout[k]:
                if control==1:
                    control=0
                    continue
                elif control==0:
                    for m in range(k+1,len(cout)):
                        if l in cout[m]:
                            no+=1
                            control=1
                            break
        return len(cout)-no+total


    # def surplus(lst,start,total):
    #     if start==len(lst)-2:
    #         print(total)
    #         return total
    #     for i in range(start,len(lst)-1):
    #         if lst[i+1]>=lst[i]:
    #             index=i
    #         elif lst[i+1]<lst[i]:
    #             break
    #     if index>start:
    #         total+=1
    #     surplus(lst,index,total)       
    if lst==[]:
        return -1
    elif len(lst)==1:
        return lst
    elif lst==sorted(lst,reverse=True):
        return 0
    else:
        return surplus(lst)

def multi_till_1(num):#递归实现阶乘
    if num==1:
        return 1
    multi=num*multi_till_1(num-1)#存放乘积
    return multi
 
def fibo(n):#经典的斐波那契数列
    if n==1:
        return 0
    if n==2:
        return 1
    fn=fibo(n-1)+fibo(n-2)
    return fn
def func7(lst):
    counter=0
    if lst==list(sorted(lst,reverse=True)):
        return 0
    elif lst==[]:
        return -1
    for i in range(len(lst)-1):
        lst_temp=[lst[i]]
        flag=1
        for j in range(i+1,len(lst)):
            if lst[j]>=lst_temp[-1]:
                lst_temp.append(lst[j])
                if len(lst_temp)==2 and flag==1:
                    base=lst_temp
                    flag=0
            else:
                print(lst_temp,counter)
                counter+=1
                lst_temp=lst_temp[:-1]
                if lst_temp==[]:
                    lst_temp=base
                
    return counter
def findSubsequences(nums):
    if not nums:
        return []
    pres = {(nums[0], )}
    for i in nums[1:]:
        pres.update({j+(i, ) for j in pres if j[-1] <= i})
        pres.add((i, ))
    return [list(i) for i in pres if len(i) > 1]


if __name__=="__main__":
    print(findSubsequences([12, 12, 4, 126, 8, 12]))
    #print(fibo(10),multi_till_1(3))
    