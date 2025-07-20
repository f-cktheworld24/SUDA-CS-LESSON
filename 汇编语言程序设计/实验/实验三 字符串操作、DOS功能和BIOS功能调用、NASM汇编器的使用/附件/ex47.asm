org 0x100

start:
    ; 输入第一个数
    call input_number
    mov [num1], ax

    ; 输入第二个数
    call input_number
    mov [num2], ax

    ; 计算和
    mov ax, [num1]
    add ax, [num2]
    mov [sum], ax

    ; 计算差 (num1 - num2)
    mov ax, [num1]
    sub ax, [num2]
    mov [diff], ax

    ; 输出和
    mov dx, msg_sum
    mov ah, 0x09
    int 0x21
    mov ax, [sum]
    call print_number

    ; 输出差
    mov dx, msg_diff
    mov ah, 0x09
    int 0x21
    mov ax, [diff]
    call print_number

    ; 退出
    mov ah, 0x4C
    int 0x21

; 输入十进制数（结果保存在 AX）
input_number:
    mov dx, msg_prompt
    mov ah, 0x09
    int 0x21
    mov bx, 0    ; 初始化结果
input_loop:
    mov ah, 0x01 ; 读取字符
    int 0x21
    cmp al, 0x0D ; 回车结束
    je input_done
    sub al, '0'  ; ASCII 转数字
    mov cl, al
    mov ax, bx
    mov dx, 10
    mul dx       ; BX *= 10
    add ax, cx   ; BX += 新数字
    mov bx, ax
    jmp input_loop
input_done:
    mov ax, bx
    ret

; 打印 AX 中的十进制数
print_number:
    mov bx, 10
    mov cx, 0
push_digits:
    xor dx, dx
    div bx       ; AX /= 10, DX = 余数
    add dl, '0'  ; 转为 ASCII
    push dx
    inc cx
    test ax, ax
    jnz push_digits
print_digits:
    pop dx
    mov ah, 0x02
    int 0x21
    loop print_digits
    mov dl, 0x0D ; 回车
    int 0x21
    mov dl, 0x0A ; 换行
    int 0x21
    ret

; 数据段
msg_prompt db 'Enter a number (0-65535): $'
msg_sum db 0x0D, 0x0A, 'Sum: $'
msg_diff db 0x0D, 0x0A, 'Difference: $'
num1 dw 0
num2 dw 0
sum dw 0
diff dw 0