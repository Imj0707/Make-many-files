#!/bin/sh

import os

for n in range(10):
    os.system('mkdir anotherone' + str(n))
    n += 1
