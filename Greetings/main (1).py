#greeting program according to timings
#to convert online timing i.e. is greenwhich mean time to indian timeings run this program on downloaded software or local computer terminal
import time
a = time.strftime("%H:%M:%S")
print(a)
b = int(time.strftime("%H"))
if (5<=b and b<=12):
  print("Good Morning")
elif (12<=b and b<=17):
  print("Good Afternoon")
elif (17<=b and b<=21):
  print("Good Evening")
else:
  print("Good Night")
