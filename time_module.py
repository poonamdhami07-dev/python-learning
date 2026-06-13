# time module 
import time
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Current time:", current_time)
hour = int(time.strftime("%H"))
print(hour)
minute = int(time.strftime("%M"))
print(minute)
second = int(time.strftime("%S"))
print(second)


if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
else:
    print("Good Night")



