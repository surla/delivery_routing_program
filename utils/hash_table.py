class HashTable:
    def __init__(self):
        self.size = 40
        self.arr = [[] for i in range(self.size)]

    def get_hash(self, key):
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.size

    # Adds items to hash table
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self. arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

