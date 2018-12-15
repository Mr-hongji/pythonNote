

#------------------------------------- 第十二章 ------------------------------------#



'''

    GUI 图形用户界面

        * wxPython 最成熟的跨平台的GUI工具包 官方文档： wxPython.org

        * 下载地址 https://sourceforge.net/projects/wxpython/files/wxPython/

        * 所下载的wxPython版本要与所安装的Python版本一致

        * 下载wxPython后，建议下载演示版本（demo,他需要独立安装）
'''


'''

    wx.App()

        * 创建应用程序对象，负责幕后所有的初始化（同Flex中的Application根标签）

    
    wx.Frame(父部件)

        * 类似于Flex中，在Application中添加一个Canvans组件，然后向里面添加各种组件等
    


import wx

app = wx.App()
win = wx.Frame(None, title='Simple Editor', size=(410, 335))
loadButton = wx.Button(win, label='Open', pos=(225, 5), size=(80,25))
saveButton = wx.Button(win, label='Save', pos=(315, 5), size=(80, 25))

filename = wx.TextCtrl(win, pos=(5, 5), size=(210,25))

content = wx.TextCtrl(win, pos=(5, 35), size=(390, 260),
                      style=wx.TE_MULTILINE | wx.HSCROLL)

win.Show()
app.MainLoop()


'''


'''

    调整窗口大小时，保证窗口中的组件也会随之调整大小和位置


    Sizer (尺寸器)

        * 管理吃组件的尺寸，只要将部件添加到尺寸器上，再加上一些布局参数
            - 然后然尺寸器自己去管理父组件的尺寸

    wx.BoxSize(wx.HORIZONTAL | wx.VERTICAL)

        * 类似于Flex中的Hbox和Vbox 有水平或垂直参数，默认是水平

    proportion

        * 百分比、比例

        * proportion = 1 获取全部剩余空间
'''


# 函数定义要放到添加事件的前面

def load(event):
    rf = open(filename.GetValue())
    contents.SetValue(rf.read())
    rf.close()

def save(event):
    sf = open(filename.GetValue(), 'w+')
    sf.write(contents.GetValue())
    sf.close()


import wx

app = wx.App()
win = wx.Frame(None, title = 'Simple Editor', size = (410, 335))

bkg = wx.Panel(win)
loadButton = wx.Button(bkg, label = 'Open')
saveButon = wx.Button(bkg, label = 'Save')

#按钮添加事件
loadButton.Bind(wx.EVT_BUTTON, load)
saveButon.Bind(wx.EVT_BUTTON, save)


filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion = 1, flag = wx.EXPAND)
hbox.Add(loadButton, proportion = 0, flag = wx.LEFT,  border = 5)
hbox.Add(saveButon, proportion = 0, flag = wx.LEFT,  border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vbox.Add(contents, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()


