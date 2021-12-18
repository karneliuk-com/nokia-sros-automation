#!/usr/bin/env python

# Modules
import datetime
import os
from dotenv import load_dotenv
from pysros.management import connect
import re


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

    results = connect_obj.cli("show router route-table | no-more")
    connect_obj.disconnect()

    ## Timestamp: completed
    t2 = datetime.datetime.now()

    ## Printing results
    tl = os.get_terminal_size()
    print(f"{'=' * tl.columns}\nCompleted in {t2 -t1}\n{'=' * tl.columns}\n")

    ## Processing Data
    is_default_route_bool = True if re.search(r'\b0\.0\.0\.0/0\b', results) else False

    num_routes_int = 0
    for line_str in results.splitlines():
        if re.match(r'^No\. of Routes:', line_str):
            num_routes_int = int(re.sub(r'^No\. of Routes: (\d)$', r'\1', line_str))

    print(f"Routes in routing table: {num_routes_int}\nDoes default route exist: {is_default_route_bool}")

    print(f"\n{'=' * tl.columns}\n")
