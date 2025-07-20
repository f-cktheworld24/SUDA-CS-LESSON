/*
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
int main() {
    char input[256], output[256];

    printf("������һ���ַ���: ");
    scanf("%s", input);

    _asm {
        CLD                     // �����־������
        LEA ESI, input          // ESI = �����ַ�����ַ
        LEA EDI, output         // EDI = ����ַ�����ַ

    FILTER_LOOP:
        LODSB                   // AL = [ESI++]
        TEST AL, AL             // ����Ƿ��ַ���ĩβ
        JZ DONE                 // ����ǣ�����

        // ����Ƿ�Ϊ��ĸ��A-Z, a-z��
        CMP AL, 'A'
        JB SKIP                 // ��� AL < 'A'������
        CMP AL, 'Z'
        JBE STORE              // ��� AL <= 'Z'���洢
        CMP AL, 'a'
        JB SKIP                 // ��� AL < 'a'������
        CMP AL, 'z'
        JA SKIP                 // ��� AL > 'z'������

    STORE:
        STOSB                   // [EDI++] = AL
        JMP FILTER_LOOP

    SKIP:
        JMP FILTER_LOOP         // ��������

    DONE:
        MOV BYTE PTR [EDI], 0   // ����ַ���������
    }

    printf("���˺���ַ���: %s\n", output);
	system("pause");
    return 0;
}
*/