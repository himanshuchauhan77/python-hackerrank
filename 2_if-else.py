#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # If n is odd, print Weird
    if n%2!=0:
        print("Weird")
    # If n is even and in the inclusive range of 2 to 5, print Not Weird
    elif 2<=n<=5:
        print("Not Weird")
    # If n is even and in the inclusive range of 6 to 20, print Weird
    elif 6<=n<=20:
        print("Weird")
    # if n is greater than 20
    elif n>20:
        print("Not Weird")
