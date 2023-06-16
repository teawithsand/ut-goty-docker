#!/usr/bin/env python3

# This script replaces DetectARCH function in shell.sh and setup.data/apply-patch.sh
# You can do that manually if it didn't work.
import re

target = """
DetectARCH() 
{
    echo "x86"
    return 0
"""

f1 = "ut-436-GOTY/setup.sh"
f2 = "ut-436-GOTY/setup.data/apply-patch.sh"
def patch(c):
    c = re.sub(r"DetectARCH\(\)[\s\S]*?\{", target, c,re.M)
    return c

c1 = patch(open(f1, "rt").read())
c2 = patch(open(f2, "rt").read())
open(f1, "wt").write(c1)
open(f2, "wt").write(c2)
        

