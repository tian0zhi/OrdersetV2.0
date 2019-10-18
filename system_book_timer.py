import time


def timer_setting():
	while True:
		now = time.localtime()
		year = now.tm_year
		month = now.tm_mon
		day = now.tm_mday
		hour = now.tm_hour
		minute = now.tm_min
		second = now.tm_sec
		#my_time = str(year)+'-'+str(month)+'-'+str(day)+'-'+str(hour)+'-07'+'-00'
		#以下是占座时间 年         月         日          时   分    秒
		my_time = str(2019)+'-'+str(9)+'-'+str(26)+'-'+str(5)+'-59'+'-58'
		goal = time.strptime(my_time, '%Y-%m-%d-%H-%M-%S')
		if now>=goal:

			return True
		else:
			goal = time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))
			print("目标时间：北京时间"+my_time+"\t"+"预计等待："+str(int(int(goal)-int(time.time())))+"秒")
			time.sleep(0.1)
