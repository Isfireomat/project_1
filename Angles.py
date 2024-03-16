import math

def angle_between_points(center, point):
    angle = math.degrees(math.atan2(point[0] - center[0], point[1] - center[1])) + 90
    return angle if angle >= 0 else 360-abs(angle) 

def sectors_sum(center,points): return sum([2**int(i/45) if i%45 else sum([2**int((i+1 if i!=360 else 1)/45)+2**int((i-1 if i!=0 else 359)/45)]) for i in [angle_between_points(center,i) for i in points]])
def get_all_sectors_sum(points):return [sectors_sum(points[i:i+3][1],[points[i:i+3][0],points[i:i+3][2]]) for i in range(len(points) - 2)]
if __name__=="__main__":    
    center = [79.96, 30.94]
    points = [[79.56, 31.24],
            [80.37, 30.63]]
    for i,z in enumerate([angle_between_points(center,i) for i in points]):
        print(f"point{points[i]}={z}")
    print(sectors_sum(center,points))
        
    
    
    
    
    
    
    
