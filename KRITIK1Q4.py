def approximation_arctan(x):
    # Check if x is within the range [0, 1] for arctan
    if x < 0 or x > 1:
        return "Error!"

    # Initialize variables
    a = 0.0
    error_bound = float('inf')
    n = 0

    # Loop to calculate the approximation until the error at most reaches 0.0001
    while error_bound > 0.0001:
        # Calculate the term using the series expansion
        term = abs(a(-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
        a += term

        # Update n for the next iteration
        n += 1

        # Determine error bound in the calculation
        error_bound = x ** (2 * n + 1) / (2 * n + 1)

    return (a, n, error_bound)


# Testing the function
test_values = [-1, 0, 0.25, 0.5, 0.75, 1]
results = {val: approximation_arctan(val) for val in test_values}

for val, result in results.items():
    print(f"arctan_approximation({val}) = {result}")

