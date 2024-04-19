with open('provinces.txt', 'r') as file:
    provinces_list = file.readlines()

print("Original list:")
print(provinces_list)

first_element = provinces_list.pop(0)
print("\nRemoved first element:", first_element)

last_element = provinces_list.pop()
print("Removed last element:", last_element)

provinces_list = [province.strip().replace("AB", "Alberta") for province in provinces_list]

print("\nModified list:")
print(provinces_list)

num_alberta = provinces_list.count("Alberta")
print("\nNumber of elements that are 'Alberta':", num_alberta)
