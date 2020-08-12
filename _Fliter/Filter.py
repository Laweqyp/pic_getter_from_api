import xlrd
import random
from xlutils.copy import copy
from PIL import Image, ImageTk

def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("Successfully append object to sheet")


def ramdompid():
    _loc = "D:\_Code\\2d_erotic_pic\\url_list.txt"
    _ret = ""
    _f = open(_loc, 'r')
    resultList = random.sample(range(0, len(open(_loc, 'r').readlines())), 1)  # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。
    lines = _f.readlines()
    for i in resultList:
        _ret = lines[i]
    _f.close()
    return _ret


def finddup(_obj):
    _fd = open('./dup.txt', 'r')
    _fdl = _fd.readlines()
    _fd.close()
    i = len(_fdl) - 1
    while i >= 0:
        if _obj == _fdl[i] or _fdl[i] == _obj + "\n":
            return True
        i -= 1
    return False


def getramdpid():
    while True:
        _tmp = ramdompid()
        if not finddup(_tmp):
            with open('./dup.txt', 'a+', encoding='utf-8') as f:
                f.write(_tmp)
            return _tmp


def imgshower(picpath):
    import tkinter
    root = tkinter.Tk()
    root.title('应用程序窗口')  # 窗口标题
    root.resizable(False, False)  # 固定窗口大小
    windowWidth = 1200  # 获得当前窗口宽
    windowHeight = 700  # 获得当前窗口高
    screenWidth, screenHeight = root.maxsize()  # 获得屏幕宽和高
    geometryParam = '%dx%d+%d+%d' % (
        windowWidth, windowHeight, (screenWidth - windowWidth) / 2, (screenHeight - windowHeight) / 2)
    root.geometry(geometryParam)  # 设置窗口大小及偏移坐标

    def resize(w, h, w_box, h_box, pil_image):
        '''
        resize a pil_image object so it will fit into
        a box of size w_box times h_box, but retain aspect ratio
        对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
        '''
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        # print(f1, f2, factor) # test
        # use best down-sizing filter
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)
    # size of image display box you want
    # 期望图像显示的大小
    w_box = 1000
    h_box = 650
    # open as a PIL image object
    # 以一个PIL图像对象打开
    pil_image = Image.open(picpath)
    # get the size of the image
    # 获取图像的原始大小
    w, h = pil_image.size
    # resize the image so it retains its aspect ration
    # but fits into the specified display box
    # 缩放图像让它保持比例，同时限制在一个矩形框范围内
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    # convert PIL image object to Tkinter PhotoImage object
    # PIL图像对象转变为Tkinter的PhotoImage对象
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    # put the image on a widget the size of the specified display box
    # Label: 这个小工具，就是个显示框，小窗口，把图像大小显示到指定的显示框
    label = tkinter.Label(root, image=tk_image, width=w_box, height=h_box)
    # padx,pady是图像与窗口边缘的距离

    label.pack(padx=10, pady=5)

    def xpr1():
        global rank
        rank = 1
        root.destroy()

    def xpr2():
        global rank
        rank = 2
        root.destroy()

    def xpr3():
        global rank
        rank = 3
        root.destroy()

    def xpr4():
        global rank
        rank = 4
        root.destroy()

    def xpr5():
        global rank
        rank = 5
        root.destroy()

    def exitmain():
        global ifexit
        ifexit = 1

    button1 = tkinter.Button(root, text=' 这也叫色图?', command=xpr1)
    button1.place(x=1110, y=20)

    button2 = tkinter.Button(root, text='  就这就这？', command=xpr2)
    button2.place(x=1110, y=60)

    button3 = tkinter.Button(root, text=' 这张还勉强 ', command=xpr3)
    button3.place(x=1110, y=100)

    button4 = tkinter.Button(root, text='这个可以有!!', command=xpr4)
    button4.place(x=1110, y=140)

    button5 = tkinter.Button(root, text='哦淦我xp爆了', command=xpr5)
    button5.place(x=1110, y=180)

    button6 = tkinter.Button(root, text='完事收工了！', command=exitmain)
    button6.place(x=1110, y=300)

    root.update_idletasks()
    root.mainloop()

ifexit = 0
while not ifexit:
    while not ifexit:
        try:
            pidurl = getramdpid()
            rank = 0
            imgshower("D:\_Code\\2d_erotic_pic\pic\\" + pidurl[57:65] + pidurl[len(pidurl)-5:len(pidurl)-1])
            _append = [[pidurl, pidurl[57:65], rank]]
            write_excel_xls_append('./Database.xls', _append)
            print(pidurl)
        except BaseException as e:
            print(e)
            continue
        else:
            break
