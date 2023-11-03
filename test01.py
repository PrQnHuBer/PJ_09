def a():
    pass
#สร้าง class 

class IoTSAU : 
    pass

#deta/attribute    เหมือนกับตัวแปร
    info1 =20
    info2 = "  "

#method members เหมือนฟังก์ชั่น
    def show(self):
        print("hi")
    def showinfo(self):
        print(self.info1,self.info1)
        self.show

#การสร้าง object 
obA = IoTSAU()
obB = IoTSAU()
obC = IoTSAU()

obA.info1=100
print(obA.info1 + obB.info1) # 120
obC.showinfo()
obA.showinfo()