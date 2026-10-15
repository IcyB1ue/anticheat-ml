cps_values = [6.5, 9.8, 13.2, 21.4, 11.0, 17.9, 7.2, 25.0]
casual = 0
normal = 0
fast = 0
very_fast = 0
review = 0

for i, cps in enumerate(cps_values, start=1):
    if cps > 20:
        review += 1
        print(f"Player {i}: {cps:.1f} CPS -> review")

    elif cps >= 16:
        very_fast += 1
        print(f"Player {i}: {cps:.1f} CPS -> very_fast")

    elif cps >= 12:
        fast += 1
        print(f"Player {i}: {cps:.1f} CPS -> fast")

    elif cps >= 8:
        normal += 1
        print(f"Player {i}: {cps:.1f} CPS -> normal")

    elif 0 < cps < 8:
        casual += 1
        print(f"Player {i}: {cps:.1f} CPS -> casual")

    else:
        print(f"Player {i} does not have a valid CPS")

print("The Counts:")
print(f"Casuals: {casual}")
print(f"Normal: {normal}")
print(f"Fast: {fast}")
print(f"Very Fast: {very_fast}")
print(f"Needs Review: {review}")