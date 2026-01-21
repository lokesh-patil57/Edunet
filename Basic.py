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