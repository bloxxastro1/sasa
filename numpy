import numpy as np
import pandas as pd
num_students = int(input("enter the number of students: "))
num_subjects = int(input("enter the number of subjects: "))
arr = np.zeros((int(num_students), int(num_subjects)))

for i in range(num_students):
    print(f"\nEnter the marks for students{i+1}:")
    for j in range(num_subjects):
        arr[i, j] = int(input(f"Subject{j+1}: "))

sum_grades = np.sum(arr)
percentage = (sum_grades / (num_subjects * 100)) * 100

if percentage > 90:
    print("a+")
elif 89 > percentage > 80:
    print("a")
elif 79 > percentage > 70:
    print("b+")
elif 69 > percentage > 60:
    print("b")
elif 59 > percentage > 50:
    print("c")
else :
    print("f")

df = pd.DataFrame(arr)
print(df)
