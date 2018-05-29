__author__ = "Kealdor"
__date__ = "$May 28, 2018 8:27:00 PM$"

from sys import platform as _platform
import subprocess
import os
#import psutil

#Set path to MTGA
MTGA_Path = ''

#if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    # linux &  # MAC OS X
    #print ("Not Supported yet")

#For windows it assumes MTGA is installed to its default location

if _platform == "win32":
    # Windows
    MTGA_Path = os.getenv("ProgramFiles") + "\\Wizards of the Coast\\MTGA\\Mtga.exe"
   
if _platform == "win64":
    # Windows 64-bit
    MTGA_Path = os.getenv("ProgramFiles(x86)") + "\\Wizards of the Coast\\MTGA\\Mtga.exe"

#Set path to MTGA Tracker
MTGA_Tracker_Path = ''

#if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    # linux &  # MAC OS X
    #print ("Not Supported yet")
    
if _platform == "win32" or _platform == "win64":
    # Windows
    MTGA_Tracker_Path = os.getenv("USERPROFILE") + "\\AppData\\Local\\mtgatracker\\MTGATracker.exe"
   
#Run The Exe's
os.system(MTGA_Path)
os.system(MTGA_Tracker_Path)

#Close The Exe's when needed
#Shards fix to work alot better 5/29/2018 at 11:30am
prog = [line.split() for line in subprocess.check_output("tasklist").splitlines()]
del prog[0]
prog = [i[0].decode("utf-8") for i in prog]

if not 'MTGA.exe' in prog:
    if _platform == "win32" or _platform == "win64":
        os.system("TASKKILL /F /IM MTGATracker.exe")
    #if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
            #for pid in (process.pid for process in psutil.process_iter() if process.name()=="MTGATracker.exe"):
                #os.kill(pid)
