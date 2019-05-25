#-*- coding: utf-8 -*-
import sys
import os 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLineEdit
from PyQt5 import uic 

# Clase heredada de QMainWindow (constructor de ventanas)
class Ventana(QMainWindow):
	# Metodo constructor de la clase
	def __init__(self):
		QMainWindow.__init__(self)
		# Cargar la configuracion del archivo .ui en el objeto
		uic.loadUi("MenuToolAndroid.ui", self)
		self.edit = Edit('', self)
		self.edit.setGeometry(84, 82, 271, 21)
		self.edit.setPlaceholderText("Arrastra el archivo aqui :)")
		self.edit2 = Edit('', self)
		self.edit2.setGeometry(84, 212, 271, 21)
		self.edit2.setPlaceholderText("Arrastra el archivo aqui :)")
		self.edit3 = Edit('', self)
		self.edit3.setGeometry(84, 342, 271, 21)
		self.edit3.setPlaceholderText("Arrastra el archivo aqui :)")		
		self.BAbrir.clicked.connect(self.archivo)
		self.BBorrar.clicked.connect(self.edit.clear)
		self.BDescompilar.clicked.connect(self.descompilar)
		self.BCompilar.clicked.connect(self.compilar)

		self.BAbrir_2.clicked.connect(self.archivo2)		
		self.BBorrar_2.clicked.connect(self.edit2.clear)
		self.BAbrir_3.clicked.connect(self.archivo3)
		self.BDex2jar.clicked.connect(self.dex2jar)
		self.BJar2dex.clicked.connect(self.jar2dex)

		self.BBorrar_3.clicked.connect(self.edit3.clear)

    # Evento para cerrar la aplicacion
	def closeEvent(self, event):
	  resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
	  if resultado == QMessageBox.Yes: event.accept()
	  else: event.ignore()

    # funcion que abrira el apk
	def archivo(self):
		# abrimos el archivo y ponemos como filtro que sea solo con extension apk 
	    fileName = QFileDialog.getOpenFileName(self, 'Selecciona el archivo', '','Archivos APK(*.apk)')	    
	    self.edit.setText(fileName[0])

	# funcion que abrira el apk
	def archivo2(self):
		# abrimos el archivo y ponemos como filtro que sea solo con extension apk 
	    fileName = QFileDialog.getOpenFileName(self, 'Selecciona el archivo', '','Archivos(*.apk *.dex)')	    
	    self.edit2.setText(fileName[0])
	# funcion que abrira el apk

	def archivo3(self):
		# abrimos el archivo y ponemos como filtro que sea solo con extension apk 
	    fileName = QFileDialog.getOpenFileName(self, 'Selecciona el archivo', '','Archivos (*.apk)')	    
	    self.edit3.setText(fileName[0])

	def descompilar(self):
	    global archivo
	    global carp_desc
	    global apktool
	    archivo = self.edit.text()
	    carp_desc = archivo.replace('.apk','')
	    apktool = 'herramientas\\apktool\\apktool.jar'
	    os.system('java -jar ' + apktool + ' d ' + archivo + ' -o ' + carp_desc)
	    QMessageBox.information(self, 'Informacion', 'Genial, Archivo descompilado', QMessageBox.Ok)

	def compilar(self):		
		nombre_archivo = os.path.basename(archivo) # extrae el nombre de la ruta del archivo archivo.apk	
		new_nombre_archivo = 'new_' + nombre_archivo # concatena la string new dando como resultado new_archivo.apk
		new_archivo = archivo.replace(nombre_archivo, new_nombre_archivo) 		
		#print('java -jar ' + apktool + ' b ' + carp_desc + ' -o ' + new_archivo)
		os.system('java -jar ' + apktool + ' b ' + carp_desc + ' -o ' + new_archivo)
		#print('termino....')
		QMessageBox.information(self, 'Informacion', 'Genial, Archivo Compilado', QMessageBox.Ok)

	def dex2jar(self):
		
		dex2jar = 'herramientas\\d2j-dex2jar\\d2j-dex2jar.bat'
		archivo2 = self.edit2.text()
		extension = os.path.splitext(archivo2)[1]
		if extension == '.dex' or extension == '.apk':
			# herramientas\\d2j-dex2jar\\d2j-dex2jar.bat ruta/archivo.apk -o ruta/archivo.jar		
			if extension == '.dex':
				new_archivo = archivo2.replace('.dex', '.jar')
			else:
				new_archivo = archivo2.replace('.apk', '.jar')


			os.system(dex2jar + ' ' + archivo2 + ' -o ' + new_archivo)
						
		else:
			QMessageBox.information(self, 'Error', 'Solo se admite archivos con extension .apk o .dex', QMessageBox.Ok)
			
		

	def jar2dex(self):
		jar2dex = 'herramientas\\d2j-dex2jar\\d2j-jar2dex.bat'
		archivo2 = self.edit2.text()
		extension = os.path.splitext(archivo2)[1]
		if extension == '.jar':
			new_archivo = archivo2.replace('.jar', '.dex')
			os.system(jar2dex + ' ' + archivo2 + ' -o ' + new_archivo)
						
		else:
			QMessageBox.information(self, 'Error', 'Solo se admite archivos con extension .dex', QMessageBox.Ok)
			# herramientas\\d2j-dex2jar\\d2j-dex2jar.bat ruta/archivo.dex -o ruta/archivo.jar		


class Edit(QLineEdit):
	def __init__( self, title, parent ):
		super().__init__(title,parent)
		self.setDragEnabled(True)
        # funciones para drap and drop 
	def dragEnterEvent(self, e):
		if e.mimeData().hasUrls():
			e.accept()
		else:
			e.ignore()
	def dropEvent(self, e):
		if e.mimeData().hasUrls():
			e.accept()
			for url in e.mimeData().urls():
				path = url.toLocalFile()
				self.setText(path)
		else:
			e.ignore()



#Instancia para iniciar una aplicacion 
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Muestra la ventana
_ventana.show()
# Ejecutar la aplicacion
app.exec_()
