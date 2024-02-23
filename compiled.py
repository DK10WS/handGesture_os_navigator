from last import camera
import subprocess
from gtts import gTTS
import os
from datetime import datetime


def tts(text):
    language= "en"
    
    speech = gTTS(text=text,lang=language, slow=False, tld= "co.uk")
    speech.save("Temp.mp3")
    vlc_command=["cvlc","--play-and-exit","--no-loop","Temp.mp3"]
    subprocess.run(vlc_command)

def selection():
        while True:
            try:
                option = camera()
                if option is not None:
                    tts(f"Your selection is {str(option)}")
                    return option

            except:
                print("No input")

def get_battery_percentage():
    try:
        with open('/sys/class/power_supply/BAT1/capacity', 'r') as file:
            battery_percentage = int(file.read().strip())
            return battery_percentage
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        tts("Welcome where do you want to start")
        tts("For opening a app hold 1")
        tts("For increasing or decreasing volume hold 2")
        tts("For turning the wifi on or off hold 3")
        tts("For checking battery percentage hold 4")
        tts("For current time and date hold 5")
        tts("To exit hold 0")   

        choice= selection()
        
        if (choice==1):
            tts("Which app would you like to choose")
            tts("For Browser hold 1")
            tts("For music hold 2")
            tts("For Messages hold 3")
            tts("To go back hold 4")
            tts("To exit hold 0")

            app= selection()
            if (app==1):
                os.system("firefox")
                
            if (app==2):
                os.system("flatpak run com.spotify.Client")
                
            if (app ==3):
               os.system("flatpak run org.telegram.desktop")

            if (app==4):
                main()
                
            if (app==0):
                break

        if (choice==2):
            tts("To increase volume hold 1")
            tts("TO decrease volume hold 2")
            tts("To mute hold 3")
            tts("To unmute hold 4")
            tts("To return hold 5")
            tts("To exit hold 0")

            volume= selection()
            if (volume==1):
                os.system("pactl set-sink-volume @DEFAULT_SINK@ +50%")
                tts("Test volume")
            if (volume==2):
                os.system("pactl set-sink-volume @DEFAULT_SINK@ -25%")
                tts("Test volume")
            if (volume==3):
                os.system("pactl set-sink-volume @DEFAULT_SINK@ 0%")
                tts("Test volume")
            if (volume==4):
                os.system("pactl set-sink-volume @DEFAULT_SINK@ 50%")
                tts("Test volume")
            if (volume==5):
                main()
            if (volume==0):
                break
            
        if choice== 3:
            tts("To turn off hold 1")
            tts("To turn on hold 2")
            tts("to return hold 3")
            tts("to exit hold 4")

            wifi= selection()

            if (wifi==1):
                os.system("nmcli radio wifi off")

            if (wifi==2):
                os.system("nmcli radio wifi on")
            
            if (wifi==3):
                main()
            if(wifi==0):
                break

        if (choice==4):
        
            battery_percentage = get_battery_percentage()
        
            if battery_percentage is not None:
                tts(f"Battery Percentage: {battery_percentage}%")
            else:
                tts("Failed to retrieve battery percentage.")

        if (choice==5):
            date= datetime.now()
            date_time_string = date.strftime("%A, %B %d, %Y %I:%M %p")
            tts(str(date_time_string))

        if(choice==0):
            break
main()
