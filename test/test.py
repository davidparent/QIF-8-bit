# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


 
@cocotb.test()
async def test_QIFNeuron(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())

    # reset the circuit
    dut.rst_n.value = 0
    # wait for 5 clock cycles
    await ClockCycles(dut.clk, 5)
    # take the design out of reset
    dut.rst_n.value = 1
   
    dut.ui_in.value = 4
    await ClockCycles(dut.clk, 50)
