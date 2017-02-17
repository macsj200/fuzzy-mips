lbu $s3, -61($sp)
mflo $a3
beq $zero, $v0, test
lw $0, 23($s3)
addu $t3, $sp, $a1
mflo $s3
jr $a3
addiu $sp, $a1, -79
xori $a1, $t2, 72
li $a1, 14
