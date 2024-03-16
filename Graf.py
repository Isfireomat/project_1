import numpy as np
import matplotlib.pyplot as plt
import math
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QPainter, QPen, QPixmap

def grafic(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for points in points:
        y = [i[0] for i in points]
        x = [i[1] for i in points]
        z = [i[2] for i in points]
    
        for i in range(len(x)-1):ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], color='b')
        for i in range(len(x)-1):ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [0, 0], color='r')
        
    ax.set_xlabel('Y')
    ax.set_ylabel('X')
    ax.set_zlabel('Pression')

    plt.show()
    
def gist(points):
    plt.bar(range(1,len(points)+1),points, color='skyblue', edgecolor='black')

    plt.title('Text')
    plt.xlabel('Номер')
    plt.ylabel('LBP')

    plt.show()

def circle(size,angle1,angle2):
    pixmap = QPixmap(size)
    pixmap.fill(Qt.white)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    rect = QRectF(30, 30, 280, 280)
    painter.drawEllipse(rect)
    pen = QPen(Qt.red) 
    pen.setWidth(2)
    painter.setPen(pen)
    center = rect.center()
    radius = rect.width() / 2
    text_offset = 20  
    for angle in range(0, 360, 15):
        adjusted_angle = (angle + 180) % 360 
        x = center.x() - 5 + (radius + text_offset) * math.cos(math.radians(adjusted_angle))
        y = center.y() + 5 + (radius + text_offset) * math.sin(math.radians(adjusted_angle))
        end_point = QPointF(x, y)
        painter.drawText(end_point, f"{(adjusted_angle+180)%360}°")

    pen.setColor(Qt.black)  
    painter.setPen(pen)
    for angle in range(0, 360, 45):
        painter.drawPie(rect, angle * 16, 45 * 16)

    blue_angle = (180+angle1)%360 
    blue_x = center.x() + radius * math.cos(math.radians(blue_angle))
    blue_y = center.y() + radius * math.sin(math.radians(blue_angle))
    painter.setBrush(Qt.blue) 
    painter.setPen(Qt.blue)  
    painter.drawEllipse(QPointF(blue_x, blue_y), 5, 5)
    
    blue_angle = (180+angle2)%360 
    blue_x = center.x() + radius * math.cos(math.radians(blue_angle))
    blue_y = center.y() + radius * math.sin(math.radians(blue_angle)) 
    painter.drawEllipse(QPointF(blue_x, blue_y), 5, 5)
    
    painter.end()
    return pixmap




def podpis(points,max_x,max_y,changed_points=0):
    pixmap = QPixmap(QSize(max_x+100, max_y+100))
    pixmap.fill(Qt.white)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    pen = QPen()
    pen.setColor(Qt.black)
    pen.setWidth(2)
    painter.setPen(pen)
    for j in points:
        for i in range(len(j) - 1):painter.drawLine(j[i][0], j[i][1], j[i + 1][0], j[i + 1][1])
    if not changed_points:changed_points=points[0][1]
    painter.setBrush(Qt.red) 
    painter.setPen(Qt.red)  
    painter.drawEllipse(QPointF(changed_points[0], changed_points[1]), 3, 3)
        
    painter.end()
    return pixmap