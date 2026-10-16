def average(values):
    """Returns the average of a list (CPS)"""
    if len(values) == 0:
        raise ValueError("The list of CPS Values cannot be empty")

    for i, value in enumerate(values, start=1):
        if not isinstance(value, (int, float)):
            raise TypeError(f"CPS must be a number, (position {i})")

    total = 0
    for value in values:
        total += value

    return total / len(values)

def cps_category(cps):
    """Returns the categorization of the player based on how high the CPS is"""
    if cps < 0:
        raise ValueError(f"CPS cannot be negative, got {cps}")

    if cps > 20:
        return "review"

    elif cps >= 16:
        return "very fast"

    elif cps >= 12:
        return "fast"

    elif cps >= 8:
        return "normal"

    else:
        return "casual"

def report(name, readings):
    """Prints the report for a player"""
    avg = average(readings)
    print(f"{name}: average {avg:.2f} CPS -> {cps_category(avg)}")

alex = [9.5, 11.0, 10.2, 10.8, 9.9]
steve = [6.0, 7.5, 6.8, 7.1]
tom = [10.0, 10.0, 10.0, 10.0, 10.0]
kai = [19.5, 20.5, 20.0, 20.0, 20.0]
zed = [22.0, 23.5, 21.0, 24.5]

report("alex", alex)
report("steve", steve)
report("tom", tom)
report("kai", kai)
report("zed", zed)

# report("ghost", [])
# average([10, "12", 8])
# cps_category(-3)