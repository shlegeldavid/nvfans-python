import os


def give_temp():
    os.system('nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader | tee temp.md')
    with open('temp.md', 'r', encoding='utf-8') as file:
        number = int(file.readline().strip())
    return number


def fanspeed(speed):
    os.system('xhost si:localuser:root')
    os.system(f'sudo /usr/bin/nvidia-settings -a "*:1[gpu:0]/GPUFanControlState=1" -a "*:1[fan-0]/GPUTargetFanSpeed={speed}" -a "*:1[fan-1]/GPUTargetFanSpeed={speed}"')
    os.system('xhost -si:localuser:root')
    print(f'Fanspeed set to: {speed}')
    return


def fan_curve(temperature):
    x = temperature
    if x >= 0 and x <= 41:
        return 40
    return print('OMG!!!')
