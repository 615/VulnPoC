#!/usr/bin/env python
# -*- coding: utf_8 -*-

import subprocess,sys
from datatype import AttribDict

sys.dont_write_bytecode = True

Version = "0.0.1"
Os_win = subprocess.mswindows
Author = "m4ng0"
urlconfig = AttribDict()

banner_1 = """\033[01;34m
 _____________________________
< VulnScan Version:%s by %s >
 -----------------------------\033[0m
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||

""" % (Version, Author)

banner_2 = """\033[01;34m
 _____________________________
< VulnScan Version:%s by %s >
 -----------------------------\033[0m
     \033[01;31m\\
      \033[01;33m\\\033[0m
          oO)-.                       .-(Oo
         /__  _\                     /_  __\\
         \  \(  |     ()~()         |  )/  /
          \__|\ |    (-___-)        | /|__/
          '  '--'    ==`-'==        '--'  '

""" %(Version, Author)


banner_3 = """\033[01;34m
_____________________________
< VulnScan Version:%s by %s >
-----------------------------\033[0m
  \033[01;31m\\
    \033[01;33m\\\033[0m
      .--.
     |o_o |
     |:_/ |
    //   \ \\
   (|     | )
   /'\_   _/`\\
   \___)=(___/

""" % (Version, Author)

Banner = [banner_1,banner_2,banner_3]
