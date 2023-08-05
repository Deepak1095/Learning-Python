class Rectange:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
    def parameter(self):
        return 2*(self.length+self.width)
    

rectange=Rectange(10,15)

print("area",rectange.area())
print("parameter",rectange.parameter())