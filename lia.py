from math import factorial

def probability(k, N):
  """
  Calculates the probability of having at least N Aa Bb organisms in the k-th generation.

  Args:
    k: The generation number (k <= 7).
    N: The minimum number of Aa Bb organisms required (N <= 2k).

  Returns:
    The probability as a float.
  """

  # Calculate the total number of organisms in the k-th generation
  total_organisms = 2**k

  # Calculate the probability of a single organism being Aa Bb
  probability_AaBb = 1/4

  # Calculate the probability of having exactly N Aa Bb organisms
  probability_exactly_N = (factorial(total_organisms) / (factorial(N) * factorial(total_organisms - N))) * (probability_AaBb**N) * ((1 - probability_AaBb)**(total_organisms - N))

  # Calculate the probability of having at least N Aa Bb organisms
  probability_at_least_N = 0
  for i in range(N, total_organisms + 1):
    probability_at_least_N += (factorial(total_organisms) / (factorial(i) * factorial(total_organisms - i))) * (probability_AaBb**i) * ((1 - probability_AaBb)**(total_organisms - i))

  return probability_at_least_N

# Example usage:
k = 6  # Generation number
N = 16  # Minimum number of Aa Bb organisms

probability_result = probability(k, N)
print(f"Probability of having at least {N} Aa Bb organisms in the {k}-th generation: {probability_result:.4f}")