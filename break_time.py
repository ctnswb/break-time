import time
import webbrowser

counter = 1
number_of_breaks = 3

print("This program started on "+time.ctime())
while(counter <= number_of_breaks ):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=ssdgFoHLwnk")
    counter = counter +1

    
