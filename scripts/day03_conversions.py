def ticks_to_seconds(ticks, tps=20):
    if tps <= 0:
        raise ValueError(f"TPS must be greater than 0, got {tps}")
    if ticks < 0:
        raise ValueError(f"The amount of ticks cannot be negative, got {ticks}")

    return ticks / tps

def seconds_to_ticks(seconds, tps=20):
    if tps <= 0:
        raise ValueError(f"TPS must be greater than 0, got {tps}")
    if seconds < 0:
        raise ValueError(f"The amount of seconds cannot be negative, got {seconds}")

    return round(seconds * tps)

print(ticks_to_seconds(40))
print(ticks_to_seconds(40, tps=10))
print(seconds_to_ticks(2.5))
print(seconds_to_ticks(0.125))
# print(seconds_to_ticks(-1))
