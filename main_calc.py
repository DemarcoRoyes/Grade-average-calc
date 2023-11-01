print("Hey hope you did well")

def average(x,y,z):
    return (x + y + z) / 3


exam1 = int(input( "Enter exam 1 score: "))
exam2 = int(input( "Enter exam 2 score: "))
exam3 = int(input( "Enter exam 3 score: "))

num = average(exam1, exam2, exam3)

def grade(num_av):
  if num_av >= 90:
    return "A"
  elif num_av >= 80:
    return "B"
  elif num_av >= 70:
    return "C"
  elif num_av >= 60:
    return "D"
  else:
    return "F"

print(grade(num))
