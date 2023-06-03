# Lab5_Robotica
Desarrollo e implementación del laboratorio 5 de robótica


Daniel Felipe Cantor Santana

Juan David Morales Restrepo

David Leonardo Cocoma Reyes

# 1) Requisitos
Para el desarrollo de esta práctica del laboratorio,se necesita lo siguiente:
  - Ubuntu versión 20.xx preferible 20.04 LTS con ROS.
  - Espacio de trabajo para catkin correctamente configurado.
  - Paquetes de Dynamixel Workbench. 
  - Paquete del robot Phantom X.
  - Marcadores borrables.
  - Toolbox de robótica de Peter Corke.
  - Un manipulador Phantom X Pincher con su base en madera.


# 2) Análisis: Cinemática Inversa

Para la solución de esta práctica es necesario realizar un modelo de cinemática inversa para el Phantom X de manera que se puedan obtener via-points para cada una de las rutinas las cuales son:
  - Cargar herramienta: El brazo se moverá para sujetar el marcador y esperar el siguiente comando.
  - Espacio de trabajo: El brazo dibujará 2 arcos, al máximo radio que alcanza y el mínimo radio, de esta manera se puede obserbar el rango de trabajo del brazo.
  - Dibujar iniciales: El brazo dibujará las iniciales de los miembros del equipo en el espacio del trabajo.
  - Dibujar figura: El brazo dibujará un corazón en el espacio del trabajo.
  - Dejar herramienta: El brazo se moverá para soltar el marcador en la base y se moverá a la posición de home.

# 3) HMI en Python
Para lograr el desarrollo del laboratorio, se realizó una HMI, empleando el paquete tkinter. 
Dicha HMI es capaz de indicar una serie de rutinas al brazo, en el primer frame de la parte superior se evidencia la información personal de los autores del laboratorio y el logo de la Universidad Nacional de Colombia.

El segundo frame envía las distintas rutinas al Phantom X, a la izquierda se puede seleccionar una de las 5 rutinas estipuladas en el laboratorio y cuenta con el botón de enviar a la derecha para enviar la instrucción, a la derecha se puede observar el tiempo total que tomó realizar la última rutina y debajo de este se muestra el estado de la herramienta cargada o descargada.

En el Frame inferior se puede visualizar los datos en tiempo real enviados por el Phantom X de posición en grados, cuenta con un botón de actualizar para iniciar la conección y leer los datos, estos se muestran en orden desde la articulación 1 hasta la 5 en forma de lista.

El archivo "HMI.py" se encuentra adjunto en este repositorio. El procedimiento de su funcionamiento es el siguiente:
   - Se inicializa el ROS mediante el comando roslaunch el codigo one_controller.launch del paquete dynamixel_one_motor
   - Se ejecuta la HMI y se puede empezar a manipular el Phantom X
   - El usuario debe darle la instrucción de tomar el marcador al brazo, de otra manera el brazo no reaccionará al resto de rutinas.
   - Cuando se envía la instrucción de movimiento, se llama la función joint_publisher() a la cual le ingresan los valores correspondientes de cada articulación por medio de un archivo txt que contine una lista con todos los puntos necesarios para la rutina  y mediante el comando joint_trajectory se crea un nodo llamado joint_publisher que empezará a enviar estos datos al Phantom X y finalmente se verá el movimiento reflejado en el mecanismo.
   - A continuación se puede empezar a leer los datos de posición del Phantom X pulsando el botón Actualizar de la parte inferior, este botón llama la función listener() la cual iniciliza el nodo 'joint_listener' que utiliza el script "joint_states" del paquete dynamixel_workbench para obtener los datos de posición, estos son tomados en la función callback() y se convierten de radianes a grados para agregarlos al Treeview y mostrarlos en tiempo real

Se tomó como base los archivos presentes en el paquete de Dynamixel "jointPub.py", "jointSub.py" y "jointSrv.py"  y el archivo "basic.yalm" se modificó, para agregar los 4 joints faltantes.

Esta HMI se diferencia de la del laboratorio pasado, en 3 características:



# 4) Video de implementación
A continuación se presenta el video donde se evidencia el funcionamiento de la interfaz gráfica y las diferentes rutinas del brazo.


# Tomar herramienta
[![Alt text](https://i9.ytimg.com/vi_webp/w0KtlU8nmic/mq1.webp?sqp=CLyj6qMG-oaymwEmCMACELQB8quKqQMa8AEB-AHOBYACgAqKAgwIABABGH8gFigdMA8=&rs=AOn4CLBySHaAW_QSTVU5JlM34KWNhg_G-g)](https://youtube.com/shorts/4Q69lODFn5Y?feature=share)\

# Arcos
[![Alt text](https://i9.ytimg.com/vi_webp/w0KtlU8nmic/mq1.webp?sqp=CLyj6qMG-oaymwEmCMACELQB8quKqQMa8AEB-AHOBYACgAqKAgwIABABGH8gFigdMA8=&rs=AOn4CLBySHaAW_QSTVU5JlM34KWNhg_G-g)](https://youtu.be/w0KtlU8nmic)
# Corazón
[![Alt text](https://i9.ytimg.com/vi_webp/w0KtlU8nmic/mq1.webp?sqp=CLyj6qMG-oaymwEmCMACELQB8quKqQMa8AEB-AHOBYACgAqKAgwIABABGH8gFigdMA8=&rs=AOn4CLBySHaAW_QSTVU5JlM34KWNhg_G-g)](https://youtu.be/BSI8GYFt1AM)
# Letras
[![Alt text](https://i9.ytimg.com/vi_webp/w0KtlU8nmic/mq1.webp?sqp=CLyj6qMG-oaymwEmCMACELQB8quKqQMa8AEB-AHOBYACgAqKAgwIABABGH8gFigdMA8=&rs=AOn4CLBySHaAW_QSTVU5JlM34KWNhg_G-g)](https://youtu.be/c9Hd1wuyeSQ)
# Descargar Herramienta  
[![Alt text](https://i9.ytimg.com/vi_webp/w0KtlU8nmic/mq1.webp?sqp=CLyj6qMG-oaymwEmCMACELQB8quKqQMa8AEB-AHOBYACgAqKAgwIABABGH8gFigdMA8=&rs=AOn4CLBySHaAW_QSTVU5JlM34KWNhg_G-g)](https://youtube.com/shorts/QDx7kIwt_BA?feature=share)
# Funcionamiento HMI
[![Alt text](https://i9.ytimg.com/vi_webp/w0KtlU8nmic/mq1.webp?sqp=CLyj6qMG-oaymwEmCMACELQB8quKqQMa8AEB-AHOBYACgAqKAgwIABABGH8gFigdMA8=&rs=AOn4CLBySHaAW_QSTVU5JlM34KWNhg_G-g)](https://youtube.com/shorts/vBoiy9MRuak?feature=share)
