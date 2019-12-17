import itertools


def pattern(output_element):
    while True:
        for _ in range(output_element):
            yield 0
        for _ in range(output_element):
            yield 1
        for _ in range(output_element):
            yield 0
        for _ in range(output_element):
            yield -1


def ones_digit(n):
    if n > 0:
        return n % 10
    else:
        return (-n) % 10


def fft_phase(numbers):
    output = []
    n = len(numbers)
    for i in range(n):
        pat = pattern(i + 1)
        next(pat)

        values = list(zip(pat, numbers))
        total = sum(p * n for p, n in values)
        output.append(ones_digit(total))
    return output


raw = "59738476840592413842278931183278699191914982551989917217627400830430491752064195443028039738111788940383790187992349338669216882218362200304304999723624146472831445016914494176940890353790253254035638361091058562936884762179780957079673204210602643442603213181538626042470133454835824128662952579974587126896226949714610624975813583386749314141495655816215568136392852888525754247201021383516228214171660111826524421384758783400220017148022332694799323429711845103305784628923350853888186977670136593067604033507812932778183786479207072226236705355778245701287481396364826358903409595200711678577506495998876303181569252680220083046665757597971122614"
numbers = [int(c) for c in raw]

for _ in range(100):
    numbers = fft_phase(numbers)
print(numbers[:8])


def part2(raw):
    offset = int(raw[:7])
    numbers = [int(c) for c in raw] * 10_000
    assert offset > len(numbers) // 2
    for _ in range(100):
        pos = len(numbers) - 1
        total = 0
        while pos >= offset:
            total += numbers[pos]
            numbers[pos] = ones_digit(total)
            pos -= 1
    return numbers[offset:offset+8]


mega = numbers * 10_000
offset = 5971981

print(part2(raw))
