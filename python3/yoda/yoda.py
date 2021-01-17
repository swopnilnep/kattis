# https://open.kattis.com/problems/yoda

from sys import stdin

def read_line_as_str():
    return str(stdin.readline()).strip()

# Read the numbers
in1 = read_line_as_str()
in2 = read_line_as_str()

in_diff = len(in1) - len(in2)
if in_diff > 0:
    in2 = '0' * in_diff + in2
elif in_diff < 0:
    in1 = '0' * abs(in_diff) + in1
if in1 == in2 == '':
    in1 = in2 = '0'

out1 = out2 = ''
for char1, char2 in zip(in1, in2):
    char_diff = int(char1) - int(char2)
    
    # Num 1 is greater
    if char_diff > 0:
        out1 += char1
    # Num 2 is greater
    elif char_diff < 0:
        out2 += char2
    # They are equal
    else:
        out1 += char1
        out2 += char2

def clash_or_yoda(s : str):
    return int(s) if s else 'YODA'

print(clash_or_yoda(out1))
print(clash_or_yoda(out2))
