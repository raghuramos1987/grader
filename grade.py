#!/usr/bin/env python
####################################################################
# File Name :
# Purpose :
# Created By :  Raghuram Onti Srinivasan
# Email         onti@cse.ohio-state.edu
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

os.chdir('data')
for f in glob.glob("*.cpp"):
    print f.split('-')[0], f.split('-')[-1]
    if f.endswith('Feet.cpp'):
        strOrig = commands.getoutput('./fallFeet.exe < inp.txt')
    if f.endswith('Dist.cpp'):
        strOrig = commands.getoutput('./fallDist.exe < inp.txt')
    strOrig = strOrig.replace(' ', '')
    commands.getoutput('rm a.out')
    strOut = commands.getoutput('g++ "%s"'%f)
    if 'Error' in strOut:
        print "Did not compile!!!"
        sys.exit(-1)
    strOut = commands.getoutput('./a.out < inp.txt')
    strOut = strOut.replace(' ','')
    if strOut == strOrig:
        print "Compiled and Executed correctly!!!"
    else:
        print "No correct output for %s: %s"%(f, strOut)


def main():
    parser = optparse.OptionParser()
    parser.add_option('-l', '--logging-level', help='Logging level')
    parser.add_option('-f', '--logging-file', help='Logging file name')
    (options, args) = parser.parse_args()
    logging_level = LOGGING_LEVELS.get(options.logging_level, logging.NOTSET)
    logging.basicConfig(level=logging_level, filename=options.logging_file,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
