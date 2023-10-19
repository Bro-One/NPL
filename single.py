from pyOptoSigma import *
from getkey import getkey


# This file is for controlling 'single' motorized stage
# DO NOT use IDE

# define functions
def prt_f():
    print("== complete! ==\n")


def prt_l(d):
    d = stages.get_position()
    print("location = {}".format(d))


# define step size
step = 1000
# 1000um = 1mm

# define maximum length
max_len = 85000

# set connection
stages = Session(Controllers.SHOT_702)
stages.append_stage(Stages.OSMS20_85)
stages.connect()

# define location
location = 0

print("****** current location ******")
prt_l(location)

# print(type(location))
msg = '''
****** Ready for keyboard input ******

 press the arrow keys in the direction you want to move. 
 
 r : set current position as new origin.
 i : come back to the origin. (initialize)
 
 unit = micro-meter (um)
 if you want to exit, press 'q' or ctrl + c
'''

print(msg)
while 1:
    key = getkey()
    print("key ={}".format(key))
    if key == keys.UP:
        stages.move(amount=step, wait_for_finish=True)  # 1000um = 1mm
        prt_l(location)
        prt_f()

    elif key == keys.DOWN:
        stages.move(amount=-step, wait_for_finish=True)
        prt_l(location)
        prt_f()

    elif key == 'r':
        print("== set current position as new origin ==")
        stages.reset(mechanical=True)
        prt_l(location)
        prt_f()

    elif key == 'i':
        print("== initialize the location ==")
        stages.initialize()
        prt_l(location)
        prt_f()

    elif key == 'q':
        print("== exit the program ==")
        break
