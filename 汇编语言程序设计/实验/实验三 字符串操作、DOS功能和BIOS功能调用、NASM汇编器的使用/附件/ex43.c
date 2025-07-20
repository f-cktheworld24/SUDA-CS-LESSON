/*
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
int main() {
    char input[256], output[256];

    printf("请输入一个字符串: ");
    scanf("%s", input);

    _asm {
        CLD                     // 方向标志：正向
        LEA ESI, input          // ESI = 输入字符串地址
        LEA EDI, output         // EDI = 输出字符串地址

    FILTER_LOOP:
        LODSB                   // AL = [ESI++]
        TEST AL, AL             // 检查是否到字符串末尾
        JZ DONE                 // 如果是，结束

        // 检查是否为字母（A-Z, a-z）
        CMP AL, 'A'
        JB SKIP                 // 如果 AL < 'A'，跳过
        CMP AL, 'Z'
        JBE STORE              // 如果 AL <= 'Z'，存储
        CMP AL, 'a'
        JB SKIP                 // 如果 AL < 'a'，跳过
        CMP AL, 'z'
        JA SKIP                 // 如果 AL > 'z'，跳过

    STORE:
        STOSB                   // [EDI++] = AL
        JMP FILTER_LOOP

    SKIP:
        JMP FILTER_LOOP         // 继续过滤

    DONE:
        MOV BYTE PTR [EDI], 0   // 添加字符串结束符
    }

    printf("过滤后的字符串: %s\n", output);
	system("pause");
    return 0;
}
*/