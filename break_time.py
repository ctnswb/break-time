import time
import webbrowser


number_of_breaks = 3
work_interval = 2*60*60  # length of work period in seconds

counter = 1
print("This work session started at "+time.ctime())
while(counter <= number_of_breaks ):
    time.sleep(work_interval)
    print("Break Started at "+time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=ssdgFoHLwnk")
    counter = counter +1
print("This work session ended at "+time.ctime())
