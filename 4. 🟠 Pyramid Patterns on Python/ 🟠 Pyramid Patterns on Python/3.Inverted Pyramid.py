def inverted_pyramid(n):
    for i in range(n, 0, -1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print asterisks
        print('*' * (2 * i - 1))

# Call the function
inverted_pyramid(5)
