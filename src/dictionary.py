"""
Simple Dictionary Examples in Python
This program demonstrates various dictionary operations
"""

# 1. Creating a dictionary
print("=== Creating Dictionaries ===")
student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "English"]
}
print("Student dictionary:", student)
print()

# 2. Accessing dictionary values
print("=== Accessing Values ===")
print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student courses:", student["courses"])
print()

# 3. Using get() method (safer way to access values)
print("=== Using get() Method ===")
print("Grade:", student.get("grade"))
print("Phone (doesn't exist):", student.get("phone", "Not available"))
print()

# 4. Adding new key-value pairs
print("=== Adding New Items ===")
student["email"] = "john.doe@example.com"
student["phone"] = "123-456-7890"
print("Updated student dictionary:", student)
print()

# 5. Modifying existing values
print("=== Modifying Values ===")
student["age"] = 21
student["grade"] = "A+"
print("Modified student dictionary:", student)
print()

# 6. Removing items from dictionary
print("=== Removing Items ===")
removed_phone = student.pop("phone")
print("Removed phone:", removed_phone)
print("Dictionary after removing phone:", student)
print()

# 7. Checking if a key exists
print("=== Checking Key Existence ===")
if "name" in student:
    print("'name' exists in the dictionary")
if "address" not in student:
    print("'address' does not exist in the dictionary")
print()

# 8. Iterating through a dictionary
print("=== Iterating Through Dictionary ===")
print("Keys and values:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

print("Only keys:")
for key in student.keys():
    print(f"  {key}")
print()

print("Only values:")
for value in student.values():
    print(f"  {value}")
print()

# 9. Dictionary methods
print("=== Useful Dictionary Methods ===")
print("Number of items:", len(student))
print("All keys:", list(student.keys()))
print("All values:", list(student.values()))
print()

# 10. Nested dictionaries
print("=== Nested Dictionaries ===")
classroom = {
    "student1": {"name": "Alice", "grade": "A"},
    "student2": {"name": "Bob", "grade": "B"},
    "student3": {"name": "Charlie", "grade": "A+"}
}
print("Classroom:", classroom)
print("Student1 name:", classroom["student1"]["name"])
print()

# 11. Creating a dictionary from lists
print("=== Creating Dictionary from Lists ===")
keys = ["apple", "banana", "orange"]
values = [1.5, 0.8, 2.0]
fruit_prices = dict(zip(keys, values))
print("Fruit prices:", fruit_prices)
print()

# 12. Dictionary comprehension
print("=== Dictionary Comprehension ===")
squares = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares)
print()

# 13. Copying a dictionary
print("=== Copying Dictionary ===")
student_copy = student.copy()
print("Original:", student)
print("Copy:", student_copy)
print()

# 14. Clearing a dictionary
print("=== Clearing Dictionary ===")
temp_dict = {"a": 1, "b": 2}
print("Before clear:", temp_dict)
temp_dict.clear()
print("After clear:", temp_dict)
