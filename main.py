import os
"""Script down below"""
SUDO_PASSWORD = ""
COMMAND = "apt-get update -y"
os.system('echo %s|sudo -S %s' % (SUDO_PASSWORD, COMMAND))
COMMAND = "apt-get upgrade -y"
os.system('echo %s|sudo -S %s' % (SUDO_PASSWORD, COMMAND))
