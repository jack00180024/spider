from multiprocessing import Process
import os

var = "outside"

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    global var
    info('function f')
    var = "inside"
    print var
    print 'hello', name

if __name__ == '__main__':
    info('main line')
    print var
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    print var
    
    
import threading
import time
 
counter = 0
mutex = threading.Lock()

weather = 0
mutexWeather = threading.Lock()

clock = ""
mutexClock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global counter, mutex
        time.sleep(1);
        if mutex.acquire():
            counter += 1
            print "I am %s, set counter:%s" % (self.name, counter)
            mutex.release()
import datetime            
class getClockInfoThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global clock, mutexClock
        
        while True:
            if mutexClock.acquire():
                # clock = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                clock = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                mutexClock.release()
                time.sleep(1)
            
class getWeatherInfoThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global weather, mutexWeather
        
        while True:
            if mutexWeather.acquire():
                weather += 1
                mutexWeather.release()
            time.sleep(15)

import os

import curses

IMG_1 = '''    **
    **
    **
    **
    **
    **
    **
    **
    **
    **'''

   
IMG_2 = '''*******
*******
     **
     **
*******
*******
**
**
*******
*******'''
   
IMG_3 = '''*******
*******
     **
     **
*******
*******
     **
     **
*******
*******'''
   
IMG_4 = '''**  **
**  **
**  **
**  **
*******
*******
    **
    **
    **
    **'''
   
   
IMG_5 = '''*******
*******
**
**
*******
*******
     **
     **
*******
*******'''
   
   
IMG_6 = '''*******
*******
**
**
*******
*******
**   **
**   **
*******
*******'''
   
   
IMG_7 = '''*******
*******
    **
    **
   **
   **
  **
  **
 **
 **'''
   
   
IMG_8 = '''*******
*******
**   **
**   **
*******
*******
**   **
**   **
*******
*******'''
   
   
IMG_9 = '''*******
*******
**   **
**   **
*******
*******
     **
     **
*******
*******'''
   
   
   
IMG_0 = '''*******
*******
**   **
**   **
**   **
**   **
**   **
**   **
*******
*******'''

IMG_EMPTY = '''       
       
       
       
       
       
       
       
       
       '''

IMG_SEP = '''

**
**


**
**'''


IMG_NUM = [IMG_0, IMG_1, IMG_2, IMG_3, IMG_4, IMG_5, IMG_6, IMG_7, IMG_8, IMG_9]
   
import commands
   

def refresh():
    if mutexWeather.acquire() and mutexClock.acquire():
        os.system('cls')
        print("abcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg\n%d\n%s"%(weather, clock))
        mutexClock.release()
        mutexWeather.release()

        
date = ""
hour1 = -1
hour2 = -1
Minute1 = -1
Minute2 = -1

mutexTime = threading.Lock()



class getTimerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global date, hour1, hour2, Minute1, Minute2, mutexTime
        while True:
            time.sleep(1)
            if mutexTime.acquire():
                strTimer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                date = strTimer.split(" ")[0]
                clock = strTimer.split(" ")[1]
                hour1 = int(clock.split(":")[0]) / 10
                hour2 = int(clock.split(":")[0]) % 10
                
                Minute1 = int(clock.split(":")[1]) / 10
                Minute2 = int(clock.split(":")[1]) % 10
                mutexTime.release()
            
def showClock():
    ''' clock window is a 39 * 12 zone with broader
    this is a example of clock window zone
    every digit number of clock time takes place of 7*10
    the date area takes place of 10*1
                                           
         **  *******      ******* *******  
         **  *******      ******* *******  
         **  **       **       **     **   
         **  **       **       **     **   
         **  *******      *******    **    
         **  *******      *******    **    
         **       **  **       **   **     
         **       **  **       **   **     
         **  *******      *******  **      
         **  *******      *******  **      
                                           
                    2018-10-31             
                                           
    '''
    # strTimer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    # date = strTimer.split(" ")[0]
    # clock = strTimer.split(" ")[1]
    # hour1 = int(clock.split(":")[0]) / 10
    # hour2 = int(clock.split(":")[0]) % 10
    
    # Minute1 = int(clock.split(":")[1]) / 10
    # Minute2 = int(clock.split(":")[1]) % 10
    winHour1.addstr(0, 0, IMG_EMPTY, curses.A_BOLD)
    winHour1.addstr(0, 0, IMG_NUM[hour1], curses.A_BOLD)
    winHour1.refresh()
    
    winHour2.addstr(0, 0, IMG_EMPTY, curses.A_BOLD)
    winHour2.addstr(0, 0, IMG_NUM[hour2], curses.A_BOLD)
    winHour2.refresh()

    winSep.addstr(0, 0, IMG_SEP, curses.A_BOLD)
    winSep.refresh()
    
    winMinute1.addstr(0, 0, IMG_EMPTY, curses.A_BOLD)
    winMinute1.addstr(0, 0, IMG_NUM[Minute1], curses.A_BOLD)
    winMinute1.refresh()
    
    winMinute2.addstr(0, 0, IMG_EMPTY, curses.A_BOLD)
    winMinute2.addstr(0, 0, IMG_NUM[Minute2], curses.A_BOLD)
    winMinute2.refresh()
    
    winDate.addstr(0, 0, date, curses.A_BOLD)
    winDate.refresh()

    
