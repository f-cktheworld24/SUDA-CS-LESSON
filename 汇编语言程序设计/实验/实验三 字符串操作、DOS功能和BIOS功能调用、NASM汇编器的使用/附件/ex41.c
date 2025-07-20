/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
    char str1[256], str2[256], result[512];

    printf("请输入第一个字符串: ");
    scanf("%s", str1);
    printf("请输入第二个字符串: ");
    scanf("%s", str2);

    _asm {
        // 复制 str1 到 result
        LEA ESI, str1     // ESI = str1 地址
        LEA EDI, result    // EDI = result 地址
        MOV ECX, 0         // ECX = 0
    COPY_STR1:
        MOV AL, [ESI]      // 加载字符
        TEST AL, AL        // 检查是否为 '\0'
        JZ COPY_STR2       // 如果是，跳转到复制 str2
        MOV [EDI], AL      // 存储字符到 result
        INC ESI            // 移动到下一个字符
        INC EDI            // 移动到下一个存储位置
        JMP COPY_STR1      // 继续复制

    COPY_STR2:
        // 复制 str2 到 result（接在 str1 之后）
        LEA ESI, str2      // ESI = str2 地址
    COPY_STR2_LOOP:
        MOV AL, [ESI]      // 加载字符
        TEST AL, AL        // 检查是否为 '\0'
        JZ DONE            // 如果是，结束
        MOV [EDI], AL      // 存储字符到 result
        INC ESI            // 移动到下一个字符
        INC EDI            // 移动到下一个存储位置
        JMP COPY_STR2_LOOP // 继续复制

    DONE:
        MOV BYTE PTR [EDI], 0 // 添加字符串结束符
    }

    printf("合并后的字符串: %s\n", result);
	system("pause");
    return 0;
}
*/