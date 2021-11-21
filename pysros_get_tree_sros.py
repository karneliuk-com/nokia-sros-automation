# Modules
import sys
import utime
from pysros.management import connect
from pysros.pprint import printTree

# Variables
path = '/nokia-conf:configure/card[slot-number="1"]'

# Body
if __name__ == "__main__":
    ## Get the timesamp in the beginning of the command
    t1 = utime.ticks_ms()

    ## Collect the information
    connect_obj = connect()             
    results = connect_obj.running.get(path)
    connect_obj.disconnect()

    ## Print results
    print("Reuqested path: \n{}\n\nResult:".format(path))   
    printTree(results)

    ## Get the timesamp at the end
    t2 = utime.ticks_ms()

    ## Print time
    print("\n\nCompleted in {} ms".format(utime.ticks_diff(t2, t1)))  
