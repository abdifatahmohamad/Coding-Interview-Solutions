# O(w*h) Space || O(w*h) Time
def find_rectangle(image):
    return [find_rectangle_top_left(image), find_rectangle_bottom_right(image)]

# O(1) Space || O(w*h) Time


def find_rectangle_top_left(image):
    for row in range(len(image)):
        for column in range(len(image[row])):
            if image[row][column] == 0:
                return (row, column)
    return None

# O(1) Space || O(w*h) Time


def find_rectangle_bottom_right(image):
    result = []
    for row in range(len(image)):
        for column in range(len(image[row])):
            if image[row][column] == 0:
                result = [row, column]
    return result

# Sugal's optimization


def find_rectangle(image):
    rows, cols = len(image), len(image[0])
    found_first = False
    coordinates = []
    last = None
    for r in range(rows):
        for c in range(cols):
            if image[r][c] == 0 and not found_first:
                coordinates.append((r, c))
                found_first = True
                continue
            if image[r][c] == 0:
                last = (r, c)
    if last:
        coordinates.append(last)

    return coordinates

# My optimization
# O(1) Space || O(w*h) Time


def find_rectangle(image):
    top_left = []
    bottom_right = []
    for row in range(len(image)):
        for column in range(len(image[row])):
            if image[row][column] == 0:
                top_left = (row, column)
                bottom_right = (row, column)
    return [top_left, bottom_right]


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
