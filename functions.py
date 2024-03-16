from functools import reduce

def sll(point1,point2): return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**(1/2)

def curvature(points):
    try:
        sl = [((points[i][0]-points[i-1][0])**2+(points[i][1]-points[i-1][1])**2+(points[i][2]-points[i-1][2])**2)**(1/2) for i in range(len(points))]
        return round(4*((sum(sl)/2*reduce(lambda x, y: x * y, [sum(sl)/2-i for i in sl]))**(1/2))/reduce(lambda x, y: x * y, sl),2)
    except: return 0
def get_all_curvatures(points): return [curvature(points[i:i+3]) for i in range(len(points) - 2)]    

def dx(points):return [0]+[abs(round((points[i+1][0]-points[i][0])/(points[i+1][2]-points[i][2])*1000,3)) for i in range(len(points)-1)]
def dy(points):return [0]+[abs(round((points[i+1][1]-points[i][1])/(points[i+1][2]-points[i][2])*1000,3)) for i in range(len(points)-1)]
def dxy(points):return [0]+[abs(round(sll(points[i+1],points[i])/(points[i+1][2]-points[i][2])*1000,3)) for i in range(len(points)-1)]
def acc(points): 
    d=dxy(points)
    return [0]+[abs(round((d[i+1]-d[i])/(points[i+1][2]-points[i][2])*1000,3)) for i in range(len(points)-1)]

def curv_acc(points):
    k=[0]+get_all_curvatures([[i[0],i[1],0] for i in points])+[0]
    v=dxy(points)
    return [round((v[i]**2)*k[i],2) for i in range(len(k)-1)]
    
    
if __name__=="__main__": 
    # print(get_all_curvatures([[25,25,0],[27,30,10],[25,50,0],[50,215,50]]))
    from Reader import get_points
    for i in curv_acc(get_points("u0001_g_0100v19.txt","time")): print(i)
