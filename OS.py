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
