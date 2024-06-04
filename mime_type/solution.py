import sys
import math
import os

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mimes = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimes.update({ext.lower():mt})

print(mimes,file=sys.stderr,flush=True)

for i in range(q):
    fname = input()  # One file name per line.
    basename,ext = os.path.splitext("x"+fname)
    ext = ext.lower()[1:11]
    print(fname,">>> Ext:["+ext+"]",file=sys.stderr,flush=True)
    mime = "UNKNOWN"
    if ext in mimes.keys():
        mime = mimes.get(ext)
    print(mime)

