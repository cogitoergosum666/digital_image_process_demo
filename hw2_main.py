import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
from mainwindow import Ui_Form


class mwindow(QMainWindow):
    def __init__(self):
        super(mwindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.bond()
        # 使用graphicsView显示图片
        self.scene1 = QGraphicsScene()  # 创建画布
        self.ui.graphicsView_left.setScene(self.scene1)  # 把画布添加到窗口
        self.ui.graphicsView_left.show()

        self.scene2 = QGraphicsScene()  # 创建画布
        self.ui.graphicsView_right.setScene(self.scene2)  # 把画布添加到窗口
        self.ui.graphicsView_right.show()


    def bond(self):

        self.ui.button_load_image.clicked.connect(self.openimage)
        self.ui.button_equalizeHist.clicked.connect(self.eq)
        self.ui.button_average_filtering.clicked.connect(self.mean)
        self.ui.button_mid_filtering.clicked.connect(self.mid)
    #选择图片
    def openimage(self):
        #选择图片
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "img", "*.jpg;*.tif;*.png;;All Files(*)")
        #print(imgName)
        self.imgname = imgName
        if imgName=="":
            return 0
        #qt5读取图片
        jpg = QPixmap(imgName).scaled(self.ui.graphicsView_left.width(), self.ui.graphicsView_left.height())
        #显示原图
        self.scene1.clear()  #先清空上次的残留
        # self.pix = QPixmap.fromImage(frame)
        self.scene1.addPixmap(jpg)

    def eq(self):#直方图均衡化
        import hw2_equ
        res = hw2_equ.work(self.imgname)
        jpg = QPixmap('.\output_HistogramEqualization.png').scaled(self.ui.graphicsView_left.width(), self.ui.graphicsView_left.height())
        #显示原图
        self.scene2.clear()  #先清空上次的残留
        
        self.scene2.addPixmap(jpg)

    def mean(self):#中值滤波
        import hw3_average
        hw3_average.meanwork(self.imgname)
        jpg = QPixmap('.\mean_res.jpg').scaled(self.ui.graphicsView_left.width(), self.ui.graphicsView_left.height())
        #显示原图
        self.scene2.clear()  #先清空上次的残留
        
        self.scene2.addPixmap(jpg)

    def mid(self):#中值滤波
        import hw3_mid
        hw3_mid.midwork(self.imgname)
        jpg = QPixmap('.\midan_res.jpg').scaled(self.ui.graphicsView_left.width(), self.ui.graphicsView_left.height())
        #显示原图
        self.scene2.clear()  #先清空上次的残留
        
        self.scene2.addPixmap(jpg)




if __name__ == '__main__':
    app = QApplication([]) #启动一个应用
    window = mwindow() #实例化主窗口
    window.show() #展示主窗口
    app.exec() #避免程序知行到这一行后直接退出
    # app=QApplication(sys.argv)
    # #初始化窗口
    # m=mwindow()
    # #绑定按钮事件
    # c1 = QPushButton('button_load_image',m)
    
    # m.pushButton.clicked.connect(m.button_load_image)#选择图片
    # m.show()
    # sys.exit(app.exec_())