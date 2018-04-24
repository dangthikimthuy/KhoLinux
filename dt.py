class sv:
	def _init_(self,mssv,hoten,makhoa):
		self.mssv=mssv
		self.hoten=hoten
		self.makhoa=makhoa
	def getmssv(self):
		return self.mssv
	
	def gethoten(self):
		return self.hoten
	
	def getmakhoa(self):
		return self.makhoa
	
		print"mssv",self.mssv,"hoten",self.hoten,"makhoa",self.makhoa
emp=sv("001","Mai A","01")
emp.disten()
emp=sv("002","Tran B","02")
emp.disten()

	
class khoa:
	def _init_(self,makhoa,tenkhoa):
		self.makhoa=makhoa
		self.tenkhoa=tenkhoa
	def getmakhoa(self):
		return self.makhoa
	
	def gettenkhoa(self):
		return self.tenkhoa
	
emp=khoa("01","cntt")
emp.disten()
emp=khoa("02","ktoan")
emp.disten()



