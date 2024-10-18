def diamond_pyramid(n):
    # Centered pyramid
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*' * (2 * i + 1))

    # Inverted pyramid
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))


# Call the function
diamond_pyramid(5)
