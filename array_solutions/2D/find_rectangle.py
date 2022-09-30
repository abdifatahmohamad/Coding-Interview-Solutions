def find_rectangle(image):
    rows, cols = len(image), len(image[0])
    visited = set()

    first = (999999, 999999)
    last = (-999999, -999999)

    def dfs(r, c):
        nonlocal first, last
        visited.add((r, c))
        if r + c < first[0] + first[1]:
            first = (r, c)
        if r + c > last[0] + last[1]:
            last = (r, c)
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            dr, dc = r + direction[0], c + direction[1]
            if dr < 0 or dr >= rows or dc < 0 or dc >= cols \
                    or (dr, dc) in visited or image[dr][dc] != 0:
                continue
            dfs(dr, dc)

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and image[r][c] == 0:
                dfs(r, c)

    return first + last if first != last else first


image1 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
print(find_rectangle(image1))  # (2,3)  row, column

image2 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0],
]
print(find_rectangle(image2))  # (4,6)

image3 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
]
print(find_rectangle(image3))  # (3,5)

image4 = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
print(find_rectangle(image4))  # (0,0)

image5 = [
    [0],
]
print(find_rectangle(image5))  # (0,0)


"""
[(2, 3), (3, 5)]
[(4, 6), (4, 6)]
[(3, 5), (4, 6)]
[(0, 0), (0, 0)]
[(0, 0), (0, 0)]

"""
