#!bin/python
# -*- coding: utf8 -*-

from connectionVOO import ConnectionVOO

import time

def main():
    """ Keep voo homespot connection alive """
    i = 1
    while True:
        try:
            print("Authentification ..")
            connection = ConnectionVOO()
            while True:
                print("Sending request to connect..")
                connection.sendRequest()
                while not connection.isLive():
                    print("Authentification failed ...")
                    connection.sendRequest()
                    time.sleep(3)
                while connection.isLive():
                    print("Connected to internet!")
                    i = 1
                    time.sleep(30)
        except:
            print("Error detected .. retrying in " + str(i) + " seconds")
            time.sleep(i)
            i += 1


if __name__ == '__main__':
    main()
