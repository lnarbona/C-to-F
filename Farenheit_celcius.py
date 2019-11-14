import sys

if len(sys.argv) != 3:
  print ("Usage:
  pythonn Farenheit_celcius.py {F,C} temp")

if sys.argv[1] == "F":
  temp=(int(sys.argv[2]) - 32)*5/9
  print(f"{temp.2f} ºC")

if sys.argv[1] == "C":
  temp=int(sys.argv[2])*9/5 + 32
  print(f"{temp.2f} ºF")
