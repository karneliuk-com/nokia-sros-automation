# Modules
import time
from pysros.management import connect
import re


# Body
if __name__ == "__main__":
    ## Get the timesamp in the beginning of the command
    t1 = time.ticks_ms()

    ## Collect the information
    connect_obj = connect()             
    results = connect_obj.cli("show router route-table | no-more")
    connect_obj.disconnect()

    ## Processing results
    is_default_route_bool = True if re.search(r'0\.0\.0\.0/0', results) else False

    num_routes_int = 0
    for line_str in results.splitlines():
        if re.match(r'^No\. of Routes:', line_str):
            num_routes_int = int(re.sub(r'^No\. of Routes: (\d)$', r'\1', line_str))

    print("Routes in routing table: {}\nDoes default route exist: {}".format(num_routes_int, is_default_route_bool))

    ## Get the timesamp at the end
    t2 = time.ticks_ms()

    ## Print time
    print("\nCompleted in {} ms".format(time.ticks_diff(t2, t1)))  
