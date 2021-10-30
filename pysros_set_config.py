#!/usr/bin/env python

# Modules
import datetime
import os
from dotenv import load_dotenv
from pysros.management import connect
from pysros.pprint import printTree


# Variables
xpath = "/openconfig-interfaces:interfaces/interface[name=\"loopback\"]"
yang_container_value = {
                            "config": {
                                "name": "loopback",
                                "type": "softwareLoopback",
                                "description": "test-pysros-loopback",
                                "enabled": True
                            },
                            "subinterfaces": {
                                "subinterface": {
                                    0: {
                                        "config": {
                                            "index": 0
                                        },
                                        "ipv4": {
                                            "addresses": {
                                                "address": {
                                                    "10.0.254.11": {
                                                        "config": {
                                                            "ip": "10.0.254.11",
                                                            "prefix-length": 32
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "ipv6": {
                                            "addresses": {
                                                "address": {
                                                    "fc00:10:0:254::11": {
                                                        "config": {
                                                            "ip": "fc00:10:0:254::11",
                                                            "prefix-length": 128
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                       }

xpath2 = "/openconfig-interfaces:interfaces/interface[name=\"loopback\"]/config/description"
description_str = "new-pysros-description"

# Functions 
def get_nokia_netconf(nc_sesion, xpath: str) -> dict:
    result = {}

    try:
        result = nc_sesion.running.get(path=xpath)

    except LookupError as e:
        result = f"{e} for {xpath}"

    return result


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

    ## Collect the configuration of an interface in OpenConfig YANG modules
    r1 = get_nokia_netconf(nc_sesion=connect_obj, xpath=xpath)
#    r1 = get_nokia_netconf(nc_sesion=connect_obj, xpath=xpath2)

    # Setting a nested value (YANG container or list)
    connect_obj.candidate.set(path=xpath, value=yang_container_value)
#    connect_obj.candidate.set(path=xpath2, value=description_str)

    ## Collect the configuration of an interface in OpenConfig YANG modules
    r2 = get_nokia_netconf(nc_sesion=connect_obj, xpath=xpath)
#    r2 = get_nokia_netconf(nc_sesion=connect_obj, xpath=xpath2)

    connect_obj.disconnect()

    ## Timestamp: completed
    t2 = datetime.datetime.now()

    ## Printing results
    tl = os.get_terminal_size()
    print(f"{'=' * tl.columns}\nCompleted in {t2 -t1}\n{'=' * tl.columns}\n")

    ## Printing collected data
    print("Pre-change collection:")
    if isinstance(r1, str):
        print(r1)
    else:
        printTree(r1)

    print("\nPost-change collection:")
    printTree(r2)

    print(f"\n{'=' * tl.columns}\n")
