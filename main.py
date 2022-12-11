def fibonacci(n: int) -> list:
    """Calculates the nth value in the Fibonacci Sequence.
    n (int): a number for the nth fibonacci.
    Returns a list of int from n=0 to n=n.
    """
    sequence = None
    # These are assumptions for the Fibonacci sequence:
    f_0 = 0
    f_1 = 1
    # If n < 0, we have nothing to return, so we'll return an empty list.
    if n < 0:
        sequence = []
    # If n == 0, we know we want F_0 in the list.
    elif n <= 0:
        sequence = [f_0]  # this inserts a number in our list.
    # If n == 1, we know we want F_0 and F_1 in the list.
    elif n <= 1:
        sequence = [f_0, f_1]

    # If n >= 2, we can get each new F_n from the last two values in the list.
    elif n >= 2:
        sequence = [f_0, f_1]
        # Run this code for each number in range 2 to n.
        for _ in range(2, n+1):
            # f_n is sum of the last two numbers in the sequence.
            f_n = sequence[-1] + sequence[-2]
            # We want to append this (insert to the end of our sequence)
            sequence.append(f_n)
    return sequence


if __name__ == "__main__":
    # print("F_-1 (E: [])=", fibonacci(n='text'))  # This would give an error.
    print("F_-1 (E: []) =", fibonacci(n=-1))
    print("F_0 (E: [0]) =", fibonacci(n=0))
    print("F_1 (E: [0, 1]) =", fibonacci(n=1))
    print("F_2 (E: [0, 1, 1]) =", fibonacci(n=2))
    print("F_3 (E: [0, 1, 1, 2]) =", fibonacci(n=3))
    print("F_4 (E: [0, 1, 1, 2 ,3]) =", fibonacci(n=4))