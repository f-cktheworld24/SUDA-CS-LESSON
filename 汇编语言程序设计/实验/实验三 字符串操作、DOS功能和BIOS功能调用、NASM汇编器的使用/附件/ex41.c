/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
    char str1[256], str2[256], result[512];

    printf("�������һ���ַ���: ");
    scanf("%s", str1);
    printf("������ڶ����ַ���: ");
    scanf("%s", str2);

    _asm {
        // ���� str1 �� result
        LEA ESI, str1     // ESI = str1 ��ַ
        LEA EDI, result    // EDI = result ��ַ
        MOV ECX, 0         // ECX = 0
    COPY_STR1:
        MOV AL, [ESI]      // �����ַ�
        TEST AL, AL        // ����Ƿ�Ϊ '\0'
        JZ COPY_STR2       // ����ǣ���ת������ str2
        MOV [EDI], AL      // �洢�ַ��� result
        INC ESI            // �ƶ�����һ���ַ�
        INC EDI            // �ƶ�����һ���洢λ��
        JMP COPY_STR1      // ��������

    COPY_STR2:
        // ���� str2 �� result������ str1 ֮��
        LEA ESI, str2      // ESI = str2 ��ַ
    COPY_STR2_LOOP:
        MOV AL, [ESI]      // �����ַ�
        TEST AL, AL        // ����Ƿ�Ϊ '\0'
        JZ DONE            // ����ǣ�����
        MOV [EDI], AL      // �洢�ַ��� result
        INC ESI            // �ƶ�����һ���ַ�
        INC EDI            // �ƶ�����һ���洢λ��
        JMP COPY_STR2_LOOP // ��������

    DONE:
        MOV BYTE PTR [EDI], 0 // ����ַ���������
    }

    printf("�ϲ�����ַ���: %s\n", result);
	system("pause");
    return 0;
}
*/