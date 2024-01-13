def cal_weight(s):#python考试第二题
    weight = 0
    for i in s:
        if 'a' <= i <= 'z':
            weight += ord(i)
    return weight // len(s)



def backtrack(start, target,b,res1,res2):#python考试第三题
    if target == 0:
        return True
    for i in range(start, len(b)):
        if b[i] in res1:
            continue
        if b[i] <= target and backtrack(i + 1, target - b[i],b,res1,res2):
            res1.append(b[i])
            res2.append(target)
            return True
    return False
def can_be_expressed(a, b):#python考试第三题
    res1 = []
    res2=[]
    for x in a:
        if backtrack(0, x,b,res1,res2):
            res2.append(x)
    res3=[]
    for y in res2:
        if y in a and y not in res3:
            res3.append(y)
    return res3

from collections import Counter#python考试第四题

def find_majority_elements(arr):
    if arr==[]:
        return -1
    count = Counter(arr)
    max_count = max(list(count.values()))
    lst=[key for key, value in count.items() if value == max_count]
    if len(lst)==1:
        return lst[0]
    else:
        lst.sort()
        return lst

def is_abnormal_sample(lst, center, k):#python考试第五题
    count = 1
    for i in range(1, len(lst)):
        if lst[i] > center and lst[i - 1] > center:
            count += 1
        elif lst[i] < center and lst[i - 1] < center:
            count += 1
        else:
            count = 1
        if count >= k:
            return True
    return False

def sort_students(lstID, lstScore):#python考试第六题
    students = sorted(zip(lstID, lstScore), key=lambda x: (-x[0], x[1]))
    return [student[1] for student in students]

def is_on_same_line(word):#python考试第七题
    for row in rows:
        if set(word.lower()).issubset(row):
            return True
    return False
def find_words_on_same_line(word_list):#python考试第七题
    rows = [
        set("qwertyuiop"),
        set("asdfghjkl"),
        set("zxcvbnm"),
    ]
    return [word for word in word_list if is_on_same_line(word)]
def func6(lst1,lst2):
    lst3=[[lst1[i],lst2[i]] for i in range(len(lst1))]
    print(lst3)
    lst3.sort(key=lambda x:[-x[0],x[1]])
    return [i[1] for i in lst3]
if __name__=="__main__":
    #print(cal_weight('aBCA;b,56ES'))#python考试第二题
    #print(find_representable_nums([8,9], [1,2,3]))
    #print(find_majority_elements([56, 56, 2, 1, 2, 3, 2, 3, 4, 56]))#python考试第四题
    #print(is_abnormal_sample([2, 2, 5, 5, 5, 5, 5, 5, 6, 7], 3, 4))#python考试第五题
    #print(is_abnormal_sample([2, 2, 5, 5, 5, 5, 5, 5, 6, 7], 3, 777))#python考试第五题
    #print(sort_students([70, 85, 70], ['2201', '2202', '2203']))#python考试第六题
    #print(find_words_on_same_line(["quote"]))  #python考试第七题
    #print(can_be_expressed([11, 6, 5, 4, 8], [1,2,3]))#python考试第三题
    #print(func6([70, 85, 70], ["2201", "2202", "2203"]))