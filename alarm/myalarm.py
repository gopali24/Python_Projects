from pygame import mixer
import time
def sound():
    mixer.init()
    tune=int(input("Enter 1 for a beeping alarm\nEnter 2 for army tune\nEnter 3 for pop tune: "))
    if(tune==1):
       mixer.music.load("alarmbeep.mp3")
    elif(tune==2):
        mixer.music.load("alarmarmy.mp3")
    elif(tune==3):
        mixer.music.load("pop.mp3")
    else:
        print("INVALID INPUT")
    
def alarm():
    hr = int(input('Enter the Hour '))
    mn = int(input('Enter the Minutes '))
    sc = int(input('Enter the Seconds '))
    print('Alarm set for ' + str(hr) +":"+ str(mn) +":"+ str(sc))
    n=int(input("Enter the snooze duration: "))
    sound()
    while True:
        if (time.localtime().tm_hour == hr and time.localtime().tm_min == mn and time.localtime().tm_sec == sc):
            print('Your alarm is now ringing')
            break
    
    while True:
        mixer.music.play()
        l=input("To snooze the alarm press s \nTo stop the alarm press any key\n=>")
        if (l=='s'):
            mixer.music.pause()
            time.sleep(n)
            mixer.music.rewind()
        else:
            mixer.music.stop()
            break
alarm()

