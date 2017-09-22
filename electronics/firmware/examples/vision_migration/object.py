# ===========
#  Libraries
# ===========


# =====================
#  Class Configuration
# =====================


# ===================
#  Class Declaration
# ===================
class Object:
    def __init__(self,name="Object"):
		self.setType(name)
		self.setColor([0,0,0])

		if(name=="blue"):
			# TODO: use "calibration mode" to find HSV min
			# and HSV max values

			self.setHSVmin( (92,0,0)) 
			self.setHSVmax( (124,256,256)) 

			# BGR value for Blue:
			self.setColor( (255,0,0)) 

		if(name=="green"):
			# TODO: use "calibration mode" to find HSV min
			# and HSV max values

			self.setHSVmin( (34,50,50)) 
			self.setHSVmax( (80,220,200)) 

			# BGR value for Green:
			self.setColor( (0,255,0)) 

		if(name=="yellow"):
			# TODO: use "calibration mode" to find HSV min
			# and HSV max values

			self.setHSVmin( (20,124,123)) 
			self.setHSVmax( (30,256,256)) 

			# BGR value for Yellow:
			self.setColor( (0,255,255)) 

		if(name=="red"):
			# TODO: use "calibration mode" to find HSV min
			# and HSV max values

			self.setHSVmin( (0,200,0)) 
			self.setHSVmax( (19,255,255)) 

			# BGR value for Red:
			self.setColor( (0,0,255)) 
			
		self.xPos = -1
		self.yPos = -1
		self.type = -1
		self.HSVmin = -1
		self.HSVmax = -1
		self.Color = -1

    def getType(self):
        return self.type

    def setType(self, t):
        self.type = t

    def getColor(self):
        return self.Color

    def setColor(self,c):
        self.Color = c

    def getXPos(self):
        return int(self.xPos)

    def setXPos(self, x):
        self.xPos = x

    def getYPos(self):
        return int(self.yPos)

    def setYPos(self, y):
        self.yPos = y

        def getHSVmin(self):
            return self.HSVmin

    def getHSVmax(self):
        return self.HSVmax

    def setHSVmin(self, min):
        self.HSVmin = min

    def setHSVmax(self, max):
        self.HSVmax = max
