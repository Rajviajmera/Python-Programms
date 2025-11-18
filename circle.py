def circle():
	r=int(input("enter radius :"))
	a=r*r*(22/7)
	c=2*r*(22/7)
	print("area of circle{}:{}".format(r,a))
	print("circumfrence {}:{}".format(r,c))
'''circle()
circle()
circle()
circle()'''
for i in range(25):
	circle()