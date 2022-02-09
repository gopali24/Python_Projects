from speedtest import Speedtest
wifi  = Speedtest()

print("Starting your speedtest...")
down_speed = wifi.download()
up_speed = wifi.upload()

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return "{0:.2f} {1}BPS".format(size, power_labels[n])

print("Wifi Download Speed is ", format_bytes(down_speed))
print("Wifi Upload Speed is ", format_bytes(up_speed))