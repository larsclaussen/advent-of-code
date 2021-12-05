from itertools import tee
from pathlib import Path

ADVANCE_BY = 1


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def part_one():
    input_file = Path("./data/measurements.txt")
    with input_file.open("r") as f:
        answer = sum([int(x) < int(y) for x,y in pairwise(f)])

    print(f"ANSWER: {answer}")
    return answer


def part_two():
    data = []
    input_file = Path("./data/measurements.txt")
    with input_file.open("r") as f:
        for line in f:
            data.append(int(line.strip("\n")))

    # slice_start = 0
    # slice_end = 3
    # import ipdb;ipdb.set_trace()
    # while slice_start < len(data):
    #     win = data[slice_start:slice_end]
    #     if len(win) != 3:
    #         print(f"Remaining window size: {win}, aborting...")
    #         break
    #     slice_start += ADVANCE_BY
    #     slice_end += ADVANCE_BY
    
    sums = []
    ws = 3
    for i, _ in enumerate(data):
        x = data[i:ws]
        if len(x) != 3:
            print(f"Remaining window size: {x}, aborting...")
            break
        sums.append(sum(x))
        ws += 1
    # import ipdb;ipdb.set_trace()
    answer = sum([x < y for x,y in pairwise(sums)])
    print(f"ANSWER: {answer}")



if __name__ == "__main__":
    part_one()
    part_two()
