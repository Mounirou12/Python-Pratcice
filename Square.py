def square_sum(numbers):
    return sum([x**2 for x in numbers])
# Exécution :
# 1. [x**2 for x in numbers] → [1, 4, 9, 16, 25]
# 2. sum([1, 4, 9, 16, 25]) → 55
# 3. return 55

# Version plus efficace avec un générateur (moins de mémoire)
# return sum(x**2 for x in numbers)  # Pas de crochets []
print(square_sum([1, 2, 2]))