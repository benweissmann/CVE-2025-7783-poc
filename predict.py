#!/usr/bin/python3

# Based on https://github.com/PwnFunction/v8-randomness-predictor/blob/main/main.py
# and https://hackerone.com/reports/2913312

import z3
import struct
import sys
import json

sequence = json.loads(sys.argv[1])

sequence = sequence[::-1]

solver = z3.Solver()

se_state0, se_state1 = z3.BitVecs("se_state0 se_state1", 64)

for i in range(len(sequence)):
    se_s1 = se_state0
    se_s0 = se_state1
    se_state0 = se_s0
    se_s1 ^= se_s1 << 23
    se_s1 ^= z3.LShR(se_s1, 17)  # Logical shift instead of Arthmetric shift
    se_s1 ^= se_s0
    se_s1 ^= z3.LShR(se_s0, 26)
    se_state1 = se_s1
    solver.add(
        int(sequence[i]) == ((z3.ZeroExt(64, z3.LShR(se_state0, 12)) * 1e11) >> 52)
    )


if solver.check() == z3.sat:
    model = solver.model()

    states = {}
    for state in model.decls():
        states[state.__str__()] = model[state]

    state0 = states["se_state0"].as_long()

    u_long_long_64 = (state0 >> 12) | 0x3FF0000000000000
    float_64 = struct.pack("<Q", u_long_long_64)
    next_sequence = struct.unpack("d", float_64)[0]
    next_sequence -= 1

    print(int(next_sequence * 1e11))
