from lib.objects import Context
from typing import Callable


class Opcode:
    def __init__(self,opcode:str,label:str,action: Callable[[Context], None]):
        self.opcode = opcode
        self.label = label
        self.action = action
    
    def execute(self,ctx):
        self.action(ctx)




def get_opcode(op):
    match op:
        case 0x00:
            return Opcode(0x00,"STOP",earlyTermination)
        case 0x60:
            return Opcode(0x60,"PUSH1",PUSH1)
        case 0x61:
            return Opcode(0x61,"PUSH2",PUSH2)
        case _:
            print("Opcode implementation not found for ", hex(op))
            # Returns true so that we can find the appropriate test case and error message
            return Opcode(0x00,"STOP",earlyTermination)

            

def earlyTermination(ctx):
    return (True,[])

def PUSH1(ctx):
    ctx.pc +=1
    ctx.stack.push(ctx.code[ctx.pc])

def PUSH2(ctx):
    print(ctx.code)
    ctx.pc +=1
    ctx.stack.push(ctx.code[ctx.pc:ctx.pc+2])

    




