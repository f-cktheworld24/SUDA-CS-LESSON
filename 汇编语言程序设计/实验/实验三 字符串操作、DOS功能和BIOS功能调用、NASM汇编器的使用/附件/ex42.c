/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char str1[256], str2[256];
    int position = -1;
    int len1, len2;

    printf("请输入主字符串 str1: ");
    scanf("%s", str1);
    printf("请输入子字符串 str2: ");
    scanf("%s", str2);

    len1 = strlen(str1);
    len2 = strlen(str2);

    _asm {
        CLD                     // 方向标志：正向
        MOV ECX, len2          // ECX = str2 长度
        JECXZ NOT_FOUND         // 如果 str2 为空，直接返回 -1

        LEA ESI, str2           // ESI = str2 地址
        LEA EDI, str1           // EDI = str1 地址
        MOV EBX, len1           // EBX = str1 长度
        SUB EBX, ECX            // EBX = 最大可能起始位置
        JC NOT_FOUND            // 如果 str2 比 str1 长，返回 -1

        MOV AL, [ESI]           // AL = str2 的第一个字符
        INC ESI                 // 指向 str2 的第二个字符
        DEC ECX                 // ECX = 剩余要比较的字符数

    SEARCH_LOOP:
        REPNE SCASB             // 在 str1 中搜索 AL
        JNE NOT_FOUND           // 如果找不到，跳转
        CMP EBX, 0              // 检查是否还有足够长度
        JL NOT_FOUND            // 如果剩余长度不足，返回 -1

        PUSH EDI                // 保存当前 EDI
        PUSH ESI               // 保存 ESI
        PUSH ECX               // 保存 ECX
        MOV ECX, len2           // ECX = str2 长度
        DEC ECX                 // 已经比较了第一个字符
        REPE CMPSB             // 比较剩余字符
        POP ECX                // 恢复 ECX
        POP ESI                // 恢复 ESI
        POP EDI                // 恢复 EDI
        JE FOUND               // 如果全部匹配，跳转 FOUND

        DEC EBX                // 减少剩余搜索长度
        JMP SEARCH_LOOP        // 继续搜索

    FOUND:
        LEA EAX, str1           // 获取 str1 的起始地址
        SUB EDI, EAX            // 计算偏移量
        DEC EDI                 // 调整位置
        MOV position, EDI       // 存储位置
        JMP DONE

    NOT_FOUND:
        MOV position, -1        // 未找到，返回 -1

    DONE:
    }

    printf("子串起始位置: %d\n", position);
    system("pause");
    return 0;
}
*/