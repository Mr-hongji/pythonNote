'''

    继承
       语法：
           子类(父类)

'''


#创建父类交通工具类 -- Vehicle

class Vehicle:
    speed = 0 #速度

    def driver(self, distance): #distance : 路程
        print float(distance / self.speed)
        


#创建子类汽车类 -- Car 继承父类Vehicle

class car(Vehicle):
    fuel = 0
    speed = 60

    driver(100)
    




#创建子类自行车类 -- bike 继承父类Vehicle 

class bike(Vehicle):

    speed = 
    
