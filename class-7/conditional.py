import sys

type = sys.argv[1]

if type == "t2.micro":
    print("It will  charge $4.00 PER Day")

elif type == "t2.medium":
    print("It will  charge $6.00 PER Day")

elif type == "t2.large":
    print("It will  charge $8.00 PER Day")

else:
    print("Please provide a proper Instance type")    