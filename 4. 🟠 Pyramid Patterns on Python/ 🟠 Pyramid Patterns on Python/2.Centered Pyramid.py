def centered_pyramid(n):
    for i in range(n):
        # Print spaces
        print(' ' * (n - i - 1), end='')
        # Print asterisks
        print('*' * (2 * i + 1))

# Call the function
centered_pyramid(5)
