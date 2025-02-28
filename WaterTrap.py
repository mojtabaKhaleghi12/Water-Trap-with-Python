def trapped_water(heights):
    if not heights or len(heights) < 3:
        return 0

    n = len(heights)
    max_left = [0] * n
    max_right = [0] * n

    max_left[0] = heights[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], heights[i])

    max_right[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], heights[i])

    total_water = 0
    for i in range(n):
        total_water += max(0, min(max_left[i], max_right[i]) - heights[i])

    return total_water

user_input = input()
heights = list(map(int, user_input.split()))

result = trapped_water(heights)
print(result)
