def decompose_list(num, length, start, end):
    if num == 1 or start > end or end < 1 or start > length:
        if start <= 1 <= end:
            return num
        else:
            return 0

    middle = length // 2 + (length % 2)

    left = decompose_list(num // 2, middle - 1, start, min(end, middle - 1))

    if start <= middle <= end:
        mid = (num % 2)
    else:
        mid = 0

    right = decompose_list(num // 2, length - middle, max(1, start - middle), end - middle)

    return left + mid + right


num, start, end = [int(num) for num in input().split(" ")]

length = 1
temp = num
while temp > 1:
    length = length * 2 + 1
    temp //= 2
print(decompose_list(num, length, start, end))
