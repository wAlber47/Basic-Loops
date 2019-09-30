"""
Implement a basic countdown from ten
First using 'while' then using a 'for'
William Alber 9/30/2019
"""

# while loop
print("Countdown: 'while' loop")
i = 10
while i >= 0:
    print(i)
    i = i - 1

# for loop
print("\nCountdown: 'for' loop")
for i in reversed(range(0, 11)):
    print(i)
