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

    ## Timestamp: started
    t1 = datetime.datetime.now()

    ## Interecting with the device
    connect_obj = connect(host=host["ip_address"], username=host["username"],
                          password=host["password"])

    results = connect_obj.running.get("/nokia-conf:configure/card[slot-number=1]")
    connect_obj.disconnect()

    ## Timestamp: completed
    t2 = datetime.datetime.now()

    ## Printing results
    tl = os.get_terminal_size()
    print(f"{'=' * tl.columns}\nCompleted in {t2 -t1}\n{'=' * tl.columns}\n")

    ## Printing collected data
    print(results)
    print(results["admin-state"])

    ## Validating data type
    print(isinstance(results["admin-state"], str))
    print(results["admin-state"] == "enable")

    # Converting data type and re-validating it again
    print(isinstance(str(results["admin-state"]), str))
    print(str(results["admin-state"]) == "enable")

    print(f"\n{'=' * tl.columns}\n")
