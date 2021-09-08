# A simple program that pulls data from excel sheet that gives price based on date
# # https://www.youtube.com/watch?v=ea8BRGxGmlA
# https://www.youtube.com/watch?v=ISir207RuKQ&t=550s

# stock_prices = {}
# filename = "stock_prices.csv"
#
# try:
#     with open(filename, "r+") as file:
#         for line in file:
#             tokens = line.split(",")
#             day = tokens[0]
#             price = float(tokens[1])
#             stock_prices[day] = price
# except FileNotFoundError:
#     print("Sorry, the file " + filename + " doesn't exit")
#
# # If we wanna know the price on Mar 9:
# # Finding an element in the dictionary is O(1)
# print(f"The price of March 9 is : {stock_prices['9-Mar']}")
#
# print(stock_prices)


###############################################################

# First thing of implementing hash map in Python is implementing hash function
# def get_hash(key: str) -> int:
#     hashing = 0
#     for char in key:
#         hashing += ord(char)
#     return hashing % 10 # Assuming 10 is size of our list
#
# # Testing out hash function
# print(get_hash('march 9'))

# IMPLEMENTING HASH MAP CLASS
class HashMap:
    def __init__(self):
        self.size = 10
        # Initialize 10 elements using list comprehension, value of each el is None
        # self.arr = [None for _ in range(self.size)]
        self.arr = [None] * self.size

        # Without list comprehension
        # self.mapping = [0] * 10
        # for i in range(len(self.mapping)):
        #     self.mapping[i] = None

    def get_hash(self, key: str) -> str:
        hashing = 0
        for char in key:
            hashing += ord(char)
        return hashing % self.size

    # Implement a function that adds elements from hash map
    # def __setitem__(self, key: str, val: int) -> None: # replace add() func with standard operator
    def add(self, key: str, val: int) -> None:
        # Retrieve hash function
        h = self.get_hash(key)  # 'march 6' the hash will be 9 index
        # map that 9 index into our array
        self.arr[h] = val

    # Implement a function that gets elements from hash map
    # def __getitem__(self, key: str) -> int: # replace get() func with standard operator
    def get(self, key: str) -> int:
        # Retrieve hash function
        h = self.get_hash(key)  # 'march 6' the hash will be 9 index
        # Return that array
        return self.arr[h]

    # Implement a function that gets elements from hash map
    # def __delitem__(self, key: str) -> None: # replace remove() func with standard operator
    def remove(self, key: str) -> None:
        # Retrieve hash function
        h = self.get_hash(key)  # 'march 6' the hash will be 9 index
        # Set None to our array
        self.arr[h] = None


# Make an object from our class
hashmap = HashMap()
print(f"The hash values of 'march 6' is: {hashmap.get_hash('march 6')}")
hashmap.add('march 6', 130)
print("Down below 130 is at index 9 inside our list, the rest is None. Here the status of my array: ")
print(hashmap.arr)
print(
    f"The corresponding value of 'march 6' in our hash map is: {hashmap.get('march 6')}")
print(f"The key of 'march 6 is deleted: {hashmap.remove('march 6')}")


# Without calling add, get, and remove functions and replacing them with standard operations
# hashmap['march 6'] = 130 # __setitem__()
# hashmap['march 6'] # __getitem__()
# del hashmap['march 6'] # __delitem__()
