import random
from schemdraw.parsing import logic_parser

gates = [
    "and",
    "or",
    "xor",
    "nand",
    "nor",
    "xnor"
]
random.shuffle(gates)


def rand_circuit(num_gates=3, first_order_gates=1, num_inputs=2):
    def rand_gate():
        global gates
        return gates[random.randint(0, len(gates) - 1)]

    def get_ascii(hx=0x41):
        return bytearray.fromhex(str(hx)).decode()

    inputs = []
    for i in range(num_inputs):
        inputs.append(get_ascii(41 + i))
    random.shuffle(inputs)

    gate_list = []
    for i in range(num_gates):
        gate = rand_gate()
        while gate in gate_list:
            gate = rand_gate()
        gate_list.append(gate)

    def inc_count(in_count):
        in_count += 1
        return in_count % len(inputs)

    def first_order(gate):
        if in_count == len(inputs) - 1:
            return f"{inputs[in_count]} {gate} {inputs[0]}"
        else:
            return f"{inputs[in_count]} {gate} {inputs[in_count + 1]}"

    def high_order(gate, nested):
        return f"{inputs[in_count]} {gate} ({nested})"

    in_count = 0
    if first_order_gates == 1:
        circuit = first_order(gate_list[0])
        in_count = inc_count(in_count)
        for lvl in range(1, num_gates):
            circuit = high_order(gate_list[lvl], circuit)
            in_count = inc_count(in_count)
    else:
        gate_1 = first_order(gate_list[0])
        in_count = inc_count(in_count)
        gate_2 = first_order(gate_list[1])
        in_count = inc_count(in_count)
        circuit = f"({gate_1}) {gate_list[2]} ({gate_2})"
        if num_gates == 4:
            sel_gate = random.randint(1, 2)
            if sel_gate == 1:
                circuit = f"({gate_1}) {gate_list[3]} ({circuit})"
            else:
                circuit = f"({gate_2}) {gate_list[3]} ({circuit})"
        if num_gates == 5:
            gate_3 = first_order(gate_list[4])
            circuit = f"({gate_3}) {gate_list[3]} ({circuit})"
    return circuit


def rand_int(bits=8):
    range_min = 2 ** (bits - 4)
    range_max = 2 ** bits
    return random.randint(range_min, range_max)


def rand_hex(bits=16, le=False):
    range_min = 2 ** (bits - 4)
    range_max = 2 ** bits
    value = random.randint(range_min, range_max)
    hex_string = hex(value)
    if le:
        hex_string = little_endian(hex_string)
    return value, hex_string


def flip_hamming(hc):
    rand_idx = random.randint(0, 10)
    hc[rand_idx] = 0 if hc[rand_idx] else 1
    return rand_idx + 1, hc


def calc_hamming(hc):
    hc[0] = (hc[0] + hc[2] + hc[4] + hc[6] + hc[8] + hc[10]) % 2
    hc[1] = (hc[1] + hc[2] + hc[5] + hc[6] + hc[9] + hc[10]) % 2
    hc[3] = (hc[3] + hc[4] + hc[5] + hc[6]) % 2
    hc[7] = (hc[7] + hc[8] + hc[9] + hc[10]) % 2
    return hc


def print_hamming(hc):
    return f"{hc[10]}{hc[9]}{hc[8]}{hc[7]}{hc[6]}{hc[5]}{hc[4]}{hc[3]}{hc[2]}{hc[1]}{hc[0]}"


def rand_hamming():
    bits = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        bits[i] = random.randint(0, 1)
    hamming = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hamming[2] = bits[0]
    hamming[4] = bits[1]
    hamming[5] = bits[2]
    hamming[6] = bits[3]
    hamming[8] = bits[4]
    hamming[9] = bits[5]
    hamming[10] = bits[6]
    return hamming


def little_endian(hex_string):
    le_string = "0x"
    index = len(hex_string)
    while index > 2:
        le_string += hex_string[index - 2:index]
        index -= 2
    return le_string

