
from operator import itemgetter
import pprint

under_cfgs = [
    {
        "priority_level": 3,
        "start_time"    : 200,
        "end_time"      : 300
    },
    {
        "priority_level" : 2,
        "start_time"     : 100,
        "end_time"       : 400
    },
    {
        "priority_level" : 2,
        "start_time"     : 200,
        "end_time"       : 600
    },
    {
        "priority_level" : 2,
        "start_time"     : 200,
        "end_time"       : 700
    },

]


# priority_level down
# start_time     up
# end_time       down

under_cfgs = sorted(under_cfgs, key = itemgetter("end_time"), reverse = True)
under_cfgs = sorted(under_cfgs, key = itemgetter("start_time"), reverse = False)
under_cfgs = sorted(under_cfgs, key = itemgetter("priority_level"), reverse = True)
pprint.pprint(under_cfgs)
