"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${12:04  p.m}
   * package - ${PACKAGE_NAME}
   * Title - Write a Stopwatch Program for measuring the time that elapses between the start and end clicks.
"""

import time

class stopwatch :

    # convert Time seconds into minutes and hours
    def time_convert(self,sec,):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        return int(hours), int(mins), float(sec)

    # Run the stopwatch hear
    def stopwatchRun(self):
        input("Press Enter to start\n")
        start_time = time.time()
        try:
            while True:
                end_time = time.time()
                times = self.time_convert(end_time - start_time)
                print("Time = {0} : {1} : {2}".format(times[0], times[1], times[2]))
                time.sleep(1)
        except KeyboardInterrupt:
            time_lapsed = end_time - start_time
            self.time_convert(time_lapsed)
            print("Total Time Lapsed  = {0}:{1}:{2}".format(times[0], times[1], times[2]))
        

# Main method
if __name__ == '__main__':
    # Exception Handling
    try :
        # Creating object of class
        stopwatchObject = stopwatch()
        stopwatchObject.stopwatchRun()
    except :
        print('Exception Raised.')