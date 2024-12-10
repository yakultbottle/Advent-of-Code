import sys

def read_data() -> list[str]:
    input = [int(num) for num in sys.stdin.read().strip()]
    id = 0
    arr = []
    for i in range(len(input)):
        count = 0
        while count < input[i]:
            if i % 2 == 0:
                arr.append(str(id))
            else:
                arr.append('.')
            count += 1
        id = id + 1 if i % 2 == 0 else id
    return arr

'''
Let's imagine a 2-pointer solution. Left looks for dots, and swaps with right. 
Right moves to the rightmost non-dot position
End when left <= right? or left < right?
'''

# Modifies arr in-place
def main(arr: list[str]):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] != '.' and left < right:
            left += 1
        while arr[right] == '.' and left < right:
            right -= 1

        l_end = left
        while l_end < len(arr) and arr[l_end] == ".":
            l_end += 1

        r_start = right
        while r_start > 0 and arr[r_start] == arr[right]:
            r_start -= 1
        r_start += 1

        l_len = l_end - left
        r_len = (right + 1) - r_start

        '''
        print(f"left: {left}, right: {right}")
        print(f"{left} < {right}")

        print(f"{left}-{l_end - 1}, {r_start}-{right}, {l_len}>={r_len}")
        '''
        if arr[right] != "." and l_len >= r_len:
            # print(f"l_start: {left}, l_end: {l_end}, r_start: {r_start}, r_end: {right}")
            '''
            print(f"Before swap: {arr}")
            print()
            print(len(arr))
            print(arr[left:left + r_len])
            print(arr[r_start:right + 1])
            '''
            arr[left:left + r_len], arr[r_start:right + 1] = arr[r_start:right + 1], arr[left:left + r_len]
            '''
            print(arr[left:left + r_len])
            print(arr[r_start:right + 1])
            print()
            print(f"After swap: {arr}")
            print()
            '''
            left = 0
        else:
            if l_end >= right:
                left = 0
                right = r_start - 1
            else:
                left = l_end

def post_process(arr: list[str]) -> int:
    output = 0
    for idx in range(len(arr)):
        if arr[idx] == '.':
            continue
        num = int(arr[idx])
        output += idx * num
    return output

if __name__ == "__main__":
    input = read_data()
    '''
    print(input)
    print()
    '''
    main(input)
    '''
    print(input)
    print()
    '''
    output = post_process(input)
    print(output)
