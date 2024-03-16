import csv
from collections import Counter

def read_csv(file_name): return ['.'.join(row).split(";") for row in csv.reader(open(file_name, newline=''))]
def read_hwr_txt(file_name): return ['.'.join(row).split(" ") for row in csv.reader(open(file_name, newline=''))]
    
def get_standart_time(file_name):    
    points=get_points(file_name,"time")     
    try:
        counter = Counter([points[i+1][2]-points[i][2] for i in range(len(points)-1)])
        time = counter.most_common(1)[0][0]
        return time 
    except: return None

def get_points(file_name,bool="nontime"):
    m = [[]]
    match file_name.split(".")[-1]:
        case "csv": 
            match bool:
                case "time":
                    return [[float(i[2]),float(i[3]),round(float(i[5]),2)] for i in read_csv(file_name)[1:]]
                case "maxmin":
                    points=[[float(i[2]),float(i[3]),round(float(i[6]),2)] for i in read_csv(file_name)[1:]]
                    min_value = min(i[1] for i in points)
                    max_value = max(i[1] for i in points)
                    for i in points: 
                        m[-1].append(i) if i[1]!=min_value and i[1]!=max_value else m.append([]) if m[-1] else None
                case _:
                    for i in [[float(i[2]),float(i[3]),round(float(i[6]),2)] for i in read_csv(file_name)[1:]]: 
                        m[-1].append(i) if i[2]!=0 else m.append([]) if m[-1] else None
                
        case "txt":
            match bool:
                case "time":
                    return [[round(float(i[0])/100,2),round(float(i[1])/100,2),round(float(i[2]),2)] for i in read_hwr_txt(file_name)[1:]] 
                case "maxmin":
                    points=[[round(float(i[0])/100,2),round(float(i[1])/100,2),round(float(i[5])/10,2)] for i in read_hwr_txt(file_name)[1:]]
                    min_value = min(i[1] for i in points)
                    max_value = max(i[1] for i in points)
                    for i in points: 
                        m[-1].append(i) if i[1]!=min_value and i[1]!=max_value else m.append([]) if m[-1] else None
                case _:
                    for i in [[round(float(i[0])/100,2),round(float(i[1])/100,2),round(float(i[5])/10,2)] for i in read_hwr_txt(file_name)[1:]]: 
                        m[-1].append(i) if i[2]!=0 else m.append([]) if m[-1] else None
        
        case "HWR":
            match bool:
                case "time":
                    return None
                case "maxmin":
                    points=[[round(float(i[0])/1000,2),round(float(i[1])/1000,2),round(float(i[2])/10,2)] for i in read_hwr_txt(file_name)[1:]]
                    min_value = min(i[1] for i in points)
                    max_value = max(i[1] for i in points)
                    for i in points: 
                        m[-1].append(i) if i[1]!=min_value and i[1]!=max_value else m.append([]) if m[-1] else None
                case _:
                    for i in [[round(float(i[0])/1000,2),round(float(i[1])/1000,2),round(float(i[2])/10,2)] for i in read_hwr_txt(file_name)[1:]]: 
                        m[-1].append(i) if i[2]!=0 else m.append([]) if m[-1] else None            
    return m




if __name__ == "__main__":
    ...
    # for i in get_points('K9.csv',"maxmin"): print(i)
    # for i in get_points('0124005_1.HWR',"maxmin"): print(i)
    # for i in get_points("u0001_g_0100v19.txt",'maxmin'): print(i)
    # print(dx(get_points("u0001_g_0100v19.txt","time")))
    # print(dy(get_points("u0001_g_0100v19.txt","time")))
    # for i in acc(get_points("K9.csv","time")): print(i)
    # print(get_standart_time("0124005_1.HWR"))
    # print(get_standart_time("K9.csv"))
    # print(get_points("u0001_g_0100v19.txt","time"))