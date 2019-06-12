# TOOL KIT ANDROID REVERSER

_Es una herramienta que con un par de clicks Descompila, Compila y Firma de una manera sencilla archivos APK, con la ventaja de ser codigo 
libre por lo tanto se puede actualizar las herramientas las veces que se necesite y colaborar para su mejora._

### Pre-requisitos 📋

_Para correr la herramienta necesitas instalar Python 3.7.3 y PyQT5_

```
pip3 install PyQt5
```
_Y si quieres mejorar la interfaz_

```
pip3 install PyQt5-tools
```

### Instalacion 🔧

_Para correr la tool solo ejecuta en consola en el directorio del proyecto_

```
python main.py
```

### Ejecutando Took Kit Android Reverser ⚙️

#### Descompilar APK

_Al ejecutar la tool podemos descompilar el archivo apk arrastrandolo al edit desde cualquier directorio_

![Optional Text](https://github.com/abeljm/Tool-Kit-Android-Reverser/blob/master/imagenes/modulo1_a.jpg)

_Dando como resultado una carpeta con el nombre del APK_

![Optional Text](https://github.com/abeljm/Tool-Kit-Android-Reverser/blob/master/imagenes/modulo1_b.jpg)

#### Compilar APK

_Para compilar el APK solo nesecitamos presionar el boton compilar , el programa buscara una carpeta con el mismo nombre del APK y compilara un nuevo archivo con agregando al nombre new_(nombredelapk).apk_

![Optional Text](https://github.com/abeljm/Tool-Kit-Android-Reverser/blob/master/imagenes/modulo1_c.jpg)

_Con esto solo faltaria firma el nuevo archivo APK, pero esto se explica mas adelante._

#### Convertir APK, DEX a JAR

_Para convertir archivos DEX a JAR no hay necesidad de descomprimir el archivo APK, solo arrastremos dicho archivo desde cualquier directorio al edit y presionamos el boton Dex2Jar, como se muestra en la imagen_

![Optional Text](https://github.com/abeljm/Tool-Kit-Android-Reverser/blob/master/imagenes/modulo2_a.jpg)

#### Convertir JAR a DEX 

_De la misma manera que hicimos en el paso anterior arrastramos el archivo JAR en el edit y presionamos el boton Jar2Dex_

![Optional Text](https://github.com/abeljm/Tool-Kit-Android-Reverser/blob/master/imagenes/modulo2_b.jpg)

#### Firmar APK

_Para firmar solo nesecitamos arrastrar el archivo APK al edit y presionar el boton Firmar, nos crear una carpeta con el APK firmado_

![Optional Text](https://github.com/abeljm/Tool-Kit-Android-Reverser/blob/master/imagenes/modulo3_a.jpg)








