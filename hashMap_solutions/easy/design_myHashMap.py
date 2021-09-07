class MyHashMap:

    def __init__(self):
        # 1:
        # self.size = 1000001
        # self.mapping = [-1] * self.size

        # 2:
        # self.mapping = [-1 for _ in range(1000001)]

        # 3:
        self.mapping = [-1] * 10
        for i in range(len(self.mapping)):
            self.mapping[i] = -1

    def put(self, key: int, value: int) -> None:
        self.mapping[key] = value

    def get(self, key: int) -> int:
        return self.mapping[key]

    def remove(self, key: int) -> None:
        self.mapping[key] = -1


# Instantiate hashMap object
h = MyHashMap()
h.put(1, 22)
h.put(2, 33)
h.put(3, 44)
h.put(4, 55)
print("The status of my list")
print(h.mapping)
print(f"Access/get the value of key number 1: {h.get(1)}")
h.remove(3)
print("The status of my list after removed key number 3")
print(h.mapping)  # 44 is removed


###############################################

class MyHashMap:
    def __init__(self):
        self.mapping = [-1] * 10
        for i in range(len(self.mapping)):
            self.mapping[i] = -1

    def get_hash(self, key: str) -> int:
        hashing = 0
        for char in key:
            hashing += ord(char)
        return hashing % 10

    def put(self, key: str, value: str) -> None:
        h = self.get_hash(key)
        self.mapping[h] = value

    def get(self, key: str) -> int:
        h = self.get_hash(key)
        return self.mapping[h]

    def remove(self, key: str) -> None:
        h = self.get_hash(key)
        self.mapping[h] = -1


# Instantiate hashMap object
h = MyHashMap()
h.put("Abdifatah", "Junior SWE")
h.put("Farah", "Mid-level SWE")
h.put("Mohamed", "Senior SWE")
print("The status of my list")
print(h.mapping)
print(f"Access/get the value of key 'Abdifatah': {h.get('Abdifatah')}")
h.remove("Farah")
print("The status of my list after removed key 'Farah' ")
print(h.mapping)  # 'Mid-level SWE' value is removed
