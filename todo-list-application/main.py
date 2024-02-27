"""
The Number of cycles should be at least 5 or greater.
A List should be used to store the user input
"""
number_of_cycles = int(input('Provide Number Of User Cycles:'))

# Creating a List for storing user info
user_info: list[str] = []

print(number_of_cycles);
while number_of_cycles >= 5:
    print(f"is the following condition true or false {number_of_cycles > - 5}")
    print(f"current value in number of cycles: {number_of_cycles}")
    user_info.append(input('Provide Your User Info'))
    number_of_cycles = -1
