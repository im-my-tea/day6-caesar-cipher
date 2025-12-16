
scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

grades = {}

for i in scores:
    if scores[i] > 90:
        grades[i] = "A"
    elif scores[i] > 80:
        grades[i] = "B"
    elif scores[i] > 70:
        grades[i] = "C"
    else:
        grades[i] = "F"

print(grades)
