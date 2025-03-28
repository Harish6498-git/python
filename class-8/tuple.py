# Tuple
# It is immutable
# It cannot add or delete anykind of element once its fixed
# If anybody trying to add or delete element by using keyword called append or remove it cannot accept because these are immutable
# Its indicated with ()

s3_buckets_lists = ("s1_demo", "s2_demo", "s3_demo", "s4_demo")

print(s3_buckets_lists)
print(type(s3_buckets_lists))

# s3_buckets_lists = ("s1_demo", "s2_demo", "s3_demo", "s4_demo")

# s3_buckets_lists.append("s5_demo")

# print(s3_buckets_lists)


# length(len)

s3_buckets_lists = ("s1_demo", "s2_demo", "s3_demo", "s4_demo")

print(len(s3_buckets_lists))

# Slicing the elements

s3_buckets_lists = ("s1_demo", "s2_demo", "s3_demo", "s4_demo")
new_lists=s3_buckets_lists[0:2]
print(new_lists)

s3_buckets_lists = ("s1_demo", "s2_demo", "s3_demo", "s4_demo")
new_lists=s3_buckets_lists[0:1]
print(new_lists)