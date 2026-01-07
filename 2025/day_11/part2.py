input = open(0).read().strip().splitlines()

adj_list: dict[str, list[str]] = {}

for line in input:
    input, *output = line.split()
    adj_list[input[:-1]] = output

adj_list["out"] = []
memo = {}

def num_ways(start: str, target: str, dont_pass: str = "") -> int:
    if (start, target) in memo:
        return memo[(start, target)]

    if start == target:
        return 1
    if start == dont_pass:
        return 0

    count = 0
    for node in adj_list[start]:
        count += num_ways(node, target)

    memo[(start, target)] = count
    return count

dac_first = num_ways(start="svr", target="dac", dont_pass="fft")
fft_first = num_ways(start="svr", target="fft", dont_pass="dac")
dac_fft = num_ways(start="dac", target="fft")
fft_dac = num_ways(start="fft", target="dac")
fft_out = num_ways(start="fft", target="out", dont_pass="dac")
dac_out = num_ways(start="dac", target="out", dont_pass="fft")

# print(f"svr to dac: {dac_first}")
# print(f"svr to fft: {fft_first}")
# print(f"dac to fft: {dac_fft}") # <- this is 0
# print(f"fft to dac: {fft_dac}")
# print(f"fft to out: {fft_out}")
# print(f"dac to out: {dac_out}")

ans = dac_first * dac_fft * fft_out + fft_first * fft_dac * dac_out
print(ans)
