import time
import webbrowser

total_break = 3
count = 0

print("This program started at" + time.ctime())
while(count < total_break):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=WWC5ee4Fl7o&list=PLyDfKTaPXoZjDvRYckZQydrF4GvozE5Ia")
	count = count + 1
