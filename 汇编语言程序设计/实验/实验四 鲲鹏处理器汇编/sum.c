#include <stdio.h>

int main() {
    int n = 0;
    int sum = 0;
    
    scanf("%d", &n);
    printf("n=%d\n", n);
    
    // 下面是嵌入汇编部分
    __asm__ __volatile__(
        "mov x3, #0\n"          // x3 = 0 (sum初始值)
        "mov x4, #1\n"          // x4 = 1 (计数器i)
        
        "loop:\n"
        "add x3, x3, x4\n"      // sum += i
        "add x4, x4, #1\n"      // i++
        "cmp x4, %[n]\n"        // 比较i和n
        "ble loop\n"            // 如果i <= n，继续循环
        
        "mov %[sum], x3\n"      // 将结果存入sum变量
        : [sum] "=r" (sum)      // 输出
        : [n] "r" (n)           // 输入
        : "x3", "x4", "cc"      // 破坏的寄存器
    );
    
    printf("sum is %d \n", sum);
    return 0;
}