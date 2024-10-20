from hash_table import HashTable

def main():
    hash_table = HashTable()

    hash_table[52] = "Mars"
    hash_table[7] = "Venus"
    hash_table[12] = "Saturn"
    hash_table[0] = "Earth"
    hash_table[99] = "Mercury"
    hash_table[75] = "Jupiter"
    hash_table[1000] = "Uranus"
    hash_table[1050] = "Neptune"


    print(hash_table[75])
    hash_table[75] = "Giellnor"
    print(hash_table[75])
    print(hash_table[1050])
    print(hash_table.data)
    print(hash_table.get(0))
    print(hash_table.put(12, "Sun"))
    print(hash_table.data)



if __name__ == "__main__":
    main()