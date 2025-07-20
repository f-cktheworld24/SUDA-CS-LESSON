def plus(lst,start,n):
    global lst2
    mid=(min(lst)+max(lst))//2
    j=0
    for i in range(start,n):
        if lst[i]<=mid:
            j+=1
    #print(lst[:j],lst[j:],j)
    lst2.append(sum(lst[:j]))
    lst2.append(sum(lst[j:]))
    #print(lst2)
    return j
def consectutive(lst,start,n,q_test):
    temp=plus(lst,start,n)
    #print(lst[:temp],lst[temp:],temp) 
    if lst[:temp]==[] or lst[temp:]==[]:
        #print("?")
        return
    if q_test<lst[temp]:
        consectutive(lst[temp:],0,len(lst[:temp]),q_test)
    else:
        consectutive(lst[temp:],0,len(lst[:temp]),q_test)
        consectutive(lst[:temp],0,len(lst[temp:]),q_test)    


if __name__=="__main__":
    t=int(input())#测试用例的数量t
    while t:
        n,q=map(int,input().split(" "))#数组长度n和要测试整数的总数q
        lst=list(map(int,input().split(" ")))#被测试数组的内容
        lst2=[sum(lst)]
        lst_q=[int(input()) for i in range(q)]#输入进行测试的整数,存放于列表lst_q
        lst.sort()
        for i in lst_q:
            consectutive(lst,0,n,i)
            if i in lst2:
                print("Yes")
            else:
                print("No")
        t-=1