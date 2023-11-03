#คุณสมบัติเด่น ของ op : Inheritance สืบทอด

class TestA :
    data1 = 10
    data2 = 20
    
    def showSAU():
        print ("Hi........SAU")
class TestB(TestA): 
    data3 = 30

    def showmom():
        print ("WOW WOW WOW")

class TestC(TestA):
    data4 = 40

class TestD(TestB):
    data5 = 50

ob1=TestA()
ob2=TestB()
ob3=TestD()
#คุณสมบัติเด่น ของ op : Polymorphism พ้องรูป พฤติกรรมเดียวกดันต่างกัน

