# Thanks to https://github.com/kmowery/mips-assembler/blob/master/instruction.py
import argparse

parser = argparse.ArgumentParser(description='Build MIPS source files for fuzz testing')
parser.add_argument('-n','--num-lines', help='number of lines to output', required=True)
parser.add_argument('-o','--output-file', help='output file', required=True)

args = vars(parser.parse_args())


instruction_formats = {
        'addu': '$rd, $rs, $rt',
        'or': '$rd, $rs, $rt',
        'xor': '$rd, $rs, $rt',
        'slt': '$rd, $rs, $rt',
        'sltu': '$rd, $rs, $rt',
        'jr': '$rs',
        'sll': '$rd, $rt, imm',
        'addiu': '$rt, $rs, imm',
        'ori': '$rt, $rs, imm',
        'xori': '$rt, $rs, imm',
        'lui': '$rt, imm',
        'lb': '$rt, imm($rs)',
        'lbu': '$rt, imm($rs)',
        'lw': '$rt, imm($rs)',
        'sb': '$rt, imm($rs)',
        'sw': '$rt, imm($rs)',
        'beq': '$rs, $rt, label',
        'bne': '$rs, $rt, label',
        'j':'label',
        'jal':'label',
        'mult':'$rs, $rt',
        'div': '$rs, $rt',
        'mfhi': '$rd',
        'mflo': '$rd',
        'li': '$rt, imm',
        'neg': '$rt, $rs',
        'mfhilo': '$rs, $rt',
        'pi': '$rs, $rt, $rd'
}
class Instruction(object):
    def __init__(self, position, name, rd=None, rs=None, rt=None, imm=None, label=None, jump_label=None):
        self.position = position
        self.name = name
        self.registers = registers
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
        if self.rd:
            args_template.replace('$rd', self.rd)
        if self.rs:
            args_template.replace('$rs', self.rs)
        if self.rt:
            args_template.replace('$rt', self.rt)
        if self.imm:
            args_template.replace('$imm', self.imm)
        if self.jump_label:
            args_template.replace('label',self.jump_label)
        val += args_template
        return val

