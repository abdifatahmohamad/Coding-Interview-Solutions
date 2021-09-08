# https://www.youtube.com/watch?v=w9JhOKb4tyk

class MyHashSet:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    # A function that calculates our hash values [it returns index]
    def hashing(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        # Retrieve hash function
        hv = self.hashing(key)

        if self.map[hv] == None:
            # Add key a list
            self.map[hv] = [key]
        else:  # Means we have a value in there [bucket]
            # Append the new key to the bucket
            self.map[hv].append(key)

    def remove(self, key: int) -> None:
        # Retrieve hash function
        hv = self.hashing(key)

        # Check if there a value in the list
        if self.map[hv] != None:
            # This while loop removes all target value [1,2,3,2]
            while key in self.map[hv]:
                # remove the element until that el isn't exist
                self.map[hv].remove(key)

    def contains(self, key: int) -> bool:
        # Retrieve hash function
        hv = self.hashing(key)

        # Check if there a value in the list
        if self.map[hv] != None:
            # if key in self.map[hv]:
            #     return True
            # else:
            #     return False

            # Short way
            return key in self.map[hv]

        # If none of the above cases are True
        return False


# Instantiate hashMap object
h = MyHashSet()
h.add(33)
h.add(99)
h.add(22)
h.add(2)
h.add(55)
print("The status of my list")
print(h.map)
h.remove(2)
print("The status of my list after removed key number 2 from the bucket ")
print(h.map)  # 2 is removed

h.contains(22)
