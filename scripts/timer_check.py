legit = list(range(0, 10001, 50))                    # a packet every 50 ms (20 per second)
timer = [round(i * 1000 / 24) for i in range(241)]   # 24 packets per second
laggy = list(range(0, 4001, 50)) + [5000 + i * 2 for i in range(20)] + list(range(5050, 10001, 50))

# The lists are the times (in ms) that the server received packets from the players.
# So if we want to know how many gaps, we can just do the amount of packets - 1: (len - 1)

def is_timer(times_ms):
    time_range = (times_ms[-1] - times_ms[0]) / 1000 # Change from ms to s
    actual_gaps = len(times_ms) - 1
    expected_gaps = time_range * 20 # There should be 20 per second
    gap_ratio = actual_gaps / expected_gaps
    if gap_ratio > 1.05: # We use 1.05 in case a player is still laggy in the interval we are checking in.
        return True
    else:
        return False

print(is_timer(legit))
print(is_timer(timer))
print(is_timer(laggy))