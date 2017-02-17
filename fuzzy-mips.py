# Thanks to https://github.com/kmowery/mips-assembler/blob/master/instruction.py
import argparse

parser = argparse.ArgumentParser(description='Build MIPS source files for fuzz testing')
parser.add_argument('-n','--num-lines', help='number of lines to output', required=True)
parser.add_argument('-o','--output-file', help='output file', required=True)

args = vars(parser.parse_args())


r_type = {'sll': ['rd', 'rt'], 'jalr': ['rd', 'rs'], 'srav': ['rd', 'rt'], 'mthi': ['rs'], 'syscall': [], 'nor': ['rd', 'rs', 'rt'], 'slt': ['rd', 'rs', 'rt'], 'mflo': ['rd'], 'and': ['rd', 'rs', 'rt'], 'sltu': ['rd', 'rs', 'rt'], 'xor': ['rd', 'rs', 'rt'], 'srlv': ['rd', 'rt', 'rs'], 'or': ['rd', 'rs', 'rt'], 'break': [], 'divu': ['rs', 'rt'], 'sllv': ['rd', 'rt'], 'addu': ['rd', 'rs', 'rt'], 'subu': ['rd', 'rs', 'rt'], 'div': ['rd', 'rs', 'rt'], 'mult': ['rs', 'rt'], 'srl': ['rd', 'rt'], 'add': ['rd', 'rs', 'rt'], 'jr': ['rs'], 'mfhi': ['rd'], 'multu': ['rs', 'rt'], 'mtlo': ['rs'], 'sra': ['rd', 'rt'], 'sub': ['rd', 'rs', 'rt']}

i_type = {'bltz': ['rs'], 'blez': ['rs'], 'bne': ['rs', 'rt'], 'xori': ['rt', 'rs'], 'sw': ['rt', 'rs'], 'lw': ['rt', 'rs'], 'sb': ['rt', 'rs'], 'swc1': ['rt', 'rs'], 'bgtz': ['rs'], 'lhu': ['rt', 'rs'], 'addiu': ['rt', 'rs'], 'lb': ['rt', 'rs'], 'lwc1': ['rt', 'rs'], 'andi': ['rt', 'rs'], 'sh': ['rt', 'rs'], 'lbu': ['rt', 'rs'], 'beq': ['rs', 'rt'], 'sc': ['rt', 'rs'], 'slti': ['rt', 'rs'], 'addi': ['rt', 'rs'], 'sltiu': ['rt', 'rs'], 'lui': ['rt'], 'ori': ['rt', 'rs'], 'lh': ['rt', 'rs'], 'bgez': ['rs']} 

j_type = {'j':[],'jal':[]}

pseudo_type = {'li':['rt'],'neg':['rt','rs'],'mfhilo':['rs','rt'],'pi':['rs','rt','rd']}

all_type = {}

all_type.update(r_type)
all_type.update(i_type)
all_type.update(j_type)
all_type.update(pseudo_type)
class Instruction(object):
    def __init__(self, position, name, rd, rs, rt, imm, label):
        self.position = position
        self.name = name
        self.registers = registers
        self.imm = imm
        self.label = label
        self.rd = rd
        self.rs = rs
        self.rt = rt
    def __str__(self):
        val = ""
        if self.label:
            val += label + ": "
        for 
