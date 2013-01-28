#!/usr/bin/env python
####################################################################
# File Name :
# Purpose :
# Created By :  Raghuram Onti Srinivasan
# Email         raghuramos1987@gmail.com
####################################################################
import os,sys,shutil
import os.path as path
import commands
import glob

import logging
import optparse

LOGGING_LEVELS = {'critical': logging.CRITICAL,
                  'error': logging.ERROR,
                  'warning': logging.WARNING,
                  'info': logging.INFO,
                  'debug': logging.DEBUG}

def checkCreated(line, name):
    return line.split(':')[-1]

def getNum(strIn):
    outL = []
    for word in strIn.split():
        try:
            outL.append(str(float(word)))
        except ValueError:
            continue
    return outL

os.chdir('data')
fp = open(sys.argv[1], 'w')
for f in glob.glob("*.cpp"):
    fp.write("%s;%s;"%(f.split('-')[0], f.split('-')[-1]))
    print f.split('-')[0], f.split('-')[-1]
    if f.endswith('Moon.cpp'):
        strOrig = commands.getoutput('./fallMoon.exe < ../inp.txt')
    if f.endswith('Dist.cpp'):
        strOrig = commands.getoutput('./projectileDist.exe < ../inp.txt')
    strOrig = ' '.join(getNum(strOrig))
    #strOrig = strOrig.replace(' ', '')
    #strOrig = strOrig.replace('\n','')
    commands.getoutput('rm a.out')
    strOut = commands.getoutput('g++ "%s"'%f)
    if 'error' in strOut:
        fp.write("No;No\n")
        print "Did not compile!!!"
        continue
    else:
        fp.write("Yes;")
    strOut = commands.getoutput('./a.out < ../inp.txt')
    strOut = ' '.join(getNum(strOut))
    #strOut = strOut.replace(' ','')
    #strOut = strOut.replace('\n','')
    if strOut == strOrig:
        fp.write("Yes")
        print "Compiled and Executed correctly!!!"
    else:
        fp.write(strOut)
        print "No correct output for %s: %s"%(f, strOut)
    fp.write('\n')
fp.close()

def main():
    parser = optparse.OptionParser()
    parser.add_option('-l', '--logging-level', help='Logging level')
    parser.add_option('-f', '--logging-file', help='Logging file name')
    (options, args) = parser.parse_args()
    logging_level = LOGGING_LEVELS.get(options.logging_level, logging.NOTSET)
    logging.basicConfig(level=logging_level, filename=options.logging_file,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
