from bs4 import BeautifulSoup

def get(htmldoc):
	bs = BeautifulSoup(htmldoc,"html.parser")
	SeatInfo = []
	listres = bs.find_all("td")
	for i in listres:
		if i.get('lib_id')!=None and i.get('lib_id')!= '':
			print(i.get('lib_id'),i.get('seat_key'))
			SeatInfo .append([i.get('lib_id'),i.get('seat_key'),i.string])
	SeatNum = len(SeatInfo)
	print('您有%d个预定座位,以下是详细信息,您要选哪个?\n'%(SeatNum))
	for i in range(1,SeatNum + 1):
		print('%d,%s'%(i,SeatInfo[i-1][2]))
	choice = int(input('请输入 数字1 或 数字2(请务必输入正确):'))# 未做输入检查，谨慎输入
	lib_id = SeatInfo[choice - 1][0]
	seat_key = SeatInfo[choice - 1][1]
	return lib_id,seat_key