from PySide import QtCore, QtGui, QtUiTools

class NautilusQMainWindow(QtGui.QMainWindow):
	def __init__(self, *args):  
		apply(QtGui.QMainWindow.__init__, (self,) + args)

		loader = QtUiTools.QUiLoader()
		file = QtCore.QFile("Nautilus.ui")
		file.open(QtCore.QFile.ReadOnly)
		self.NautilusQMainWindow = loader.load(file, self)
		file.close()

		self.setCentralWidget(self.NautilusQMainWindow)

if __name__ == '__main__':
	import os, sys
	print("Running in " + os.getcwd() + " .\n")
	print("os.path.dirname(os.path.realpath(__file__)) = " + os.path.dirname(os.path.realpath(__file__)) + " .\n\n")


	app = QtGui.QApplication(sys.argv)  

	win  = NautilusQMainWindow()  
	win.show()

	app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
		app, QtCore.SLOT("quit()"))
	app.exec_()