def showWeather():
    pass
    


workSpaceEmptyStr = (" " * 156 + "\n") * 38 + " " * 156
workSpaceStr = "please input your command: "



workSpaceMenu = '''This is the main menu:
<1> get a random number\n
<2> choice 2\n
<3> choice 3\n
<4> choice 4\n
<5> choice 5\n
<6> choice 6\n
<7> choice 7\n
make a choice or input a command: 
'''
def showWorkspace():
    global workSpaceStr
    size = len(workSpaceStr.split("\n"))
    if size > 39:
        workSpaceStr = "\n".join(workSpaceStr.split("\n")[-39:])
    winWorkZone.addstr(1, 0, workSpaceEmptyStr, curses.A_BOLD)
    
    winWorkZone.addstr(1, 0, workSpaceStr, curses.A_BOLD)
    winWorkZone.refresh()
    
    
def monitorRefresh():
    showClock()
    showWeather()
    # showWorkspace()
    
import random
    
class monitorRefreshThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        while True:
            monitorRefresh()
            time.sleep(1)

 
if __name__ == "__main__":
    if 0:
        thread_list = []
        
        threadWeather = getWeatherInfoThread()
        thread_list.append(threadWeather)
        
        threadClock = getClockInfoThread()
        thread_list.append(threadClock)
        # for i in range(0, 100):
            # my_thread = MyThread()
            # thread_list.append(my_thread)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        
        # for t in thread_list:
            # t.join()
        n = 5
        while n > 0:
            n -= 1
            refresh()
            time.sleep(5)
    

        
        # for t in thread_list:
            # t.join()

            
            
            

    stdscr = curses.initscr()
    # stdscr.addstr(0, 0, "testing by Jack", curses.A_BOLD)
    # stdscr.refresh()
    
    
    HEIGHT = 10; WIDTH = 8

    clockZone_x = 118; clockZone_y = 0
    winClockZone = curses.newwin(HEIGHT + 4, WIDTH * 4 + 7, clockZone_y, clockZone_x)
    winClockZone.box()
    winClockZone.refresh()
    
    winHour1 = curses.newwin(HEIGHT, WIDTH, clockZone_y + 1, clockZone_x + 1)
    winHour2 = curses.newwin(HEIGHT, WIDTH, clockZone_y + 1, clockZone_x + 1 + WIDTH)
    winSep = curses.newwin(HEIGHT, WIDTH, clockZone_y + 1, clockZone_x + 1 + WIDTH*2 + 1)
    winMinute1 = curses.newwin(HEIGHT, WIDTH, clockZone_y + 1, clockZone_x + 1 + WIDTH*2 + 5)
    winMinute2 = curses.newwin(HEIGHT, WIDTH, clockZone_y + 1, clockZone_x + 1 + WIDTH*3 + 5)
    winDate = curses.newwin(1, 11, clockZone_y + HEIGHT + 3 - 1, clockZone_x + WIDTH*2)

    weatherZone_x = 108; weatherZone_y = 0
    winWeatherZone = curses.newwin(HEIGHT + 4, 10, weatherZone_y, weatherZone_x)
    winWeatherZone.box()
    winWeatherZone.refresh()


    WorkZone_x = 0; workZone_y = 14
    winWorkZone = curses.newwin(40, 157, workZone_y, WorkZone_x)
    winWorkZone.box()
    winWorkZone.refresh()
    
    showWorkspace()
    
    
    
    if 1:
        thread_list = []
        
        threadTimer = getTimerThread()
        thread_list.append(threadTimer)

        threadRefresh = monitorRefreshThread()
        thread_list.append(threadRefresh)
        
        # threadClock = getClockInfoThread()
        # thread_list.append(threadClock)
        # for i in range(0, 100):
            # my_thread = MyThread()
            # thread_list.append(my_thread)
        for t in thread_list:
            t.setDaemon(True)
            t.start()

    
    while True:
        strInput = winWorkZone.getstr()

        print("|%s|"%strInput)
        if strInput == "quit":
            break
        elif strInput == "":
            os.popen("\n")
            workSpaceStr += "\n" + workSpaceMenu
        elif strInput == "1":
            workSpaceStr += "\nyou have a random number(between 1 to 100) -- %d\n"%random.randint(1, 100)
        else:
            response = os.popen(strInput)
            
            workSpaceStr = workSpaceStr + strInput + "\n"

            # winWorkZone.addstr(response.read(), curses.A_BOLD)
            for line in response.readlines():
                while len(line) > 156:
                    workSpaceStr = workSpaceStr + line[:156] + "\n"
                    line = line[156:]
                workSpaceStr = workSpaceStr + line
            
        showWorkspace()    
            
    # win.addstr(" testing by Jack", curses.A_BOLD)
    # win.refresh()
    # time.sleep(3)