class HashTable:
    def __init__(self):
        self.size = 40
        self.arr = [[] for _ in range(self.size)]

    def get_hash(self, key):
        index = 0
        for char in str(key):
            index += ord(char)
        return index % self.size

    # Adds items to hash table
    def add(self, key, value):
        index = self.get_hash(key)
        found = False;
        kvp = (key, value)
        for i, item in enumerate(self.arr[index]):
            if len(item) == 2 and item[0] == key:
                self.arr[index][i] = kvp
                found = True
                break
        if not found:
            self.arr[index].append(kvp)

    def get(self, key):
        index = self.get_hash(key)
        for item in self.arr[index]:
            if item[0] == str(key):
                return item[1]

    def __getitem__(self, key):
        index = self.get_hash(key)
        for item in self.arr[index]:
            if item[0] == str(key):
                return item[1]
