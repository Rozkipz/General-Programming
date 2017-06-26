from threading import Thread, Condition
import logging
from time import sleep
from random import randint, choice


class WheelState:
    def __init__(self):
        self.Working, self.Blocked, self.Freewheeling, self.Sinking = range(4)
        """Initialises wheel height to lower."""
        self.WheelHeight = 0

    def changeWheelHeight(self, newHeight):
        # Function to change the wheel height.
        self.WheelHeight = newHeight

    def returnRandomValue(self):
        # Returns a random value from our enum.
        return choice([self.Working, self.Blocked, self.Freewheeling, self.Sinking])


def wheelfunction(wheelnum):
    # Make the variables global so they can be used between threads.
    global currentdistance
    global blockedwheels

    # Selects wheel from the array of wheels

    wheel = p[wheelnum]
    logging.info('Thread {0}.'.format(wheelnum+1))

    # Returns a random problem/working for the wheel.
    randvalue = wheel.returnRandomValue()

    if len(blockedwheels) >= 2:
        # Checks if the array of broken wheels has 2 or more wheels in.
        logging.info('Two wheels stuck at once, contacting control.')

        if choice([True, False]):
            # 50/50 chance of being fixed by control, clearing the blocked array.
            logging.info('Control fixed all problems, all wheels working.')
            blockedwheels = []
        else:
            logging.info('Control couldn\'t fix the problem this time.')
        return
    
    if choice([True, False]):
        # 50/50 chance of the problem being to complicated to fix.
        logging.info('Problem too complicated, contacting control for wheel {0}.'.format(wheelnum+1))
        if choice([True, False]):
            # 50/50 chance that control can fix it.
            randwheelnum = choice([0, 1])
            logging.info('Control managed to fix it by changing wheel to {0}'.format(randwheelnum))
            wheel.changeWheelHeight(randwheelnum)
            # Randomly assigns wheel height from control.
        else:
            logging.info('Control unable to fix wheel')
            blockedwheels.append(wheelnum)
            # Adds wheel to list of blocked wheels.
            
    elif randvalue == 0:
        # Check if wheel is working correctly.
        logging.info('Random problem: Working.')
        logging.info('Not changing WheelHeight for wheel {0}, current value: {1}'.format(wheelnum+1, wheel.WheelHeight))
        currentdistance += traveldistance
        # Go forward a travel distance (1m)
        logging.info('Adding {0} to the distance travelled. Total distance is now {1}'.format(traveldistance, currentdistance))
        
    elif randvalue == 1:
        # Check if wheel is blocked.
        logging.info('Random problem: Blocked.')
        wheel.changeWheelHeight(1)
        # Lift wheel.
        logging.info('Change WheelHeight to 1 for wheel {0}.'.format(wheelnum+1))
        
    elif randvalue == 2:
        # Check if wheel is free wheeling.
        logging.info('Random problem: FreeWheeling.')
        wheel.changeWheelHeight(0)
        # Lower wheel
        logging.info('Change WheelHeight to 0 for wheel {0}.'.format(wheelnum+1))
        
    elif randvalue == 3:
        # Check if the wheel is sinking.
        logging.info('Random problem: Sinking.')
        wheel.changeWheelHeight(1)
        # Raise the wheel.
        logging.info('Change WheelHeight to 1 for wheel {0}.'.format(wheelnum+1))


def wheel1(cv):
    global currentdistance
    # global maxdistance
    while currentdistance <= maxdistance:
        # Check if the max distance has been reached.
        cv.acquire()
        # Acquire the lock.
        wheelfunction(0)
        # Run the wheel function.
        cv.release()
        # Release the CV.
        sleep(.3)
        # Sleep so that this thread doesn't pick up the CV again immediately.


def wheel2(cv):
    global currentdistance
    while currentdistance <= maxdistance:
        cv.acquire()
        wheelfunction(1)
        cv.release()
        sleep(.3)


def wheel3(cv):
    global currentdistance
    while currentdistance <= maxdistance:
        cv.acquire()
        wheelfunction(2)
        cv.release()
        sleep(.3)


def wheel4(cv):
    global currentdistance
    while currentdistance <= maxdistance:
        cv.acquire()
        wheelfunction(3)
        cv.release()
        sleep(.3)


def wheel5(cv):
    global currentdistance
    while currentdistance <= maxdistance:
        cv.acquire()
        wheelfunction(4)
        cv.release()
        sleep(.3)


def wheel6(cv):
    global currentdistance
    while currentdistance <= maxdistance:
        cv.acquire()
        wheelfunction(5)
        cv.release()
        sleep(.3)


######################### Setup Logging #########################
logger = logging.getLogger()                                    #
fileHandler = logging.FileHandler('./mars_rover_project.log')   #
formatting = logging.Formatter('%(asctime)s %(message)s')       #
fileHandler.setFormatter(formatting)                            #
logger.addHandler(fileHandler)                                  #
logger.setLevel(logging.INFO)                                   #
#################################################################


cvariable = Condition()
maxdistance = 200
traveldistance = 1
currentdistance = 0
control = randint(1, 6)
blockedwheels = []

p = [WheelState(), WheelState(), WheelState(), WheelState(), WheelState(), WheelState()]

print "Please check the log file found at ./mars_rover_project.log."

Thread(target=wheel1, args=(cvariable,)).start()
Thread(target=wheel2, args=(cvariable,)).start()
Thread(target=wheel3, args=(cvariable,)).start()
Thread(target=wheel4, args=(cvariable,)).start()
Thread(target=wheel5, args=(cvariable,)).start()
Thread(target=wheel6, args=(cvariable,)).start()
