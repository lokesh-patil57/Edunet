# Demonstrating basic list operations in Python


print("Basic List Operations:")
l1 = [1,2,3,4,5,6]
print(f"Original list: {l1}")
l1.append(7)
print(f"List after appending 7: {l1}")
l1.remove(3)
print(f"List after removing 3: {l1}")
l1.insert(2, 7)
print(f"List after inserting 7 at index 2: {l1}")
l1.reverse()
print(f"List after reversing: {l1}")
l1.sort()
print(f"List after sorting: {l1}")

#Dictionary operations


print("\nBasic Dictionary Operations:")
city_data = {
    "New York": "USA",
    "Tokyo": "Japan",
    "Delhi": "India",
    "London": "UK"
}

print(f"Original dictionary: {city_data}")

city_data.get("Tokyo")
print(f"Country for Tokyo: {city_data['Tokyo']}")

city_data["Berlin"] = "Germany"
print(f"Dictionary after adding Berlin: {city_data}")

city_data.pop("Delhi")
print(f"Dictionary after removing Delhi: {city_data}")

city_data.keys()
print(f"Keys in the dictionary: {list(city_data.keys())}")

city_data.update({"Sydney": "Australia"})
print(f"Dictionary after updating with Sydney: {city_data}")


#Operators in Python

print("\nBasic Operators in Python:")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}") 
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

print("\nComparison Operators:")
print(f"Equality (a == b): {a == b}")
print(f"Inequality (a != b): {a != b}")
print(f"Greater than (a > b): {a > b}")
print(f"Less than (a < b): {a < b}")
print(f"Greater than or equal to (a >= b): {a >= b}")
print(f"Less than or equal to (a <= b): {a <= b}")

print("\nLogical, Bitwise, Identity and Membership Operators:")
print(f"Logical AND (a > 5 and b < 5): {a > 5 and b < 5}")
print(f"Logical OR (a > 5 or b > 5): {a > 5 or b > 5}")
print(f"Logical NOT (not(a > 5)): {not(a > 5)}")
print(f"Bitwise AND (a & b): {a & b}")
print(f"Bitwise OR (a | b): {a | b}")
print(f"Bitwise XOR (a ^ b): {a ^ b}")
print(f"Bitwise NOT (~a): {~a}")
print(f"Left Shift (a << 1): {a << 1}")
print(f"Right Shift (a >> 1): {a >> 1}")
print(f"Identity (a is b): {a is b}")
print(f"Membership (b in [1,2,3,4,5]): {b in [1,2,3,4,5]}")