endianness_order = [
    True,
    False
]

random.shuffle(endianness_order)
ans1, problem1 = rand_hex(24, endianness_order[0])
order1 = "little endian" if endianness_order[0] else "big endian"
print(f"Solution to problem #1 is: {ans1}")

ans2, problem2 = rand_hex(24, endianness_order[1])
order2 = "little endian" if endianness_order[1] else "big endian"
print(f"Solution to problem #2 is: {ans2}")

random.shuffle(endianness_order)
problem3, ans3 = rand_hex(24, endianness_order[0])
order3 = "little endian" if endianness_order[0] else "big endian"
print(f"Solution to problem #3 is: {ans3}")

problem4, ans4 = rand_hex(24, endianness_order[1])
order4 = "little endian" if endianness_order[1] else "big endian"
print(f"Solution to problem #4 is: {ans4}")

problem5 = rand_hamming()
ans5 = calc_hamming(problem5)
print(f"Solution to problem #5 is: {print_hamming(ans5)}")

problem6 = rand_hamming()
ans6 = calc_hamming(problem6)
print(f"Solution to problem #6 is: {print_hamming(ans6)}")

problem7 = rand_hamming()
problem7 = calc_hamming(problem7)
ans7, problem7 = flip_hamming(problem7)
print(f"Solution to problem #7 is: {ans7}")

problem8 = rand_hamming()
problem8 = calc_hamming(problem8)
ans8, problem8 = flip_hamming(problem8)
print(f"Solution to problem #8 is: {ans8}")

hardware_questions = [
    "Describe the role of the ALU within the CPU.  Give examples of six of the most basic operations handled by the ALU.",
    "What is the function of the northbridge and southbridge in computer architecture, and how do they differ in terms of the components they manage?",
    "Outline the steps involved in the FDE cycle.  Why is this cycle fundamental to the operation of a CPU?",
    "What is the purpose of the system clock in a computer\'s CPU, and how does it affect the timing and synchronization of operations within the processor?",
    "How does the fetch, decode, execute cycle differ from the other common usage of the word 'cycle' in computer science?",
    "How does a GPU differ from a CPU?  Describe a problem that you would expect to execute faster on a GPU, and explain why.",
    "Explain the difference between Cache memory and RAM.  Which component of the motherboard handles transferring data from one to the other?",
    "RAM DIMMs are commonly sold in pairs, and the RAM slots on a motherboard are commonly arranged in pairs denoted A1,B1,A2,B2 or similar.  Why?"
]

assembly_questions = [
    "What does the CPU's PC register store?  How do the x86 `call` and `ret` operations modify its value?",
    "Describe the implicit operation performed by the 'cmp' operation in x86.  List two of the flags set by this operation.",
    "What does the 'rsp' register store in x86 assembly?  How do the 'push' and 'pop' operations modify the register's value?",
    "Modern x64 assembly does not appear to utilize the 'rbp' register to index or limit access to the stack.  What are the implications of this?"
]

mobo_list = [
    'A',
    'B',
    'C',
    'D',
    'E'
]

hardware_problems = random.sample(hardware_questions, 4)
assembly_problems = random.sample(assembly_questions, 2)

short_answer = hardware_problems + assembly_problems
random.shuffle(short_answer)

