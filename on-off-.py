##############################################
#####        Import modules   ################
############################################## 
import platform
import time
import os,sys
from sys import argv
import glob
##############################################
##### Get System root function################
############################################## 
def get_root():
    path = sys.executable
    while os.path.split(path)[1]:
        path = os.path.split(path)[0]
    return path

##############################################
#####    Get file location       #############
############################################## 
def appear():
    now = str(os.path.abspath(__file__))
    now = now.split("/")
    row = now[0:-1]
    lash = ["/" + one for one in row]
    lash = "".join(lash)
    return lash
default = appear()
##############################################
##### Same line message class#################
##############################################
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

def progress(act, tot):
    sys.stdout.write("\r Current progress %d percent" % ((act*100.0) / tot))
    sys.stdout.write(".")
    time.sleep(0.3)
##############################################
##### confirm function waiting for enter #####
##############################################
def confirm(system):
    print "Your system was detected as %s" % system
    print "Press Enter to continue..."
    raw_input("or Ctrl Z to cancel...")
##############################################
##### Global Variables 1 #####################
##############################################
uname = platform.platform()
uname = uname.lower()
tot = 0
act = 0
##############################################
#####   Class initiate   #####################
##############################################
sys.stdout = Unbuffered(sys.stdout)
##############################################
##### Edit file function #####################
##############################################
def fileedit(editfile, command):
    act = -1
    print "Setting up start up script"
    with open(editfile) as a:
        lines = a.read().splitlines()
        tot = len(lines)
        if command not in lines:
            if editfile == "rc.local":
                searchline = 'exit 0'
                i = lines.index(searchline)
                lines.insert(i, command)
                os.chdir(get_root() + "/tmp/")
                with open("rc.local", 'w') as a:
                    for line in lines:
                        a.write(line+'\n') 
                        act+=1
                        progress(act, tot)
                mo =  rot+"mv "+get_root()+"/tmp/rc.local"+" "+edit_location
                print "[DONE]"
                os.system(mo)
                time.sleep(5)
                os.system("sudo chown root /etc/rc.local")
                os.system("sudo chmod 755 /etc/rc.local")
                
            else:
                lines.insert(1, command)
                print "Setting up start up script"
                with open(editfile, 'w') as a:
                    for line in lines:
                        a.write(line+'\n') 
                        #act+=1
                        print "Altering startup configuration"
                        #progress(act, tot)
                print "[DONE]"
        else:
            print "script already exists!"
