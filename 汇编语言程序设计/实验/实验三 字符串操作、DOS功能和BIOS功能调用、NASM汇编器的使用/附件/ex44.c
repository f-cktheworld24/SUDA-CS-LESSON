/*
#include <stdio.h>
#include <stdlib.h>  // ����exit����

void generateString(char ch1, int n, char *str1) {
	_asm {
		MOV AL, ch1     // Ҫ�����ַ�
        MOV ECX, n      // ����ѭ������
        MOV EDI, str1    // Ŀ���ַ,char *str1 ��Ϊָ��������ڻ����ֱ��ʹ�� LEA EDI, str1 ���ȡָ�뱾��ĵ�ַ����������ָ��Ļ�������ַ

    FILL_LOOP:
        MOV [EDI], AL           // �洢�ַ����ڴ�
        INC EDI                 // �ƶ�����һ��λ��
        DEC ECX                 // ECX--
        JNZ FILL_LOOP           // ���ECX!=0�����ѭ��
        
    OVER:
        MOV BYTE PTR [EDI], 0   // ����ַ�����ֹ��
    }
}

int main()
{
    char ch1;
    int n;
    char str1[256] = {0};  // ��ʼ��Ϊȫ0

    printf("������һ���ַ�:");
    if (scanf_s(" %c", &ch1, 1) != 1) {  // ��ȫ���
        printf("�������\n");
        exit(1);
    }

    printf("������һ����ֵn:");
    if (scanf_s("%d", &n) != 1 || n < 0) {  // ���Ǹ�����
        printf("��������ǷǸ�������\n");
        exit(1);
    }

    if (n >= 255) {  // �߽���
        printf("������ֵ������������С��\n");
        exit(1);
    }
	generateString(ch1, n, str1);
    printf("���ɵ��ַ���: %s\n", str1);
	system("pause");
    return 0;
}
*/