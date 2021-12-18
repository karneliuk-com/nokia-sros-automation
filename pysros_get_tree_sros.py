# Modules
import sys
import time
from pysros.management import connect
from pysros.pprint import printTree

# Variables
path = '/nokia-conf:configure/card[slot-number="1"]'

# Body
if __name__ == "__main__":
    ## Check input args
    input_args_list = sys.argv
    del input_args_list[0]

    input_args_list = [path] if len(input_args_list) == 0 else input_args_list

    for path_str in input_args_list:
        ## Get the timesamp in the beginning of the command
        t1 = time.ticks_ms()

        ## Collect the information
        connect_obj = connect()             
        results = connect_obj.running.get(path_str)
        connect_obj.disconnect()

        ## Print results
        print("Reuqested path: \n{}\n\nResult:".format(path_str))   
        printTree(results)

        ## Get the timesamp at the end
        t2 = time.ticks_ms()

        ## Print time
        print("\nCompleted in {} ms".format(time.ticks_diff(t2, t1)))  
