import glob, os, sys

os.chdir(os.getcwd())
#change the directory to the folder containing the srt files
#you can replace this with a string to the desired folder
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


out = open("input.txt",'w')

def cleanstr(inputstr):
    #occasionally some srt files have the '♪' file
    bad = ['<i>','</i>']
    for item in bad:
        if item in inputstr:
            inputstr = inputstr.replace(item,'')
    inputstr = inputstr.upper()
    return inputstr

for filename in glob.glob("*.srt"):
    f = open(filename,'rt')
    for line in f:
        proc = line.strip()
        if not (RepresentsInt(proc) or "->" in proc):
            proc = cleanstr(proc)
            out.write("{}\n".format(proc))
