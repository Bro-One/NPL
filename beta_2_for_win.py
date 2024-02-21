from pyOptoSigma import *
import msvcrt
import time

# define functions
def prt_f():
    print("== complete! ==\n")

def prt_l(mode=0):
    list = [0, 0]
    list[0] = stages.get_position()[0] - new_origin[0]
    list[1] = stages.get_position()[1] - new_origin[1]
    if mode == 0:
        print("location = {}".format(list))
    elif mode == 1:
        return list

# define step size
step = 1000  # 1000um = 1mm

# define maximum lengths
max_len_1 = 100000
max_len_2 = 100000

# set connection
stages = Session(Controllers.SHOT_702)
stages.append_stage(Stages.OSMS26_100)
stages.append_stage(Stages.OSMS26_100)
stages.connect("COM3")

msg = '''
****** Ready for keyboard input ******

 press the key below in the direction you want to move. 
        w
    a       d
        s
 r : set current position as new origin.
 i : come back to the absolute origin. (initialize)
 m : move to the target position
 1 : print this message again

 unit = micro-meter (um)
 if you want to exit, press 'q' 
'''

print(msg)
print("****** current location ******")
location = stages.get_position()
print(location)
new_origin = [0, 0]

while True:
    k = msvcrt.getch().decode()  # Decode the byte string to a Unicode string

    if k == 'w':
        print("up")
        if stages.get_position()[0] + step > max_len_1:
            print("out of range!")
            print(msg)
            continue
        else:
            stages.move(stage=1, amount=step, wait_for_finish=True)
            prt_l()
            prt_f()

    elif k == 's':
        print("down")
        if stages.get_position()[0] - step < 0:
            print("out of range!")
            continue
        else:
            stages.move(stage=1, amount=-step, wait_for_finish=True)
            prt_l()
            prt_f()

    elif k == 'd':
        print("right")
        if stages.get_position()[1] + step > max_len_2:
            print("out of range!")
            continue
        else:
            stages.move(stage=2, amount=step, wait_for_finish=True)
            prt_l()
            prt_f()

    elif k == 'a':
        print("left")
        if stages.get_position()[1] - step < 0:
            print("out of range!")
            continue
        else:
            stages.move(stage=2, amount=-step, wait_for_finish=True)
            prt_l()
            prt_f()

    elif k == 'q':
        quit()

    elif k == 'c':
        print("== current location ==")
        print("absolute coord: {}".format(stages.get_position()))
        print("relative coord: {}".format(prt_l(mode=1)))

    elif k == 'i':
        print("== initialize the location ==")
        stages.initialize()
        prt_l()
        prt_f()

    elif k == 'r':
        print("== set current position as new origin ==")
        new_origin = stages.get_position()
        prt_l()
        prt_f()

    elif k == 'm':
        target_x, target_y = input("target position \n((ex) 1000, 1000) : ").split(",")
        target_x = int(target_x)
        target_y = int(target_y)
        stages.move(stage=1, amount=target_x, wait_for_finish=True)
        stages.move(stage=2, amount=target_y, wait_for_finish=True)
        prt_l()

    else:
        print("it is not permitted. press arrow keys to move the stages.")
