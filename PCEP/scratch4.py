from platform import *
print(machine())
print(system())
print(processor())
print(platform())
print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())
print(python_version_tuple())

for atr in python_version_tuple():
    print(atr)

dir(platform)

import os
dir(os)



