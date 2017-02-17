# Thanks to https://github.com/kmowery/mips-assembler/blob/master/instruction.py
import argparse
import random
import string
parser = argparse.ArgumentParser(description='Build MIPS source files for fuzz testing')
parser.add_argument('-n','--num_lines', help='number of lines to output', required=True)
parser.add_argument('-o','--output_file', help='output file', required=True)
parser.add_argument('-v', '--valid_code', help='if true, produce valid code')

args = vars(parser.parse_args())

instruction_formats = {
        'addu': '{rd}, {rs}, {rt}',
        'or': '{rd}, {rs}, {rt}',
        'xor': '{rd}, {rs}, {rt}',
        'slt': '{rd}, {rs}, {rt}',
        'sltu': '{rd}, {rs}, {rt}',
        'jr': '{rs}',
        'sll': '{rd}, {rt}, {imm}',
        'addiu': '{rt}, {rs}, {imm}',
        'ori': '{rt}, {rs}, {imm}',
        'xori': '{rt}, {rs}, {imm}',
        'lui': '{rt}, {imm}',
        'lb': '{rt}, {imm}({rs})',
        'lbu': '{rt}, {imm}({rs})',
        'lw': '{rt}, {imm}({rs})',
        'sb': '{rt}, {imm}({rs})',
        'sw': '{rt}, {imm}({rs})',
        'beq': '{rs}, {rt}, {label}',
        'bne': '{rs}, {rt}, {label}',
        'j':'{label}',
        'jal':'{label}',
        'mult':'{rs}, {rt}',
        'div': '{rs}, {rt}',
        'mfhi': '{rd}',
        'mflo': '{rd}',
        'li': '{rt}, {imm}',
        'neg': '{rt}, {rs}',
        'mfhilo': '{rs}, {rt}',
        'pi': '{rs}, {rt}, {rd}'
}
# $zero, $at, $v0, $a0 - $a3, $t0 - $t3, $s0 - $s3, $sp, and $ra. The name $0
valid_registers = ['$zero', '$0', '$at', '$v0', '$a0', '$a1', '$a2', '$a3', '$t0', '$t1', '$t2', '$t3', '$s0', '$s1', '$s2', '$s3', '$sp', '$ra']
labels = []
class Instruction(object):
    def __init__(self, position, name, rd=None, rs=None, rt=None, imm=None, label=None, jump_label=None):
        self.position = position
        self.name = name
        self.imm = imm
        self.label = label
        self.jump_label = jump_label
        self.rd = rd
        self.rs = rs
        self.rt = rt
    def __str__(self):
        val = ""
        if self.label:
            val += label + ": "
        val += self.name
        args_template = instruction_formats[self.name]
        args_template = args_template.format(rd=self.rd, rs=self.rs, rt=self.rt, imm=self.imm, label=self.jump_label)
        val += " " + args_template
        return val

with open(args['output_file'], 'w') as output_file:
    for line in range(int(args['num_lines'])):
        instr_name = random.choice(list(instruction_formats.keys()))
        label = None
        if random.getrandbits(1) or len(labels) == 0:
            label = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
            labels.append(label)
        imm = 0
        if 'valid_code' in args.keys():
            if args['valid_code']:
                if instr_name == 'addiu' or instr_name == 'lb' or instr_name == 'lbu' or instr_name == 'lw' or instr_name == 'sb' or instr_name == 'sw':
                    imm = random.randint(-32768,32767)
                elif instr_name == 'ori' or instr_name == 'xori' or instr_name == 'lui':
                    imm = random.randint(0, 65535)
        ins = Instruction(line, instr_name, rd=random.choice(valid_registers), rs=random.choice(valid_registers), rt=random.choice(valid_registers), imm=imm, label=label, jump_label=random.choice(labels))
        output_file.write(str(ins)+'\n')
