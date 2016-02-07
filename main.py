import os
import random
import getpass

x = random.randint(100000000, 1000000000)

os.system("net user {0} {1}".format(getpass.getuser(), x))

print(x)
