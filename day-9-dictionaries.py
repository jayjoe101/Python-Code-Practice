dict = {} # curly braces makes dict

x_dict = {'key1':'value', 'key2':'value'} # sorted by keys with corresponding value
print(x_dict['key1']) # instead of index simply grab the key, this will return the value
x_dict['key3'] = 'value' # to add new items progamatically

print(x_dict)

x_dict = {} # wipes the dictionary

print(x_dict)

for key in x_dict: # when iterating through a dict x in dict will equal the key
    print(x_dict[key]) # will iterate through the values of the dict
    x_dict[key] = 'hello' # manipulates dict values

# --example--
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)
# --example--

nested_dict = {
    'key1': ['a','b','c','d'],
    'key2': {'key3': 'value'},
}
print(nested_dict)