import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QFileDialog
from PyQt5.QtCore import Qt,QSize
import convert
from main_project_form import Ui_MainWindow
from Reader import get_points
from functions import get_all_curvatures,sll
from Angles import get_all_sectors_sum,angle_between_points
from Graf import grafic,gist, podpis,circle

def sl(point1,point2): 
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**(1/2)

class Form(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.LoadFile)
        self.pushButton_2.clicked.connect(self.LBP_bar_charts)
        self.pushButton_3.clicked.connect(self.Pression)
        self.comboBox.currentIndexChanged.connect(self.CircleUpdate)
    
    def CircleUpdate(self,value): 
        self.label_2.setPixmap(circle(QSize(self.label_2.width(), self.label_2.height()),angle_between_points(self.primary_points[value+1],self.primary_points[value]),angle_between_points(self.primary_points[value+1],self.primary_points[value+2])))
        self.label.setPixmap(podpis(self.points,self.max_value_1,self.max_value_2,sum(self.points,[])[value+1]))
          
    def LoadFile(self):
        file_path,_=QFileDialog().getOpenFileName(self, "Выбрать файл", "", "CSV file (*.csv)")
        if file_path: 
            points=get_points(file_path)       
            self.second_points=get_points(file_path)
            self.primary_points=sum(get_points(file_path),[])
            min_value_1,min_value_2 = min(sum(points, []), key=lambda x: x[0])[0], min(sum(points, []), key=lambda x: x[1])[1]
            self.points=points=[ [[int(round((i[0]-min_value_1)*10+10)),int(round((i[1]-min_value_2)*10+100))] for i in j] for j in points]
            self.max_value_1,self.max_value_2=max(sum(points,[]), key=lambda x: x[0])[0], max(sum(points,[]), key=lambda x: x[1])[1]
            self.comboBox.addItems([f"{i+2}: {str(m[:2])}" for i,m in enumerate(self.primary_points[1:len(self.primary_points)-1])])
        
    def Pression(self):
        if self.second_points: grafic(self.second_points)
    
    def LBP_bar_charts(self):
        if self.primary_points: gist(get_all_sectors_sum(self.primary_points))
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            pos = event.pos()
            pixmap = self.label.pixmap()
            if pixmap:
                masiv=[sll(i,[pos.x(),pos.y()]) for i in sum(self.points,[])[1:len(sum(self.points,[]))-1]]
                self.label.setPixmap(podpis(self.points,self.max_value_1,self.max_value_2,sum(self.points,[])[masiv.index(min(masiv))+1]))
                self.comboBox.setCurrentIndex(masiv.index(min(masiv)))
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    Main_Form=Form()
    Main_Form.show()
    app.exec_()


























# points=[i[:2]+[0] for i in points]
# curvatures=get_all_curvatures(points)
# grafic(points)
# for i in get_all_sectors_sum(points): print(i)
# print(get_all_sectors_sum(points))
# gist(get_all_sectors_sum(points))



#визуализировать сектора
