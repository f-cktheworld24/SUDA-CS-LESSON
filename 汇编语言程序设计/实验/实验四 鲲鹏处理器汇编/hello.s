.text
.global _start  

_start:
    /* write(1, msg, len) */
    mov x0, #1      /* 文件描述符 1 = stdout */
    ldr x1, =msg    /* 字符串地址 */
    ldr x2, =len    /* 字符串长度 */
    mov x8, #64     /* 系统调用号 64 = write (AArch64) */
    svc #0          /* 调用内核 */

    /* exit(123) */
    mov x0, #123    /* 退出状态码 */
    mov x8, #93     /* 系统调用号 93 = exit (AArch64) */
    svc #0          /* 调用内核 */

.data
msg:
    .ascii "Hello World!\n"
len = . - msg       /* 计算字符串长度 */