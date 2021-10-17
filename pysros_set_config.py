#!/usr/bin/env python

# Modules
import datetime
import os
from dotenv import load_dotenv
from pysros.management import connect


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

    r1 = connect_obj.running.get(path="/openconfig-interfaces:interfaces/interface[name=\"loopback\"]")

    # Setting a value (YANG leaf or list-leaf type )
    r2 = connect_obj.candidate.set(path="/openconfig-interfaces:interfaces/interface[name=\"loopback\"]/config/description", value="test configuration")

    # Setting a nested value (YANG container or list)
    r3 = connect_obj.candidate.set(path="/openconfig-interfaces:interfaces/interface[name=\"loopback\"]/subinterfaces/subinterface", value={1: {"config": {"index": 1, "description": "another test", "enabled": True}}})

    r4 = connect_obj.running.get(path="/openconfig-interfaces:interfaces/interface[name=\"loopback\"]")

    connect_obj.disconnect()

    ## Timestamp: completed
    t2 = datetime.datetime.now()

    ## Printing results
    tl = os.get_terminal_size()
    print(f"{'=' * tl.columns}\nCompleted in {t2 -t1}\n{'=' * tl.columns}\n")

    ## Printing collected data
    print(r1)
    print(r2)
    print(r3)
    print(r4)

    print(f"\n{'=' * tl.columns}\n")
