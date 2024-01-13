def func8(s):#首先判断是进行了题目中步骤二三四的哪一个
    if ord(s[0]) in range(ord('0'),ord('9')+1) and s[1] in range(ord('0'),ord('9')+1) and s[-1] not in range(ord('0'),ord('9')+1):
        n=int(s[0])
        s2=s[1:]#步骤二
    elif ord(s[0]) in range(ord('0'),ord('9')+1) and s[1] in range(ord('0'),ord('9')+1) and s[-1] in range(ord('0'),ord('9')+1):
        n=int(s[-1])
        s2[:-1]#步骤三
    else:
        if ord(s[0]) in range(ord('0'),ord('9')+1):
            n=int(s[0])
            s2=s[1:]#步骤一
            
        else:
            n=int(s[-1])
            s2=s[:-1]
    d1={k:chr(k) for k in range(ord('0'),ord('9')+1)}#0-9的ascii码字典
    d2={k:chr(k) for k in range(ord("a"),ord("z")+1)}#a-z的ascii码字典
    d3={k:chr(k) for k in range(ord("A"),ord("Z")+1)}#A-Z的ascii码字典
    # 加密是循环右移，解密就是要循环左移
    lst_1=[list(d1.keys())[0]-i for i in range(1,n+2)]#0-9时,ascii码左移n的列表
    lst_2=list(d1.values())[-1:-n-2:-1]#0-9时,从9左移n次的列表
    d1_1=dict(zip(lst_1,lst_2))#合并成字典1
    lst_3=[list(d2.keys())[0]-i for i in range(1,n+2)]#a-z时,ascii码左移n的列表
    lst_4=list(d2.values())[-1:-n-2:-1]#a-z时,从z左移n次的列表
    d2_1=dict(zip(lst_3,lst_4))#合并成字典2
    lst_5=[list(d3.keys())[0]-i for i in range(1,n+2)]#同上
    lst_6=list(d3.values())[-1:-n-2:-1]
    d3_1=dict(zip(lst_5,lst_6))
    d1.update(d1_1)
    d2.update(d2_1)
    d3.update(d3_1)
    fin=''
    for i in s2:
        if ord(i) in range(ord('0'),ord('9')+1):
            fin+=d1[ord(i)-n]
        elif ord(i) in range(ord('a'),ord('z')+1):
            fin+=d2[ord(i)-n]
        elif ord(i) in range(ord('A'),ord('Z')+1):
            fin+=d3[ord(i)-n]
        else:
            fin+=i
    return fin
if __name__=="__main__":
    print(func8("abcde12#9"))
            
    