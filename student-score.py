lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student in students:
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(students):
    homework = average(students["homework"])
    homework = average(students['quizzes'])
    homework = average(students['tests'])
    return 0.1 * average(students["homework"]) + 0.3 * average(students['quizzes']) + 0.6 * average(students['tests'])

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print ''
print "Lloyd's grade is: %s" % get_grade(get_average(lloyd))
print "Alice's grade is: %s" % get_grade(get_average(alice))
print "Tylers's grade is: %s" % get_grade(get_average(tyler))

def get_class_average(class_list):
  results = []
  for student in class_list:
    get_average(student)
    results.append(get_average(student))
  return average(results)


students = [lloyd, alice, tyler]
class_avg = get_class_average(students)
print ''
print 'Class average score is: %s' % class_avg
print 'Class average grade is: %s' % get_grade(class_avg)