latex_code = f'''
\\documentclass[12pt]{{article}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage[all]{{xy}}


\\usepackage{{amsmath,amsthm,amssymb,color,latexsym}}
\\usepackage{{geometry}}        
\\geometry{{letterpaper}}    
\\usepackage{{graphicx}}
\\usepackage{{multicol}}
\\usepackage{{svg}}
\\usepackage{{changepage}}

\\newtheorem{{problem}}{{}}%Problem}}

\\newenvironment{{solution}}[1][\\it{{Solution}}]{{\\textbf{{#1. }} }}{{$\\square$}}


\\begin{{document}}
\\noindent \\Large \\textbf{{COSC-3310}}  \\hfill \\textbf{{Final Exam}}  \\hfill \\textbf{{Dec. 12, 2023}}\\\\

\\vspace{{0cm}}

\\textbf{{Name:}}
\\hrulefill

\\hspace{{-10mm}}
\\begin{{tabular}}{{rcc}}
     \\textbf{{Instructions:}} & $\\bullet$ No notes & $\\bullet$ Calculators allowed \\\\
\\end{{tabular}}

\\vspace{{.5cm}}

\\begin{{problem}}
\\Large Find the decimal value of $\\mathtt{{{problem1}}}$ ({order1}).
\\end{{problem}}

\\vspace{{7cm}}

\\begin{{problem}}
\\Large Find the decimal value of $\\mathtt{{{problem2}}}$ ({order2}).
\\end{{problem}}

\\newpage

\\begin{{problem}}
\\Large Convert the decimal value $\\mathtt{{0d{problem3}}}$ to hexadecimal ({order3}).
\\end{{problem}}

\\vspace{{7cm}}

\\begin{{problem}}
\\Large Convert the decimal value $\\mathtt{{0d{problem4}}}$ to hexadecimal ({order4}).
\\end{{problem}}

\\vspace{{7cm}}

% Hamming codes
\\begin{{problem}}
\\Large Calculate the Hamming Code for this array:
\\newline
\\newline
\\vspace{{1cm}}
\\hspace{{1cm}}
\\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|}}
     \\hline
     ${problem5[10]}$ & ${problem5[9]}$ & ${problem5[8]}$ & \\hspace{{4mm}} & ${problem5[6]}$ & ${problem5[5]}$ & ${problem5[4]}$ & \\hspace{{4mm}} & ${problem5[2]}$ & \\hspace{{4mm}} & \\hspace{{4mm}} \\\\
     \\hline
\\end{{tabular}}
\\end{{problem}}

\\newpage

\\begin{{problem}}
\\Large Calculate the Hamming Code for this array:
\\newline
\\newline
\\vspace{{1cm}}
\\hspace{{1cm}}
\\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|}}
    \\hline
    ${problem6[10]}$ & ${problem6[9]}$ & ${problem6[8]}$ & \\hspace{{4mm}} & ${problem6[6]}$ & ${problem6[5]}$ & ${problem6[4]}$ & \\hspace{{4mm}} & ${problem6[2]}$ & \\hspace{{4mm}} & \\hspace{{4mm}} \\\\
    \\hline
\\end{{tabular}}
\\end{{problem}}

\\vspace{{4cm}}

\\begin{{problem}}
\\Large Identify the corrupted bit in this Hamming Code:
\\newline
\\newline
\\vspace{{1cm}}
\\hspace{{1cm}}
\\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|}}
     \\hline
     ${problem7[10]}$ & ${problem7[9]}$ & ${problem7[8]}$ & ${problem7[7]}$ & ${problem7[6]}$ & ${problem7[5]}$ & ${problem7[4]}$ & ${problem7[3]}$ & ${problem7[2]}$ & ${problem7[1]}$ & ${problem7[0]}$ \\\\
     \\hline
\\end{{tabular}}
\\end{{problem}}

\\vspace{{4cm}}

\\begin{{problem}}
\\Large Identify the corrupted bit in this Hamming Code:
\\newline
\\newline
\\vspace{{1cm}}
\\hspace{{1cm}}
\\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|}}
     \\hline
     ${problem8[10]}$ & ${problem8[9]}$ & ${problem8[8]}$ & ${problem8[7]}$ & ${problem8[6]}$ & ${problem8[5]}$ & ${problem8[4]}$ & ${problem8[3]}$ & ${problem8[2]}$ & ${problem8[1]}$ & ${problem8[0]}$ \\\\
     \\hline
\\end{{tabular}}
\\end{{problem}}

\\newpage

\\begin{{problem}}
\\Large Identify and fill in the truth tables for the logic gates.
\\end{{problem}}

\\vspace{{2mm}}

\\begin{{multicols}}{{2}}

\\normalsize
\\hspace{{1mm}}
\\includesvg[width=0.2\\textwidth]{{{gates[0]}.svg}}
\\vspace{{2mm}}

\\begin{{tabular}}{{c|c||c}}
     A & B & \\hspace{{2cm}} \\\\
     \\hline
     0 & 0 &  \\\\
     \\hline
     0 & 1 &  \\\\
     \\hline
     1 & 0 &  \\\\
     \\hline
     1 & 1 &  \\\\
\\end{{tabular}}

\\vspace{{12mm}}

\\hspace{{1mm}}
\\includesvg[width=0.2\\textwidth]{{{gates[1]}.svg}}
\\vspace{{2mm}}

\\begin{{tabular}}{{c|c||c}}
     A & B & \\hspace{{2cm}} \\\\
     \\hline
     0 & 0 &  \\\\
     \\hline
     0 & 1 &  \\\\
     \\hline
     1 & 0 &  \\\\
     \\hline
     1 & 1 &  \\\\
\\end{{tabular}}

\\vspace{{12mm}}

\\hspace{{1mm}}
\\includesvg[width=0.2\\textwidth]{{{gates[2]}.svg}}
\\vspace{{2mm}}

\\begin{{tabular}}{{c|c||c}}
     A & B & \\hspace{{2cm}} \\\\
     \\hline
     0 & 0 &  \\\\
     \\hline
     0 & 1 &  \\\\
     \\hline
     1 & 0 &  \\\\
     \\hline
     1 & 1 &  \\\\
\\end{{tabular}}

\\vspace{{12mm}}

\\hspace{{0mm}}
\\includesvg[width=0.2\\textwidth]{{not.svg}}
\\vspace{{2mm}}

\\begin{{tabular}}{{c||c}}
     A & \\hspace{{2cm}} \\\\
     \\hline
     0 &  \\\\
     \\hline
     1 &  \\\\
\\end{{tabular}}

\\vspace{{3cm}}

\\hspace{{1mm}}
\\includesvg[width=0.2\\textwidth]{{{gates[3]}.svg}}
\\vspace{{2mm}}

\\begin{{tabular}}{{c|c||c}}
     A & B & \\hspace{{2cm}} \\\\
     \\hline
     0 & 0 &  \\\\
     \\hline
     0 & 1 &  \\\\
     \\hline
     1 & 0 &  \\\\
     \\hline
     1 & 1 &  \\\\
\\end{{tabular}}

\\vspace{{12mm}}

\\hspace{{1mm}}
\\includesvg[width=0.2\\textwidth]{{{gates[4]}.svg}}
\\vspace{{2mm}}

\\begin{{tabular}}{{c|c||c}}
     A & B & \\hspace{{2cm}} \\\\
     \\hline
     0 & 0 &  \\\\
     \\hline
     0 & 1 &  \\\\
     \\hline
     1 & 0 &  \\\\
     \\hline
     1 & 1 &  \\\\
\\end{{tabular}}

\\vspace{{12mm}}

\\hspace{{1mm}}
\\includesvg[width=0.2\\textwidth]{{{gates[5]}.svg}}
\\vspace{{2mm}}

\\begin{{tabular}}{{c|c||c}}
     A & B & \\hspace{{2cm}} \\\\
     \\hline
     0 & 0 &  \\\\
     \\hline
     0 & 1 &  \\\\
     \\hline
     1 & 0 &  \\\\
     \\hline
     1 & 1 &  \\\\
\\end{{tabular}}

\\end{{multicols}}

\\newpage

\\begin{{problem}}
\\Large Complete the truth table for this circuit.

\\vspace{{1cm}}

\\includesvg[width=0.7\\textwidth]{{circuit_1.svg}}

\\vspace{{1cm}}

\\Large
\\begin{{tabular}}{{c|c||c||c||c}}
     & & (C) & (D) &  \\\\
    A & B & \\hspace{{3cm}} & \\hspace{{3cm}} & \\hspace{{3cm}} \\\\
    \\hline
    0 & 0 & & & \\\\
    \\hline
    0 & 1 & & & \\\\
    \\hline
    1 & 0 & & & \\\\
    \\hline
    1 & 1 & & & \\\\
\\end{{tabular}}

\\end{{problem}}

\\vspace{{1cm}}

\\begin{{problem}}
\\Large Diagram an "SR NAND Latch"-type memory flip-flop.  When we describe a CMOS process as being an X-nanometer process, what does that describe?
\\end{{problem}}

\\newpage

\\begin{{problem}}
\\Large Complete the truth table for this circuit.

\\vspace{{1cm}}

\\hspace{{10mm}}
\\includesvg[width=0.7\\textwidth]{{circuit_2.svg}}

\\vspace{{1cm}}

\\Large
\\begin{{tabular}}{{c|c|c||c||c||c||c||c}}
     & & & (D) & (E) & (F) & (G) &  \\\\
    A & B & C & \\hspace{{2cm}} & \\hspace{{2cm}} & \\hspace{{2cm}} & \\hspace{{2cm}} & \\hspace{{2cm}} \\\\
    \\hline
    0 & 0 & 0 & & & & & \\\\
    \\hline
    0 & 0 & 1 & & & & & \\\\
    \\hline
    0 & 1 & 0 & & & & & \\\\
    \\hline
    0 & 1 & 1 & & & & & \\\\
    \\hline
    1 & 0 & 0 & & & & & \\\\
    \\hline
    1 & 0 & 1 & & & & & \\\\
    \\hline
    1 & 1 & 0 & & & & & \\\\
    \\hline
    1 & 1 & 1 & & & & & \\\\
\\end{{tabular}}

\\end{{problem}}

\\newpage

\\begin{{problem}}
\\Large {short_answer[0]}
\\end{{problem}}


\\vspace{{9cm}}

\\begin{{problem}}
\\Large {short_answer[1]}
\\end{{problem}}

\\newpage

\\begin{{problem}}
\\Large {short_answer[2]}
\\end{{problem}}

\\vspace{{9cm}}

\\begin{{problem}}
\\Large {short_answer[3]}
\\end{{problem}}

\\newpage

\\begin{{problem}}
\\Large {short_answer[4]}
\\end{{problem}}

\\vspace{{9cm}}

\\begin{{problem}}
\\Large {short_answer[5]}
\\end{{problem}}

\\end{{document}}

'''

circuit_1 = rand_circuit(3, 1, 2)
print(f"Circuit 1 is {circuit_1}")
gate = logic_parser.logicparse(circuit_1)
# gate.draw()
gate.save('circuit_1.svg')

circuit_2 = rand_circuit(5, 2, 3)
print(f"Circuit 2 is {circuit_2}")
gate = logic_parser.logicparse(circuit_2)
# gate.draw()
gate.save('circuit_2.svg')

and_gate = logic_parser.logicparse("A and B")
and_gate.save('and.svg')

or_gate = logic_parser.logicparse("A or B")
or_gate.save('or.svg')

xor_gate = logic_parser.logicparse("A xor B")
xor_gate.save('xor.svg')

nand_gate = logic_parser.logicparse("A nand B")
nand_gate.save('nand.svg')

nor_gate = logic_parser.logicparse("A nor B")
nor_gate.save('nor.svg')

xnor_gate = logic_parser.logicparse("A xnor B")
xnor_gate.save('xnor.svg')

not_gate = logic_parser.logicparse("not A")
not_gate.save('not.svg')

with open('test2.tex', 'w') as latex_file:
    latex_file.write(latex_code)
