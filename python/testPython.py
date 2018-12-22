class A:
    def __init__(self,tdiem=0):
        self._diem=tdiem


    @property
    def diem(self):
        print('Lấy điểm')
        return self._diem

    @diem.setter
    def diem(self,temp):
        print('Nhap diem')
        self._diem=temp

    
    
# a=A(3)
# print(a.diem)
X = 10
lam= lambda x: X+5
print(lam(5))
   


        