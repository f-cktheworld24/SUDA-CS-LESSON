/* globalBuiltin.c*/
#include <stdio.h>
int main()
{
int val=0x12345678;

 __asm__ __volatile__(
    "mov x3,%1\n"
	"mov w3,w3, ror #8\n"
	"bic w3,w3, #0x00ff00ff\n"

	"mov x4,%1\n"
	"mov w4,w4, ror #24\n"
	"bic w4,w4, #0xff00ff00\n"

	"add w3,w4,w3\n"
	"mov %0,x3\n"

	:"=r"(val)
	:"0"(val)
	:"w3","w4","cc"
	);

printf("out is %x \n",val);
return 0;
}
