#!/usr/bin/env python
# -*- coding: utf_8 -*-

import sys
import os,re
from settings import Os_win,Version
from common import banner
from options import initoptions
import argparse


sys.dont_write_bytecode = True


def main():

    # 这里还要在check 基本环境
    argpa = argparse.ArgumentParser(description="A Scan For Network")
    argpa.add_argument("--banner")
    argpa.add_argument("--debug")
    argpa.add_argument("-u",help="Web Url")
    argpa.add_argument("-p",help="Server Port")
    argpa.add_argument("-H",help="Server Host")
    args= argpa.parse_args()
    # arg_dict= arg.__dict__
    # # print arg_dict

    if Os_win:
        print "a"

    banner()

    try:
        initoptions(args)
    except Exception,msg:
        pass



if __name__ == '__main__':
    main()