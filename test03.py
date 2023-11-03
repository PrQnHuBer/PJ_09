#คุณสมบัติเด่น ของ endcapsulation (ซ่อนหรือห่อหุ้ม)โดยใส่ __ ไว้ข้างหน้า

class MytestA :
    __data1=10
    data2=20
    #เมื่อdata ถูกห่อหุ้มให้ผ่านmethod get set
    def getdata1(self):
        return self.__data1
    def setdata1(self):
        self.__data1 = data1
    def getdata(self):
        self.__data3
    def setdata1(self,data3):
        return self.__data3
    def setdata1(self,data3):
        self.__data3 = data3

    def __init__(self, data3):
        self.__data1 = data3
    
    def showdata(self):
        print (f'__data1={self.__data1}')
        print (f'data2={self.data2}')
        print (f'__data3={self.__data3}')
        print ('-------------------------')


ob1 =MytestA(30)
ob1.showdata()
ob1.data2=200
ob1._data1=100
ob1.showdata()