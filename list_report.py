
shopping_list = ["milk", "bread", "eggs", "milk", "rice"]

print("SHOPPING LIST REPORT")
print("--------------------")

print("All items:")
for item in shopping_list:
    print("-", item)

print("\nTotal items:", len(shopping_list))

unique_items = []

for item in shopping_list:
    if item not in unique_items:
        unique_items.append(item)

print("Unique items:", len(unique_items))

print("\nItem counts:")
for item in unique_items:
    count = shopping_list.count(item)
    print(item, ":", count)
