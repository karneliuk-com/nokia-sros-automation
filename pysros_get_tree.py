#!/usr/bin/env python

# Modules
import datetime
import os
from dotenv import load_dotenv
from pysros.management import connect
from pysros.pprint import printTree


# Body
if __name__ == "__main__":
    ## Get connectivity details
    load_dotenv()
    host={
            "ip_address": os.getenv("NOKIA_IP"),
            "username": os.getenv("NOKIA_USER"),
            "password": os.getenv("NOKIA_PASS")
         }

    ## Get path
    path = '/nokia-conf:configure/card[slot-number="1"]'

    ## Timestamp: started
    t1 = datetime.datetime.now()

    ## Interecting with the device
    connect_obj = connect(host=host["ip_address"], username=host["username"],
                          password=host["password"])

    results = connect_obj.running.get(path)
    connect_obj.disconnect()

    ## Timestamp: completed
    t2 = datetime.datetime.now()

    ## Printing results
    tl = os.get_terminal_size()
    print(f"{'=' * tl.columns}\nCompleted in {t2 -t1}\n{'=' * tl.columns}\n")

    ## Printing collected data
    print(path)
    printTree(results)

    print(f"\n{'=' * tl.columns}\n")
