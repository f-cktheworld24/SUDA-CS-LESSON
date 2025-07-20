gcc -c main.c
as -o encrypt.o encrypt.s
gcc -o caesar main.o encrypt.o
./caesar