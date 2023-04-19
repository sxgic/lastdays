import time

cur_time = int(time.time())

timeArray = time.localtime(cur_time)
otherStyleTime = time.strftime("%Y%m%d", timeArray)

for i in range(0, 145):
    next_time = i * 3600 * 24 + cur_time
    timeArray = time.localtime(next_time)
    otherStyleTime = time.strftime("%Y%m%d", timeArray)
    print("CREATE TABLE IF NOT EXISTS `t_name_log_%s` LIKE `t_name_log`;" % otherStyleTime)
