# HashTable Implementation

This Python implementation of a **Hash Table** stores key-value pairs using hash functions and open addressing for collision resolution. The `HashTable` class provides methods for inserting, retrieving, and handling collisions, as well as basic functionalities like indexing (`__getitem__` and `__setitem__`).

## Key Characteristics of a Hash Table

- **Hash Function**: Maps a key to an index in the internal array, called a **slot**.
- **Collisions**: Handled using **open addressing** with **linear probing** (rehashing).
- **Key-Value Pair Storage**: Each key maps to a data value.
- **Slots**: Internal array that holds the keys, and a separate array holds the corresponding data values.

## Class Structure

### Properties
- `size`: Size of the hash table (default is 11).
- `slots`: List that holds the keys at hashed positions.
- `data`: List that holds the data values corresponding to the keys.

### Methods

#### 1. `put(key, data)`
Inserts a key-value pair into the hash table.
- **Hashing**: Uses a hash function to determine the slot for the key.
- **Collision Resolution**: If a collision occurs (i.e., the slot is already taken), the method uses **rehashing** (linear probing) to find the next available slot.
- **Key Update**: If the key already exists in the hash table, its data value is updated.

#### 2. `hash_function(key, size)`
Generates a hash value for the given key using the modulus operator:
- `hash_value = key % size`
- Ensures the key is mapped to a valid index within the hash table's slots.

#### 3. `rehash(old_hash, size)`
Handles collisions by rehashing the original hash value:
- `rehash_value = (old_hash + 1) % size`
- Moves to the next available slot in the event of a collision (linear probing).

#### 4. `get(key)`
Retrieves the value associated with a given key.
- **Search**: Starts at the slot computed by the hash function and continues rehashing if the key isn't immediately found.
- **Collision Handling**: Uses rehashing (linear probing) to find the correct key in the case of collisions.
- **Return**: Returns the value if the key is found, or `None` if the key is not in the hash table.

#### 5. `__getitem__(key)`
Provides `get` functionality using `[]` indexing.
- Example: `value = hash_table[key]`

#### 6. `__setitem__(key, data)`
Provides `put` functionality using `[]` indexing for setting values.
- Example: `hash_table[key] = value`

## Example Usage

```python
# Initialize the hash table
hash_table = HashTable()

# Insert key-value pairs
hash_table[54] = "cat"
hash_table[26] = "dog"
hash_table[93] = "lion"
hash_table[17] = "tiger"

# Retrieve values using keys
print(hash_table[54])  # Output: "cat"
print(hash_table[26])  # Output: "dog"

# Update a value
hash_table[54] = "mouse"
print(hash_table[54])  # Output: "mouse"

| Operation               | Average Time Complexity | Worst Time Complexity | Space Complexity |
|-------------------------|-------------------------|-----------------------|------------------|
| **Insert (put)**         | O(1)                    | O(n)                  | O(n)             |
| **Retrieve (get)**       | O(1)                    | O(n)                  | O(n)             |
| **Collision (rehash)**   | O(1) (per rehash)       | O(n)                  | O(n)             |

### Notes on Complexity

1. **Average Case (O(1) Time)**: 
   - Insertion and retrieval of values in a hash table are, on average, constant time O(1). This assumes the keys are well-distributed across the slots, leading to minimal collisions.
   - Hash tables are designed to minimize collisions with a good hash function and a load factor that avoids clustering.

2. **Worst Case (O(n) Time)**: 
   - In the worst case, when multiple collisions occur and the load factor of the hash table is high (many elements compared to the number of slots), the performance can degrade to O(n). This is because the `rehash` function (linear probing) may have to traverse the entire table to find an open slot or the key.
   - This occurs when:
     - All elements are hashed to the same slot.
     - The table size is small, and rehashing frequently occurs.

3. **Space Complexity (O(n))**: 
   - The space complexity is O(n), where `n` is the number of slots in the hash table. The hash table uses two arrays, one for storing keys and one for storing data, each of size `n`.
   - No additional space is used beyond the internal arrays to store key-value pairs.

### Load Factor and Hash Table Performance

- The **load factor** of a hash table, defined as the ratio of the number of elements to the size of the table, significantly impacts its performance.
- To maintain efficient operations (O(1) average time), it's essential to resize the hash table when the load factor becomes too high (typically above 0.7 or 0.75).
- **Resizing the Hash Table**: When the hash table is resized, the time complexity temporarily becomes O(n) as all elements need to be rehashed and inserted into the new table. However, this is an infrequent operation and does not affect the average-case performance.