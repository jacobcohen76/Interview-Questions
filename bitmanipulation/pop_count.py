
def pop_count(x: int) -> int:
    count = 0
    while x:
        count += 1
        x &= x ^ -x
    return count

print(pop_count(0x3F))