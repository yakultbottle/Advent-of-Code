import sys

def read_data() -> tuple[list[str],list[str]]:
    input = sys.stdin.read().split("\n\n")
    rules = input[0].splitlines()
    pages = input[1].splitlines()
    return (rules, pages)

def process_rules(rules: list[str]) -> tuple[list[int],list[int]]:
    before = []
    after = []
    for rule in rules:
        pair = [int(x) for x in rule.split("|")]
        before.append(pair[0])
        after.append(pair[1])

    return (before, after)

def process_pages(pages: list[str]) -> list[list[int]]:
    res = []
    for page in pages:
        temp = [int(x) for x in page.split(",")]
        res.append(temp)
    return res

def main(before: list[int], after: list[int], pages: list[list[int]]) -> int:
    correct_reports = []
    before_set = set(before)
    
    for page in pages:
        ok = True
        seen = set()
        for num in page:
            if num in before_set:
                for i in range(len(before)):
                    if before[i] == num and after[i] in seen:
                        ok = False
                        break
            seen.add(num)
        if ok:
            correct_reports.append(page)
    
    output = []
    for report in correct_reports:
        output.append(report[len(report) // 2])

    res = 0
    for line in output:
        res += line
    return res

if __name__ == "__main__":
    input = read_data()
    before, after = process_rules(input[0])
    pages = process_pages(input[1])
    output = main(before, after, pages)
    print(output)
