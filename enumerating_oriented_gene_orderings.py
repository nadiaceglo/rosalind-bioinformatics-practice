import itertools

n = 6

def signed_permutations(n):
    # Creates list of numbers 1 to n
    nums = list(range(1, n+1))
    # Loops through each positive permutation generated
    for perm in itertools.permutations(nums):
        # Produces lists of all ways to assign a sign to each of the n numbers eg. (1, -1, 1) or (-1, 1, 1)
        for signs in itertools.product([-1, 1], repeat=n):
            # Zip pairs up each element of the permutation with a sign eg. (2, 3, 1) with (-1, 1, -1) = [(2, -1), (3, 1), (1, -1)]
            # Multiplies each number in tuple to give one signed permutation
            # Yield makes this a generator function to save memory
            yield [p * s for p, s in zip(perm, signs)]

perms = list(signed_permutations(n))

output_path = "/Users/macbook/python/rosalind/signed_permutations_output.txt"


with open(output_path, "w") as f:
    f.write(str(len(perms)) + "\n")
    for p in signed_permutations(n):
        f.write(" ".join(map(str, p)) + "\n")