def find_ones(n, l, r):
    def count_ones(num, length, l, r):
        if num == 1 or l > r or r < 1 or l > length:
            return num if l <= 1 <= r else 0

        mid = length // 2 + (length % 2)

        # Calculate ones in the left part
        left_ones = count_ones(num // 2, mid - 1, l, min(r, mid - 1))
        print(num // 2, mid - 1, l, min(r, mid - 1))

        # Calculate ones in the middle (the remainder)
        middle_ones = (num % 2) if l <= mid <= r else 0
        print(middle_ones)

        # Calculate ones in the right part
        right_ones = count_ones(num // 2, length - mid, max(1, l - mid), r - mid)
        print(num // 2, length - mid, max(1, l - mid), r - mid)

        print(left_ones,middle_ones,right_ones)
        return left_ones + middle_ones + right_ones

    length = 1
    temp = n
    while temp > 1:
        length = length * 2 + 1
        temp //= 2
        #print(length,temp)

    return count_ones(n, length, l, r)


# 输入
n, l, r = map(int, input().split())

# 输出
result = find_ones(n, l, r)
print(result)

