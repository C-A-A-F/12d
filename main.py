import math
side=float(input("Enter the side of a square that is greater than 5:  "))
if side<=5:
  print("Refresh the page..")
else:
  s1=side**2
  side2=side+5
  s2=side2**2
  perce=math.ceil(s2*100/s1)
  print("The square whose side was lengthened by 5 centimetres is",perce,"% larger than the initial square.")