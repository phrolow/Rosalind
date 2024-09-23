# def rabbit_pairs(n, m):
#   """
#   Calculates the number of rabbit pairs remaining after n months, given that rabbits live for m months.
#
#   Args:
#     n: The number of months.
#     m: The lifespan of a rabbit in months.
#
#   Returns:
#     The total number of rabbit pairs remaining after n months.
#   """
#
#   # Initialize rabbit pairs for the first m months
#   rabbit_pairs = [0] * (m + 1)
#   rabbit_pairs[1] = 1  # Start with one pair
#
#   # Calculate rabbit pairs for each month
#   for month in range(2, n + 1):
#     # Add new pairs from previous month's breeding pairs
#     new_pairs = rabbit_pairs[month - 1]
#     # Subtract pairs that died this month
#     rabbit_pairs[month] = new_pairs + rabbit_pairs[month - m]
#
#   return rabbit_pairs[n]

# >>> rabbits(6, 3)
# 4
# >>> rabbits(29, 2)
# 1
# >>> rabbits(28, 5)
# 88412
# >>> rabbits(29, 3)
# 2513
# >>> rabbits(100, 20)
# 353368918335207375428

def rabbit_pairs(n, m):
    """
    Calculates the number of rabbit pairs remaining after n months, given that rabbits live for m months.

    Args:
      n: The number of months.
      m: The lifespan of a rabbit in months.

    Returns:
      The total number of rabbit pairs remaining after n months.
    """

    # Initialize rabbit pairs for the first m months
    pairs = [0] * (m + n + 1)
    pairs[0] = 1  # Start with one pair
    pairs[1] = 1
    pairs[m] -= 1

    # Calculate rabbit pairs for each month
    for month in range(2, n + 1):
        # Add new pairs from previous month's breeding pairs
        new_pairs = pairs[month - 2]
        pairs[month - 1 + m] -= new_pairs
        # Subtract pairs that died this month
        pairs[month] += new_pairs + pairs[month - 1]

    return pairs[n - 1]


# Example usage:
n = 99  # Number of months
m = 20  # Rabbit lifespan in months

remaining_pairs = rabbit_pairs(n, m)
print(f"Total rabbit pairs remaining after {n} months: {remaining_pairs}")