/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char str1[256], str2[256];
    int position = -1;
    int len1, len2;

    printf("���������ַ��� str1: ");
    scanf("%s", str1);
    printf("���������ַ��� str2: ");
    scanf("%s", str2);

    len1 = strlen(str1);
    len2 = strlen(str2);

    _asm {
        CLD                     // �����־������
        MOV ECX, len2          // ECX = str2 ����
        JECXZ NOT_FOUND         // ��� str2 Ϊ�գ�ֱ�ӷ��� -1

        LEA ESI, str2           // ESI = str2 ��ַ
        LEA EDI, str1           // EDI = str1 ��ַ
        MOV EBX, len1           // EBX = str1 ����
        SUB EBX, ECX            // EBX = ��������ʼλ��
        JC NOT_FOUND            // ��� str2 �� str1 �������� -1

        MOV AL, [ESI]           // AL = str2 �ĵ�һ���ַ�
        INC ESI                 // ָ�� str2 �ĵڶ����ַ�
        DEC ECX                 // ECX = ʣ��Ҫ�Ƚϵ��ַ���

    SEARCH_LOOP:
        REPNE SCASB             // �� str1 ������ AL
        JNE NOT_FOUND           // ����Ҳ�������ת
        CMP EBX, 0              // ����Ƿ����㹻����
        JL NOT_FOUND            // ���ʣ�೤�Ȳ��㣬���� -1

        PUSH EDI                // ���浱ǰ EDI
        PUSH ESI               // ���� ESI
        PUSH ECX               // ���� ECX
        MOV ECX, len2           // ECX = str2 ����
        DEC ECX                 // �Ѿ��Ƚ��˵�һ���ַ�
        REPE CMPSB             // �Ƚ�ʣ���ַ�
        POP ECX                // �ָ� ECX
        POP ESI                // �ָ� ESI
        POP EDI                // �ָ� EDI
        JE FOUND               // ���ȫ��ƥ�䣬��ת FOUND

        DEC EBX                // ����ʣ����������
        JMP SEARCH_LOOP        // ��������

    FOUND:
        LEA EAX, str1           // ��ȡ str1 ����ʼ��ַ
        SUB EDI, EAX            // ����ƫ����
        DEC EDI                 // ����λ��
        MOV position, EDI       // �洢λ��
        JMP DONE

    NOT_FOUND:
        MOV position, -1        // δ�ҵ������� -1

    DONE:
    }

    printf("�Ӵ���ʼλ��: %d\n", position);
    system("pause");
    return 0;
}
*/