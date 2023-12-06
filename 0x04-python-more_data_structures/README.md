**Python - More Data Structures: Set, Dictionary**

**Sets:**

Sets in Python are an unordered collection of unique elements. Here's how to use them:

```python
# Creating a set
my_set = {1, 2, 3}

# Adding elements to a set
my_set.add(4)

# Removing elements from a set
my_set.remove(2)

# Common set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Union
intersection_set = set1 & set2  # Intersection
difference_set = set1 - set2  # Set difference

# Iterating through a set
for item in my_set:
    print(item)
```

**Common Set Methods:**

1. `add(element)`: Adds an element to the set.
2. `remove(element)`: Removes an element from the set. Raises an error if the element is not present.
3. `union(other_set)`: Returns a new set containing all elements from the current set and another set.
4. `intersection(other_set)`: Returns a new set containing elements present in both sets.
5. `difference(other_set)`: Returns a new set containing elements that are in the current set but not in the other set.

**When to Use Sets vs. Lists:**

Use sets when you need to work with unique elements and don't care about the order. Lists allow duplicates, while sets ensure uniqueness.

**Dictionaries:**

Dictionaries are collections of key-value pairs. Here's how to use them:

```python
# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values by key
name = my_dict['name']

# Modifying values
my_dict['age'] = 31

# Adding new key-value pairs
my_dict['country'] = 'USA'

# Removing a key-value pair
del my_dict['city']

# Iterating through a dictionary
for key, value in my_dict.items():
    print(key, value)
```

**When to Use Dictionaries vs. Lists or Sets:**

Use dictionaries when you need to associate values with keys, for example, when representing data with named attributes or when implementing key-value storage.

**Key in a Dictionary:**

A key in a dictionary is a unique identifier that maps to a specific value.

**Iterating Over a Dictionary:**

You can iterate over a dictionary using a `for` loop to access keys and their corresponding values, as shown in the code example above.

**Lambda Function:**

A lambda function is an anonymous, small, and inline function in Python. It's typically used for simple operations where defining a full function is unnecessary. For example:

```python
add = lambda x, y: x + y
result = add(3, 4)  # Result is 7
```

**map, reduce, and filter Functions:**

1. `map(function, iterable)`: Applies the given function to each element of the iterable and returns a new iterable with the results.

2. `reduce(function, iterable)`: Applies the given function cumulatively to the elements of the iterable, reducing it to a single value.

3. `filter(function, iterable)`: Filters elements from the iterable based on the given function's condition and returns a new iterable containing the filtered values.
