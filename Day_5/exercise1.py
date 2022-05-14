# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#replicate sum()
sum = 0
for height in student_heights:
    sum+=height
#replicate len()
total_items = 0
for element in student_heights:
    total_items+=1

print(round(sum / total_items))
