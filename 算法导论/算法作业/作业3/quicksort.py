"""lst=[37,104,99,173,130,15,37,135,72,97]
for i in range(1,len(lst)):
    for j in range(i):
        if lst[i]<lst[j]:
            lst[j],lst[i]=lst[i],lst[j]
    print("第{:2d}轮".format(j+1),lst)
print(lst)"""

# def searchInsert(nums, target):
#     if target in nums:
#         return nums.index(target)
#     else:
#         temp=1
#         for i in range(len(nums)-1):
#             if (nums[i]<=target and nums[i+1]>=target) or (nums[i]>=target and nums[i+1]<=target):
#                 temp=i+1
                
#             elif target>=nums[-1] and len(nums)!=1:
#                 temp=len(nums)
#             elif target<=nums[0] and len(nums)!=1:
#                 temp=0
#         if target<=nums[0]:
#             temp=0
#         print(temp)
#         return temp
# if __name__ == "__main__":
#     searchInsert([1,3,5,6],7)

# import random
# def quicksort(a,start,end):
#     ranind=random.randint(start,end)
#     a[start],a[ranind]=a[ranind],a[start]
#     pivot=start
#     j=start+1
#     for i in range(start+1,end+1):
#         if a[i]<=a[pivot]:
#             a[i],a[j]=a[j],a[i]
#             j+=1
#     a[pivot],a[j-1]=a[j-1],a[pivot]
#     pivot=j-1
#     return pivot


# def Quicksort(a,start,end):
#     if start>=end:
#         return 
#     pivot=quicksort(a,start,end)
#     Quicksort(a,start,pivot-1)
#     Quicksort(a,pivot+1,end)
# if __name__=="__main__":
#     a=[8,5,12,6,4,3,7,9,2,1,10,11]
#     Quicksort(a,0,11)
#     print(a)

def plus(lst,start,n):
    global lst2
    mid=(min(lst)+max(lst))//2
    j=0
    for i in range(start,n):
        if lst[i]<=mid:
            j+=1
    #print(lst[:j],lst[j:],j)
    if lst[j:]!=[] and lst[:j]!=[]:
        lst2.append(sum(lst[:j]))
        lst2.append(sum(lst[j:]))
    #print(lst2)
    return j
def consectutive(lst,start,n):
    temp=plus(lst,start,n)
    #print(lst[:temp],lst[temp:],temp) 
    if len(lst[:temp])==0 or len(lst[temp:])==0:
        #print("?")
        return
    if lst[:temp][0] not in lst2 or lst[temp:][0] not in lst2:
        consectutive(lst[:temp],0,len(lst[:temp]))
        consectutive(lst[temp:],0,len(lst[temp:]))    


if __name__=="__main__":
    t=int(input())#测试用例的数量t
    while t:
        n,q=map(int,input().split(" "))#数组长度n和要测试整数的总数q
        lst=list(map(int,input().split(" ")))#被测试数组的内容
        lst2=[sum(lst)]
        lst_q=[int(input()) for i in range(q)]#输入进行测试的整数,存放于列表lst_q
        lst.sort()
        consectutive(lst,0,n)
        for i in lst_q:
            if i in lst2:
                print("Yes")
            else:
                print("No")
        t-=1
