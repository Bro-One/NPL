from pyOptoSigma import *
from getkey import getkey, keys


# This file is for controlling 'single' motorized stage
# DO NOT use IDE

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

# print and get a current position

# define step size
step = 1000
# 1000um = 1mm

# define maximum lengthr
max_len_1 = 100000
max_len_2 = 100000
# set connection
stages = Session(Controllers.SHOT_702)
stages.append_stage(Stages.OSMS26_100)
stages.append_stage(Stages.OSMS26_100)
stages.connect()

# initialize
#print("****** initialize the location ******")
#stages.initialize()

# define location

msg = '''
****** Ready for keyboard input ******

 press the arrow keys in the direction you want to move. 
 
 r : set current position as new origin.
 i : come back to the absolute origin. (initialize)
 m : move to the target position
 1 : print this message again
 
 unit = micro-meter (um)
 if you want to exit, press 'q' or ctrl + c
'''

print(msg)
print("****** current location ******")
location = stages.get_position()
print(location)

new_origin = [0, 0]
while 1:
    key = getkey()
    print("key ={}".format(key))
    # control the stage 1 (vertical)
    if key == keys.UP:
        if stages.get_position()[0] + step > max_len_1:
            print("out of range!")
            print(msg)
            continue
        else:
            stages.move(stage=1, amount=step, wait_for_finish=True)  # 1000um = 1mm
            prt_l()
            prt_f()

    elif key == keys.DOWN:
        # print("location - step = ", stages.get_position()[0] - step)
        if stages.get_position()[0] - step < 0:
            print("out of range!")
            continue
        else:
            stages.move(stage=1, amount=-step, wait_for_finish=True)
            prt_l()
            prt_f()
    # control the stage 2 (horizontal)
    elif key == keys.RIGHT:
        if stages.get_position()[1] + step > max_len_2:
            print("out of range!")
            continue
        else:
            stages.move(stage=2, amount=step, wait_for_finish=True)
            prt_l()
            prt_f()
    elif key == keys.LEFT:
        if stages.get_position()[1] - step < 0:
            print("out of range!")
            continue
        else:
            stages.move(stage=2, amount=-step, wait_for_finish=True)
            prt_l()
            prt_f()
    elif key == 'm':
        target_x, target_y = input("target position \n((ex) 1000, 1000) : ").split(",")
        target_x = int(target_x)
        target_y = int(target_y)
        stages.move(stage=1,amount=target_x, wait_for_finish=True)
        stages.move(stage=2,amount=target_y, wait_for_finish=True)
        prt_l()
    elif key == "c":
        print("== current location ==")
        print("absolute coord: {}".format(stages.get_position()))
        print("relative coord: {}".format(prt_l(mode=1)))

    elif key == 'r':
        print("== set current position as new origin ==")
        new_origin = stages.get_position()
        prt_l()
        prt_f()

    elif key == 'i':
        print("== initialize the location ==")
        stages.initialize()
        prt_l()
        prt_f()

    elif key == 'q':
        print("== exit the program ==")
        break

    elif key == '1':
        print(msg)

    else:
        print("It is not permitted. if you want to see notification. please press 1")
        continue
