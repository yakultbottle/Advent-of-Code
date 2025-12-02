answer = 0

while True:
    temp1 = 0
    temp2 = 0
    is_first_digit = True
    try:
        inp = str(input())
    except EOFError:
        break
    for char in inp:
        if char.isdigit():
            if is_first_digit:
                temp1 += (int(char) * 10)
                temp2 = int(char)
                is_first_digit = False
            else:
                temp2 = int(char)
    temp1 += temp2
    answer += temp1

with open('output.txt', 'w') as output:
    output.write(str(answer))