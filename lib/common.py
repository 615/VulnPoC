#!/usr/bin/env python
# -*- coding: utf_8 -*-

import os,sys
import urllib,urllib2
import re
import urlparse,random
from settings import Banner

sys.dont_write_bytecode = True
def dataStdout(date):
    message = date
    sys.stdout.write(message)


def banner():
    print random.randint(0,2)
    _ = Banner[random.randint(0,2)]
    dataStdout(_)
