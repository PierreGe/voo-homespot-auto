#!bin/python
# -*- coding: utf8 -*-


import main
import daemon

# running this script will create a daemon (program running in the background)

with daemon.DaemonContext():
    main.main()
