import random

pass_amount = int(input("How many passwords do you want?\n"))
pass_size = int(input("What should be length of the password?\n"))
for i in range(pass_amount):
	print("".join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * pass_size, pass_size)))