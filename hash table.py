class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        total = 0
        for char in string:
            total += ord(char)
        return total

    def add(self, key, value):
        index = self.hash(key)

        if index not in self.collection:
            self.collection[index] = {}

        self.collection[index][key] = value

    def remove(self, key):
        index = self.hash(key)

        # If index exists and key exists, remove only that key
        if index in self.collection and key in self.collection[index]:
            del self.collection[index][key]

            # Remove empty dictionary after deleting last key
            if self.collection[index] == {}:
                del self.collection[index]

    def lookup(self, key):
        index = self.hash(key)

        if index in self.collection and key in self.collection[index]:
            return self.collection[index][key]

        return None


# Example Testing

table = HashTable()

table.add("golf", "sport")
print(table.collection)
print(table.lookup("golf"))

table.add("dear", "friend")
table.add("read", "book")
print(table.collection)

table.add("rose", "flower")
print(table.collection)

table.add("fcc", "coding")
table.add("cfc", "chemical")
print(table.collection)

table.remove("golf")
print(table.collection)

table.remove("unknown")   # Should not raise error
print(table.collection)
