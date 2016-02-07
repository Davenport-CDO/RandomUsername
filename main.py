import os
import random
import getpass

x = random.randint(100000, 999999)

os.system("net user {0} {1}".format(getpass.getuser(), x))

print(x)
