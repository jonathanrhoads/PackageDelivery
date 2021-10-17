class HashTable:

    # Constructor creates an empty list of lists based off of the given initial capacity.
    # Time: O(n)
    def __init__(self, initial_capacity=10):
        '''
        O(n)
        :param initial_capacity:
        '''
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


    def insert(self, item):
        '''
        Inserts item into hash table.
        Time: O(1)
        :param item:
        :return:
        '''
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        bucket_list.append(item)

    def insert(self, key, item):
        '''
        Overload of insert that takes a key to place item at. If key is found, value will be updated.
        O(n)
        :param key:
        :param item:
        :return:
        '''
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Updates the key if found inside the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # If key is not found, item is inserted to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        '''
        Iterates through the bucket list's keys to find a match. If match is found then the value will be returned.
        If the value is not found then None will be returned.
        O(n)
        :param key:
        :return:
        '''
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

        return None

    #
    def remove(self, key):
        '''
        Iterates through the bucket list and if a matching key is found then the key and corresponding value will be
        removed.
        O(n)
        :param key:
        :return:
        '''
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
