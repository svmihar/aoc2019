in_range = (245318, 765747)


def check(num_range):
    digits = [int(x) for x in str(num_range)]
    sama = {}
    for k, v in enumerate(digits):
        if k + 1 < len(digits) and v > digits[k + 1]:
            return False
        if k + 1 < len(digits) and v == digits[k + 1]:
            if v not in sama.keys():
                sama[v] = 0
            sama[v] += 1
    print(sama)
    return list(sama.values()) or False

print(len([x for x in range(*in_range) if check(x)]))
print(len([x for x in range(*in_range) if check(x) and 1 in check(x)]))