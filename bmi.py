def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = weight / (height * height)
 print("BMI = " + str(bmi))


 if (bmi < 18.5):
  print("Underweight")
  return 0


 elif (bmi > 25.0):
  print("Overweight")
  return 1

 else:
  print("Normal Weight")
  return -1


calculate_bmi(weight=57, height=1.73)
