import system_config
import tkinter
from tkinter import ttk
import tkinter.messagebox

app = tkinter.Tk()
app.title("河南财经政法大学图书馆选座助手 v3.01版")
app.geometry("910x540")


def go(*args):
	floor = book_floors.get()
	position = book_positions.get()
	seat = book_seats.get()
	sessions = session.get()
	system_config.wechatSESS_ID = sessions
	tkinter.messagebox.showinfo(floor+position+seat,"选座结果:\n"+"\t\t选座成功！")


padding = tkinter.Label(app)
padding.pack()


main_label = tkinter.Label(app,text="欢迎订阅河南财经政法大学图书馆选座系统('来选座') Build 1555049354.5663848")
main_label.pack()


padding = tkinter.Label(app)
padding.pack()

# 选择楼层
book_floor = tkinter.StringVar()
book_floors = ttk.Combobox(app, textvariable=book_floor,width=38)
book_floors["values"] = ("二楼", "三楼", "四楼","五楼","六楼","七楼","八楼","九楼")
book_floors.current(0)
book_floors.pack()

# 选择阅览区
book_position = tkinter.StringVar()
book_positions = ttk.Combobox(app,textvariable=book_position,width=38)
book_positions['values'] = ("东阅览区","西阅览区","中阅览区","南阅览区","北阅览区","东电子阅览区","西电子阅览区","中电子阅览区")
book_positions.current(0)
book_positions.pack()

# 位置
book_seat = tkinter.StringVar()
book_seats = ttk.Combobox(app,textvariable=book_seat,width=38)
book_seats['values'] = ("21号座位 (固定订阅用户)不支持可变序列座位位置")
book_seats.current(0)
book_seats.pack()


padding = tkinter.Label(app)
padding.pack()

session = tkinter.Entry(app, width=40)
session.pack()

padding = tkinter.Label(app)
padding.pack()

booking = tkinter.Button(app,bg="blue",text="开始选座",width=8,height=2,command=go)
booking.pack()

app.mainloop()