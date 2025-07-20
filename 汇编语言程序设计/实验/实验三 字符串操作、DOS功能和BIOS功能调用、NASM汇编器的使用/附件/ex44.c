/*
#include <stdio.h>
#include <stdlib.h>  // 用于exit函数

void generateString(char ch1, int n, char *str1) {
	_asm {
		MOV AL, ch1     // 要填充的字符
        MOV ECX, n      // 设置循环次数
        MOV EDI, str1    // 目标地址,char *str1 作为指针参数，在汇编中直接使用 LEA EDI, str1 会获取指针本身的地址，而不是它指向的缓冲区地址

    FILL_LOOP:
        MOV [EDI], AL           // 存储字符到内存
        INC EDI                 // 移动到下一个位置
        DEC ECX                 // ECX--
        JNZ FILL_LOOP           // 如果ECX!=0则继续循环
        
    OVER:
        MOV BYTE PTR [EDI], 0   // 添加字符串终止符
    }
}

int main()
{
    char ch1;
    int n;
    char str1[256] = {0};  // 初始化为全0

    printf("请输入一个字符:");
    if (scanf_s(" %c", &ch1, 1) != 1) {  // 安全检查
        printf("输入错误！\n");
        exit(1);
    }

    printf("请输入一个数值n:");
    if (scanf_s("%d", &n) != 1 || n < 0) {  // 检查非负整数
        printf("输入必须是非负整数！\n");
        exit(1);
    }

    if (n >= 255) {  // 边界检查
        printf("错误：数值超过缓冲区大小！\n");
        exit(1);
    }
	generateString(ch1, n, str1);
    printf("生成的字符串: %s\n", str1);
	system("pause");
    return 0;
}
*/