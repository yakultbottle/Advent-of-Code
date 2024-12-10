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
        while arr[left] != '.':
            if not left < right:
                break
            left += 1
        while arr[right] == '.' and left < right:
            if not left < right:
                break
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]

def post_process(arr: list[str]) -> int:
    output = 0
    for idx in range(len(arr)):
        if arr[idx] == '.':
            break
        num = int(arr[idx])
        output += idx * num
    return output

if __name__ == "__main__":
    input = read_data()
    # print(input)
    main(input)
    # print(input)
    output = post_process(input)
    print(output)
