# Lists
# Lists are mutable
# If you need any elements to be added or remove by using keywords for adding keyword is "append" and remove the element the keyword is "remove"
# It indicates with []

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]

print(s3_buckets_lists)

# If you want to know which type is that you should use keyword called "type"

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]

print(type(s3_buckets_lists))

# adding the element using keyword "append"

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]

s3_buckets_lists.append("s5_demo")

print(s3_buckets_lists)

# adding the element using keyword "remove"

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]

s3_buckets_lists.remove("s4_demo")

print(s3_buckets_lists)

# if you need to print a particular element

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]
print(s3_buckets_lists[1])

# If you need to find the length of the element use keyword "len"

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]
print(len(s3_buckets_lists))

s3_buckets_lists.append("s5_demo")
print(len(s3_buckets_lists))

s3_buckets_lists.remove("s4_demo")
s3_buckets_lists.remove("s5_demo")
print(len(s3_buckets_lists))

# Slicing the elements

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]
new_lists=s3_buckets_lists[0:2]
print(new_lists)

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]
new_lists=s3_buckets_lists[0:3]
print(new_lists)

# Concatination

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]

print(s3_buckets_lists[0] + "," + s3_buckets_lists[2])

# You can check if an element exists in a list using the in keyword.
# Its give output like boolean if present the result is true and if not its falseS

s3_buckets_lists = ["s1_demo", "s2_demo", "s3_demo", "s4_demo"]

is_present = 's3_demo' in s3_buckets_lists
print(is_present)

is_present = 's5_demo' in s3_buckets_lists
print(is_present)