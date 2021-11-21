# Modules
import sys
import utime
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
        t1 = utime.ticks_ms()

        ## Collect the information
        full_xpath_str = "/" + path_str
        connect_obj = connect()             
        results = connect_obj.running.get(full_xpath_str)
        connect_obj.disconnect()

        ## Print results
        print("Reuqested path: \n{}\n\nResult:".format(full_xpath_str))   
        printTree(results)

        ## Get the timesamp at the end
        t2 = utime.ticks_ms()

        ## Print time
        print("\nCompleted in {} ms".format(utime.ticks_diff(t2, t1)))  
