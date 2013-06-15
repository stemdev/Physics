"""
A python script for cleaning up directories after
typsetting LaTeX documents.
"""
import os

logExts = (
        ".aux",
        ".log",
        ".nav",
        ".out",
        ".snm",
        ".toc",
        ".tui",
        ".tmp",
        ".synctex.gz"
)

thisDir = os.getcwd()

count = 0
for root, dirs, files in os.walk(thisDir):
    for x in files:
        if x.endswith(logExts):
            os.remove(os.path.join(root,x))
            count += 1

print(str(count) + ' files cleaned.')
