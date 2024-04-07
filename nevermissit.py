import datetime
import webbrowser
import time

print("Thanks for Downloading!")
print("Never miss iledopapiezowej again with this program! It will open the site at 21:36 so you have time to prepare yourself.")
print("===========================")
def check_time_and_open_website():
    target_time = datetime.time(21, 37) 
    while True:
        current_time = datetime.datetime.now().time()
        print('The time is - ',current_time)
        if current_time.hour == target_time.hour and current_time.minute == target_time.minute:
            webbrowser.open("https://2137.epicsite.xyz/")
            break 
        time.sleep(60)
if __name__ == "__main__":
    check_time_and_open_website()
