class IoTThailand :
    #data
    wow=100
    wea=""

    #construtor ทำงานทุกครั้งที่สร้างobject 
    def __init__ (self,woo,wee,wea) :
        self.woo = woo
        self.wee = wee
        self.wea = wea

    #method 
    def showdata(self):
        print (self.wow*20)

    #destructor ทำงานอัตโนมัติหลังทำงานเสร็จหรือถูกทำลาย
    def __del__(self):
        print ("Good morning")


ob1 = IoTThailand(10,20,10)
ob2 = IoTThailand(10,20,35)
ob3 = IoTThailand(5,20,10)
ob4 = IoTThailand(10,20,10)

print (ob1.wea + ob2.wea)
ob3.showdata()