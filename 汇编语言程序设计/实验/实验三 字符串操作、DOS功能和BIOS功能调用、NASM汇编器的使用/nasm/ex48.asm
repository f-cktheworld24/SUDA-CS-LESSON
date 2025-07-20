org 0x100

start:
    mov dx, msg_instructions
    mov ah, 0x09
    int 0x21

key_loop:
    ; 等待按键
    mov ah, 0x00
    int 0x16

    ; 显示 ASCII 码
    mov dx, msg_ascii
    mov ah, 0x09
    int 0x21
    movzx ax, al
    call print_number

    ; 显示扫描码
    mov dx, msg_scancode
    mov ah, 0x09
    int 0x21
    movzx ax, ah
    call print_number

    ; 检查是否按 ESC 键
    cmp al, 27
    jne key_loop

    ; 退出
    mov ah, 0x4C
    int 0x21

; 打印 AX 中的十进制数（同程序 2）
print_number:
    mov bx, 10
    mov cx, 0
push_digits:
    xor dx, dx
    div bx
    add dl, '0'
    push dx
    inc cx
    test ax, ax
    jnz push_digits
print_digits:
    pop dx
    mov ah, 0x02
    int 0x21
    loop print_digits
    mov dl, 0x0D
    int 0x21
    mov dl, 0x0A
    int 0x21
    ret

; 数据段
msg_instructions db 'Press any key (ESC to exit):', 0x0D, 0x0A, '$'
msg_ascii db 'ASCII: $'
msg_scancode db 'Scan code: $'