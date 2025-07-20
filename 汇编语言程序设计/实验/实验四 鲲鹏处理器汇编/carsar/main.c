#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern void encryptString(char *str);

int main() {
    char str[100];
    
    printf("Enter a string: ");
    if (fgets(str, sizeof(str), stdin) == NULL) {
        perror("Error reading input");
        return 1;
    }
    
    str[strcspn(str, "\n")] = '\0';
    
    encryptString(str);
    printf("Encrypted string: %s\n", str);
    
    return 0;
}