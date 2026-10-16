LIMIT = 15


def rate(hits, seconds=4):
    if seconds <= 0:
        raise ValueError(f"seconds must be positive, got {seconds}")
    return hits / seconds


def grade(r):
    if r >= LIMIT:
        return "flag"
    elif r >= 5:
        return "watch"
    return "fine"


def log(name, hits, seconds=4):
    r = rate(hits, seconds)
    print(f"{name}: {r:.2f}/s {grade(r)}")


def bump(score):
    score = score * 3
    return score


log("eli", 30)
out = log("fay", 90, seconds=5)
print(out)
print(round(4.5), round(5.5), -9 // 4, 9 % 4)

score = 2
for k, ms in enumerate([40, 2000, 60, 55], start=1):
    if ms > 1000:
        print(f"skip {k}")
        continue
    score += 1
print(score, k, ms)
print(bump(score), score)

m = 1
while m < 20:
    m *= 3
print(m)

log("gus", 12, seconds=0)
print("end")

# What will be printed out?
# The correct answer is
# eli: 7.50/s watch
# fay: 18.00/s flag
# None
# 4 6 -3 1
# skip 2
# 5 4 55
# 15 5
# 27