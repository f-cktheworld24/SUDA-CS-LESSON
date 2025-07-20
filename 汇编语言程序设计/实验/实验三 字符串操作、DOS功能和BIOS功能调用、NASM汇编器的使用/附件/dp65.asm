  section code
..start:
  MOV AX, data
  MOV DS, AX
  MOV DX, hello
  CALL Print_str
  MOV AH, 40H
  INT 21H
over:
  ;--------------
  section data
hello db "Hello,world" , 0DH, 0AH, 24H
  ;--------------
  section code
Print_str:
  MOV AH, 9
  INT 21H
  RET