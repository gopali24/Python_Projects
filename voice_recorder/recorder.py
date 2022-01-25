import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds=30,file="Recording.wav"):
    print("Recording started... ")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file,44100,recording)
    print("Recording Finished")

ch = input("Do you want to enter a predetermined time for your recording:\nEnter Y for yes and N for no: ").lower()
if ch=='y':
    time = int(input("Enter the time in seconds: "))
elif ch=='n':
    ch1 = input("Do you want to select a period of time\n1 for short recording - 10 secs\n2 for a medium recording - 30 sec\n3 for a long recording - 60 sec\nAny other key for a 20 sec recording option\n")
    if ch1=='1':
        time = 10
    elif ch1=='2':
        time = 30
    elif ch1=='3':
        time = 60
    else:
        time = 20
else:
    print("Invalid Option -_-")

ch=input("Do you want to name your recording? Enter Y for yes and N for No: ").lower()
if ch=='y':
    f_name=input("Enter the name for your recording: ")
    f_name+=".wav"
    voice_recorder(time,f_name)
elif ch=='n':
    voice_recorder(time)
else:
    print("Invalid Option -_-")