##############################################
##### Check file existence function ##########
##############################################
def open_if_not_exists(efile, location):
    os.chdir(location)
    try:
        fd = os.open(efile, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError, e:
        if e.errno == 17:
            fileedit(efile, command)
        else:
            pass#raise
    else:
        fo = os.fdopen(fd, 'w')
        sys.stdout.write("\r Creating new startup configuration file")
        fo.write(command)
        fo.close()
        time.sleep(0.5)
        print "[DONE]"

if "debian" in uname:
##############################################
###  actions required for install in OSMC  ###
##############################################
    confirm("debian")
    print "it equals Debian based system"
    sytem = "debian"
    command = "sudo python /usr/local/bin/button/button.py"
    script_location = get_root() + "/usr/local/bin/button/"
    edit_location = get_root() + "/etc/"
    efile = "rc.local"
    rot = "sudo "
    library ="#sys.path.append('/usr/local/bin/button/RPi')\n"
elif "glibc" in uname:
##############################################
#####actions required for install in *ELEC ###
##############################################
    confirm("Elec")
    print "it equals ELECbased system"
    system = "elec"
    command = "(python /storage/scripts/button.py)&"
    script_location = get_root() + "/storage/scripts/"
    edit_location = get_root() + "/storage/.config/"
    efile = "autostart.sh"
    rot = ""
    library ="#sys.path.append('/storage/scripts/RPi')\n"
elif "dora" in uname:
##############################################
##actions required for install fedora os ##
##############################################
    confirm("Fedora")
    print "Wooohoo we detected Fedora based OS"
    sytem = "fedora"
    command = "sudo python /usr/local/bin/button/button.py"
    script_location = get_root() + "/usr/local/bin/button/"
    edit_location = get_root() + "/etc/"
    efile = "rc.local"
    rot = "sudo "
    library ="#sys.path.append('/usr/local/bin/button/RPi')\n"
elif "XXXXX" in uname:
##############################################
##actions required for install Another os ####
##############################################
    confirm("debian")
    print "Wooohoo we detected XXXXX based OS"
    sytem = "fedora"
    command = "sudo python /usr/local/bin/button/button.py"
    script_location = get_root() + "/usr/local/bin/button/"
    edit_location = get_root() + "/etc/"
    efile = "rc.local"
    rot = "sudo "
    library ="#sys.path.append('/usr/local/bin/button/RPi')\n"
elif "ubuntu" in uname:
##############################################
### actions required for install Ubuntu os ###
##############################################
    confirm("Ubuntu")
    print "Wooohoo we detected Ubuntu based OS"
    sytem = "ubuntu"
    command = "sudo python /usr/local/bin/button/button.py"
    script_location = get_root() + "/usr/local/bin/button/"
    edit_location = get_root() + "/etc/"
    efile = "rc.local"
    rot = "sudo "
    library ="#sys.path.append('/usr/local/bin/button/RPi')\n"
else:
##############################################
##actions required for Else condition   ######
##############################################
    confirm("Unknown")
    print "not supported system detected"
    print "please contact administrator"
    time.sleep(2)
    exit()
##############################################
######    System alteration           ########
##############################################
if not os.path.exists(script_location):
    os.system(rot+"mkdir "+script_location)
os.chdir(script_location)
os.system(rot+"wget http://joural.wz.cz/joural/gpio.tar.gz")
os.system(rot+"tar -xzf gpio.tar.gz -C"+ script_location)
##############################################
######     Create button.py           ########
##############################################
os.chdir(default)
with open(argv[0]) as f:
    section = f.readlines()[245:]
    section.insert(6, library)
    for line in section:
        tot+=1
    os.chdir(get_root() + "/tmp/")
    name = open('button.py', 'w')
    print "Creating script file"
    act = 0
    for line in section:
        name.write(line[1:])
        act+=1
        progress(act, tot)
    name.close()
print("[DONE]")
os.system(rot+"mv "+get_root()+"/tmp/button.py "+script_location)
##############################################
######    System alteration           ########
##############################################
os.chdir(edit_location)
open_if_not_exists(efile, edit_location)
##############################################
######    Clean up temp files         ########
##############################################
os.chdir(script_location)
##for filename in glob.glob(appear() +"/gpio*"):
    ##remove(filename)
os.system(rot+"rm -f gpio*") 
os.chdir(default)
try:
    #os.remove(argv[0])
    pass
except OSError:
    pass
print "System will now reboot"
time.sleep(1.5)
os.system(rot+"reboot")

##############################################
#########         button.py           ########
##############################################
#import time 
#import os
#import sys

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#PIN = 17
#led = 4
#GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(led, GPIO.OUT)
#GPIO.output(led, True)
#
#def Shutdown():
#    for i in range(0,4):## Run loop numTimes
#        GPIO.output(led,True)##if deosnt work 
#        time.sleep(0.7)## Wait
#        GPIO.output(led,False)##change led to 4 or originaly 26
#        time.sleep(0.3)
#    GPIO.output(led, True)
#    GPIO.cleanup()
#    os.system("sudo shutdown -h now")
#
#def Reboot():
#    for i in range(0,2):## Run loop numTimes
#        GPIO.output(led,True)##if deosnt work 
#        time.sleep(0.7)## Wait
#        GPIO.output(led,False)##change led to 4 or originaly 26
#        time.sleep(1.2)
#    GPIO.output(led, True)
#    GPIO.cleanup()
#    os.system("sudo reboot -h now")
#            
#
#while True:
#    GPIO.wait_for_edge(PIN, GPIO.FALLING)
#    start = time.time()
#    time.sleep(0.2)
#    while GPIO.input(PIN) == GPIO.LOW:
#        time.sleep(0.01)
#    lengh = time.time() - start
#    if lengh >= 3:
#        # Long Press function"
#        Shutdown()
#    else:
#        # Short Press function"
#        Reboot()
