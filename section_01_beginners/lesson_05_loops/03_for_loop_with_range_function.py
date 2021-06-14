for num in range(1, 11): # 2nd agrument is not inclusive
  print(num)

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
total = 0
for num in range(2, 101, 2):
  total += num

print(f"Total (2 + 4 + 6 + 8 +10 ... + 98 + 100) = {total}")