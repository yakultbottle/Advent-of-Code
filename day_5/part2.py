from collections import defaultdict
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
    incorrect_reports = []
    greater = defaultdict(set)
    for i in range(len(before)):
        greater[before[i]].add(after[i])
    
    for page in pages:
        ok = True
        for i in range(len(page)):
            for j in range(1, len(page) - i):
                if page[j - 1] in greater[page[j]]:
                    ok = False
                    temp = page[j]
                    page[j] = page[j - 1]
                    page[j - 1] = temp
        if not ok:
            incorrect_reports.append(page)
    
    output = []
    for report in incorrect_reports:
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
