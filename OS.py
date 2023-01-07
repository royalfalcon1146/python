# Kill an application
import os

# Getting the pid of an application by going to details in task manager
def close_program(pid):
    try:
        os.kill(pid, 9)
    except OSError:
        print("Unable to close program with PID {}".format(pid))

# Example usage
close_program(1234)

#--------------------------------------------------------------------------------------------------

# Executing a command in cmd from python
import os
cmd = "shutdown/p" #here is where you write your code in the double quotes
subprocess.run(cmd, shell=True)
