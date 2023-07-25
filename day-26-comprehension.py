import random as r
import pandas as p

# List Comprehension

numbers = [1,2,3]
print ([i + 1 for i in numbers])
# new_list = [new_item for item in list]

f_name = 'Alex'
print ([c for c in f_name])

print ([n * 2 for n in range(1,5)])

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
print ([name for name in names if len(name) < 5])
#new_list = [new_item for item in list if test]

print ([name.upper() for name in names if len(name) > 5])


# Dictionary Comprehension

# new_dict = {new_key:new_vaule for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()} # iterates through each key value pair
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

student_scores = {name:r.randint(25,100) for name in names}
print (student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score > 50}
print(passed_students)

# Pandas Comprehension

student_data = p.DataFrame(passed_students, index=[0])
print(student_data)

for (index, row) in student_data.iterrows():
    print(row)