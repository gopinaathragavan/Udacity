#module import
from selenium import webdriver
import time

#User inputs
timerinput = float(input("This is a timer. Please enter number of minutes as a positive whole number:"))
total_breaks = int(input("Enter number of breaks as a positive whole number:"))
break_counter = 1

# Enforces minimum timer and maximum timer of 50 minutes to ensure there is a break after 50 minutes
if  timerinput <1:
    raise ValueError("Enter at least 0.5 minutes")
elif timerinput > 50:
    timerinput = 50
else:
    pass
timer = timerinput * 60

# Based on time worked, enforces a minimum break and also a maximum break to avoid procrastination
if timer >= 3000:
    break_minutes = 20 # enforcing min break of 20 minutes for long hours of work
elif timer <=1500:
    break_minutes = 5 # duration is in seconds to pass to break_timer enforcing minimum break of 15minutes
else:
    break_minutes = 15

break_timer = break_minutes * 60

# Enter pomodoro loop ensuring breakcount is positive
url = str("https://www.google.com.au/search?q=timer+"+str(break_timer)+"+seconds")
while (break_counter <= total_breaks) and (total_breaks > 0):
    print("This timer started at ", time.ctime(), "set for", timer, "seconds.")
    time.sleep(timer)
    browser = webdriver.Chrome()
    browser.get(url)
    print("This break", str(break_counter), "of ", total_breaks, "started at ", time.ctime(), "for", break_timer, "seconds.")
    time.sleep(break_timer)
    browser.close()
    break_counter += 1

#Clear variables from memory
del browser
del url
del timer
del timerinput
del break_minutes
del total_breaks
del break_timer
del break_counter
