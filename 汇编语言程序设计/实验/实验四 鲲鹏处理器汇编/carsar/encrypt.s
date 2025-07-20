.text
.global encryptChar
.global encryptString

encryptChar:
    // 输入: w0 = 字符c
    // 输出: w0 = 加密后的字符
    
    // 检查是否是小写字母
    cmp w0, 'a'
    b.lt done
    cmp w0, 'z'
    b.gt done
    
    // 转换为大写
    sub w0, w0, #32
    
    // 向后移动3位
    add w0, w0, #3
    
    // 处理溢出
    cmp w0, 'Z'
    b.le done
    sub w0, w0, #26
    
done:
    ret

encryptString:
    // 输入: x0 = 字符串指针
    
    // 保存调用者保存的寄存器
    stp x29, x30, [sp, #-16]!
    mov x29, sp
    
    // 保存原始指针
    mov x1, x0
    
    // 计算字符串长度
    bl strlen
    mov x2, x0          // x2 = 字符串长度
    mov x3, x1          // x3 = 字符串指针
    
    // 检查空字符串
    cbz x2, end
    
loop:
    // 加载字符
    ldrb w0, [x3]
    
    // 加密字符
    bl encryptChar
    
    // 存储加密后的字符
    strb w0, [x3], #1
    
    // 递减计数器并检查是否结束
    subs x2, x2, #1
    b.ne loop
    
end:
    // 恢复调用者保存的寄存器并返回
    ldp x29, x30, [sp], #16
    ret