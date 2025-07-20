org 0x100      ; COM 程序起始地址 0x100

start:
    mov cx, 6   ; 循环 6 次
print_lines:
    push cx     ; 保存循环计数器
    mov ah, 0x02 ; 设置 DOS 功能号：显示字符
    mov dl, 'A'  ; 从 'A' 开始
print_letters:
    int 0x21    ; 调用 DOS 中断
    inc dl      ; 下一个字母
    cmp dl, 'Z' ; 是否到达 'Z'？
    jle print_letters ; 未到则继续
    mov dl, 0x0D ; 回车
    int 0x21
    mov dl, 0x0A ; 换行
    int 0x21
    pop cx      ; 恢复循环计数器
    loop print_lines ; 继续下一行
    mov ah, 0x4C ; 退出程序
    int 0x21