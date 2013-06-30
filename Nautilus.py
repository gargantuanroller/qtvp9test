import os, sys
from PySide import QtCore, QtGui, QtUiTools
if __name__ == '__main__':
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	print("Running in " + os.getcwd() + "\n")

def uiToWidget(uiPath):
	loader = QtUiTools.QUiLoader()
	file = QtCore.QFile(os.path.normpath(uiPath))
	file.open(QtCore.QFile.ReadOnly)
	widget = loader.load(file)
	file.close()
	return widget


#class NautilusQMainWindow(QtGui.QMainWindow):
#	def __init__(self, *args): 
#		apply(QtGui.QMainWindow.__init__, (self,) + args)

#		loader = QtUiTools.QUiLoader()
#		file = QtCore.QFile(os.getcwd() + "/Nautilus.ui")
#		file.open(QtCore.QFile.ReadOnly)
#		self.NautilusQMainWindow = loader.load(file, self)
#		file.close()

#		self.setCentralWidget(self.NautilusQMainWindow)

#if __name__ == '__main__':
#	app = QtGui.QApplication(sys.argv) 

#	win  = NautilusQMainWindow() 
#	win.show()

#	app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
#		app, QtCore.SLOT("quit()"))
#	app.exec_()

