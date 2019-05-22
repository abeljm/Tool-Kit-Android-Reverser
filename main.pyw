#-*- coding: utf-8 -*-
import sys
import os 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5 import uic 

# Clase heredada de QMainWindow (constructor de ventanas)
class Ventana(QMainWindow):
	# Metodo constructor de la clase
	def __init__(self):
		QMainWindow.__init__(self)
		# Cargar la configuracion del archivo .ui en el objeto
		uic.loadUi("MenuToolAndroid.ui", self)
		self.BAbrir.clicked.connect(self.archivo)
		self.BBorrar.clicked.connect(self.lineEdit.clear)
		self.BDescompilar.clicked.connect(self.descompilar)
		self.BCompilar.clicked.connect(self.compilar)

    # Evento para cerrar la aplicacion
	def closeEvent(self, event):
	  resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
	  if resultado == QMessageBox.Yes: event.accept()
	  else: event.ignore()

    # funcion que abrira el apk
	def archivo(self):
		# abrimos el archivo y ponemos como filtro que sea solo con extension apk 
	    fileName = QFileDialog.getOpenFileName(self, 'Selecciona el archivo', '','Archivos APK(*.apk)')	    
	    self.lineEdit.setText(fileName[0])
	    

	def descompilar(self):
	    global archivo
	    global carp_desc
	    global apktool
	    archivo = self.lineEdit.text()
	    carp_desc = archivo.replace('.apk','')
	    apktool = 'herramientas\\apktool.jar'
	    os.system('java -jar ' + apktool + ' d ' + archivo + ' -o ' + carp_desc)
	    QMessageBox.information(self, 'Informacion', 'Genial, Archivo descompilado', QMessageBox.Ok)

	def compilar(self):		
		nombre_archivo = os.path.basename(archivo)		
		new_nombre_archivo = 'new_' + nombre_archivo
		new_archivo = archivo.replace(nombre_archivo, new_nombre_archivo)		
		#print('java -jar ' + apktool + ' b ' + carp_desc + ' -o ' + new_archivo)
		os.system('java -jar ' + apktool + ' b ' + carp_desc + ' -o ' + new_archivo)
		#print('termino....')
		QMessageBox.information(self, 'Informacion', 'Genial, Archivo Compilado', QMessageBox.Ok)




#Instancia para iniciar una aplicacion 
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Muestra la ventana
_ventana.show()
# Ejecutar la aplicacion
app.exec_()
