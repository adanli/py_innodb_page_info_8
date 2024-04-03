#! /usr/bin/env python
#encoding=utf-8
import mylib
from sys import argv
from mylib import myargv

if __name__ == '__main__':
    myargv = myargv(argv)
    print("argv: %s" % argv)
    mylib.get_innodb_page_type(myargv)
