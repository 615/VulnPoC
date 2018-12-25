#!/usr/bin/env python
# -*- coding: utf_8 -*-

import sys
import os
import logging
import time
from settings import urlconfig
sys.dont_write_bytecode = True

def initoptions(args):
    urlconfig.url=[]
    guideRegister(args)


def guideRegister(args):
    input_url = raw_input("[1]Plz input url:")
    urlconfig.url.append(input_url)