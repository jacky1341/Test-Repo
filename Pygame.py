import math
import os
import sys
from lib2to3.pgen2.token import GREATER
from urllib import request

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):

    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
