import cocotb
from cocotb.triggers import Timer
#import random

@cocotb.test()
async def MUX_Convert_DFF(dut):
    """Test for Passing data"""

    X = 2
    
    A = 5
    
    B = 1


    # input driving
    dut.D1.value = A
    
    dut.S.value = B
    
    dut.Y.value = X
    
    await Timer(2, units='ns'
    
    if (B == 1):
        
        assert dut.Y.value = A
    else
    
        assert dut.Y.value = X