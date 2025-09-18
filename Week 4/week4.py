# Written  by Sam Stuyvenberg
# Question 1
'''
larger_num = int(input("Enter a larger number: "))
smaller_num = int(input("Enter a smaller number: "))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num+=1
    print(f"Number of times halved: {num}")
'''
# Question 2

'''
word = input("Enter a word: ")
result = ""
for i in range (1, len(word) -1, 2):
    result += word[i]

print(f"Output = {result}")
'''

# Question 3
'''
num = int(input("Enter a number"))
for num in range(37, 1050 +1):
    if num % 2==0:
        print(num)
'''

# Question 4 
'''

word = ""

while True:
    user_input = input("Enter a letter: ")
    if user_input == "done":
        break
    else:
        word += user_input

# Print out the done
print(f"The final word is {word}")
'''

# Question 5 

start = 50
end = 517

for i in range(start +1, end +1, 2):
    print(i)