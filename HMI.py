from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time
import os

def reiniciar_cronometro():
    return time.time()

validar = False
ruta_absoluta = os.path.abspath("images")
rt2 = ruta_absoluta + "/Escudo_unal_2016.png"

root = Tk()
root.title("HMI")
root.config(bg="silver")
root.geometry("800x700")
root.geometry("+300+0")

global joint1pos, joint2pos,joint3pos,joint4pos,joint5pos

joint1pos = 0
joint2pos = 0
joint3pos = 0
joint4pos = 0
joint5pos = 0

dat1 = []
dat2 = []
dat3 = []
dat4 = []
dat5 = []


frame1 = LabelFrame(root, text="Controlador Phantom X", font=('Times', 20))
frame2 = LabelFrame(root, text="Configurar pose", font=('Times', 20))
frame3 = LabelFrame(root, text="Leer pose", font=('Times', 20))

frame1.pack(fill="both", expand="yes", padx=20, pady=10)
frame2.pack(fill="both", expand="yes", padx=20, pady=10)
frame3.pack(fill="both", expand="yes", padx=20, pady=10)


lbl1 = Label(frame1, text="Integrantes", font=('Times', 14))
lbl1.grid(column=0, row=0, padx=5, pady=3)
lbl1 = Label(frame1, text="David Leonardo Cocoma Reyes", font=('Times', 12))
lbl1.grid(column=0, row=1, padx=5, pady=3)
lbl1 = Label(frame1, text="Juan David Morales Restrepo", font=('Times', 12))
lbl1.grid(column=0, row=2, padx=5, pady=3)
lbl1 = Label(frame1, text="Daniel Felipe Cantor Santana", font=('Times', 12))
lbl1.grid(column=0, row=3, padx=5, pady=3)

etiquet = tk.Label(frame1, text=" ",width=15)
etiquet.grid(column=1, row=3, padx=5, pady=3)

lbl1 = Label(frame1, text="Correo unal", font=('Times', 14))
lbl1.grid(column=2, row=0, padx=5, pady=3)
lbl1 = Label(frame1, text="dcocoma", font=('Times', 12))
lbl1.grid(column=2, row=1, padx=5, pady=3)
lbl1 = Label(frame1, text="jumoralesr", font=('Times', 12))
lbl1.grid(column=2, row=2, padx=5, pady=3)
lbl1 = Label(frame1, text="dfcantors", font=('Times', 12))
lbl1.grid(column=2, row=3, padx=5, pady=3)

etiqueta = tk.Label(frame1, text=" ",width=15)
etiqueta.grid(column=3, row=3, padx=5, pady=3)
imagen2 = tk.PhotoImage(file=rt2)

etiqueta2 = tk.Label(frame1, image=imagen2)
#etiqueta2 = tk.Label(frame1, text="no c")
etiqueta2.grid(column=4, row=0,rowspan=4, padx=5, pady=3)


var1 = tk.IntVar()

pos1 = tk.Radiobutton(frame2,text="Tomar marcador",variable=var1,value=1,font=('Times', 12))
pos2 = tk.Radiobutton(frame2,text="Hacer radios",variable=var1,value=2,font=('Times', 12))
pos3 = tk.Radiobutton(frame2,text="Hacer letras",variable=var1,value=3,font=('Times', 12))
pos4 = tk.Radiobutton(frame2,text="Hacer figura",variable=var1,value=4,font=('Times', 12))
pos5 = tk.Radiobutton(frame2,text="Dejar marcador",variable=var1,value=5,font=('Times', 12))

pos1.grid(column=0, row=0, padx=5, pady=3)
pos2.grid(column=0, row=1, padx=5, pady=3)
pos3.grid(column=0, row=2, padx=5, pady=3)
pos4.grid(column=0, row=3, padx=5, pady=3)
pos5.grid(column=0, row=4, padx=5, pady=3)

cbtn = Button(frame2, text="Aceptar")
cbtn.grid(column=1, row=2, padx=5, pady=3)

act = Button(frame3, text="Actualizar")
act.pack()

etiqueta6 = tk.Label(frame2, text="                ")
etiqueta6.grid(column=6, row=0, padx=5, pady=3)

etiqueta3 = tk.Label(frame2, text="Tiempo ultima rutina: ")
etiqueta3.grid(column=7, row=1, padx=5, pady=3)

etiqueta5 = tk.Label(frame2, text="Herramienta: ")
etiqueta5.grid(column=7, row=2, padx=5, pady=3)

etiqueta4 = tk.Label(frame2, text=" ")
etiqueta4.grid(column=8, row=1, padx=5, pady=3)

etiqueta7 = tk.Label(frame2, text="Inactiva")
etiqueta7.grid(column=8, row=2, padx=5, pady=3)

trv = ttk.Treeview(frame3, columns=(1,2,3), show="headings", height="10")
trv.pack()

trv.heading(1, text="Joint", anchor="w")
trv.heading(2, text="Posicion actual",anchor="w")
trv.heading(3, text="Torque Enable", anchor="w")


#vamos ha hacer una lista con los archivos
nombre_archivo = ['tomar.txt','arcos.txt','letras.txt','figura.txt','dejar.txt']
#nombre_archivo = 'arcos.txt'
#nombre_archivo = 'letras.txt'
#nombre_archivo = 'figura.txt'
#nombre_archivo = 'dejar.txt'



def leer_archivo_txt(letras):
    filas = []
    columnas = []

    with open(nombre_archivo[0], 'r') as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            fila = linea.strip().split(',')
            filas.append(fila)
    return filas

def leer_archivo_txt1(letras):
    filas = []
    columnas = []

    with open(nombre_archivo[1], 'r') as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            fila = linea.strip().split(',')
            filas.append(fila)
    return filas
def leer_archivo_txt2(letras):
    filas = []
    columnas = []

    with open(nombre_archivo[2], 'r') as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            fila = linea.strip().split(',')
            filas.append(fila)
    return filas

def leer_archivo_txt3(letras):
    filas = []
    columnas = []

    with open(nombre_archivo[3], 'r') as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            fila = linea.strip().split(',')
            filas.append(fila)
    return filas

def leer_archivo_txt4(letras):
    filas = []
    columnas = []

    with open(nombre_archivo[4], 'r') as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            fila = linea.strip().split(',')
            filas.append(fila)
    return filas



def updateval(d1, d2, d3, d4, d5):
    dat1 = [1,round(d1,5),"Enable"]
    dat2 = [2,round(d2,5),"Enable"]
    dat3 = [3,round(d3,5),"Enable"]
    dat4 = [4,round(d4,5),"Enable"]
    dat5 = [5,round(d5,5),"Enable"]

    trv.insert("", "end", values=dat1)
    trv.insert("", "end", values=dat2)
    trv.insert("", "end", values=dat3)
    trv.insert("", "end", values=dat4)
    trv.insert("", "end", values=dat5)

def enviar_pose():
    inicio = reiniciar_cronometro()

    if var1.get() == 0:
        joint1pos = 0
        joint2pos = 0
        joint3pos = 0
        joint4pos = 0
        joint5pos = -90
        joint_publisher(parserad(joint1pos),parserad(joint2pos),parserad(joint3pos),parserad(joint4pos),parserad(joint5pos))
    elif var1.get() == 2:
        nombre_archivo = 'arcos.txt'  # Nombre del archivo de texto a leer
        filas = leer_archivo_txt1(nombre_archivo)
        
        for linea in filas:
            fila = linea
            joint1pos = float(fila[0])
            joint2pos = float(fila[1])
            joint3pos = float(fila[2])
            joint4pos = float(fila[3])
            joint5pos = float(fila[4])
            joint_publisher(joint1pos,joint2pos,joint3pos,joint4pos,joint5pos)
    elif var1.get() == 3:
        nombre_archivo = 'letras.txt'  # Nombre del archivo de texto a leer
        filas = leer_archivo_txt2(nombre_archivo)
        
        for linea in filas:
            fila = linea
            joint1pos = float(fila[0])
            joint2pos = float(fila[1])
            joint3pos = float(fila[2])
            joint4pos = float(fila[3])
            joint5pos = float(fila[4])
            joint_publisher(joint1pos,joint2pos,joint3pos,joint4pos,joint5pos)
    elif var1.get() == 4:
        nombre_archivo = 'figura.txt'  # Nombre del archivo de texto a leer
        filas = leer_archivo_txt3(nombre_archivo)
        
        for linea in filas:
            fila = linea
            joint1pos = float(fila[0])
            joint2pos = float(fila[1])
            joint3pos = float(fila[2])
            joint4pos = float(fila[3])
            joint5pos = float(fila[4])
            joint_publisher(joint1pos,joint2pos,joint3pos,joint4pos,joint5pos)
    elif var1.get() == 5:
        nombre_archivo = 'dejar.txt'  # Nombre del archivo de texto a leer
        filas = leer_archivo_txt4(nombre_archivo)
        for linea in filas:
            fila = linea
            joint1pos = float(fila[0])
            joint2pos = float(fila[1])
            joint3pos = float(fila[2])
            joint4pos = float(fila[3])
            joint5pos = float(fila[4])
            joint_publisher(joint1pos,joint2pos,joint3pos,joint4pos,joint5pos)
        etiqueta7.config(text="Inactiva")
    elif var1.get() == 1:
        nombre_archivo = 'tomar.txt'  # Nombre del archivo de texto a leer
        filas = leer_archivo_txt(nombre_archivo)
        for linea in filas:
            fila = linea
            joint1pos = float(fila[0])
            joint2pos = float(fila[1])
            joint3pos = float(fila[2])
            joint4pos = float(fila[3])
            joint5pos = float(fila[4])
            joint_publisher(joint1pos,joint2pos,joint3pos,joint4pos,joint5pos)
        etiqueta7.config(text="Activa")

    
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    etiqueta4.config(text=str(round(tiempo_transcurrido,2)) + " segundos")


def parserad(p):
    return p * 3.1416 / 180

def rad2deg(p):
    return p * 180 / 3.1416

def joint_publisher(p1,p2,p3,p4,p5):
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [p1,p2,p3,p4,p5]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(3)
        break

def callback(data):
    rospy.loginfo(data.position)
    trv.delete(*trv.get_children())
    updateval(data.position[0], (data.position[1]), (data.position[2]), (data.position[3]), data.position[4])
    trv.update()

    
    
def listener():
    #sub = rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.init_node('joint_listener', anonymous=True)
    #rospy.spin()
    #sub.unregister()
    rospy.signal_shutdown()

"""
def randompos():
    try:
        en1 = int(ent1.get())
        en2 = int(ent2.get())
        en3 = int(ent3.get())
        en4 = int(ent4.get())
        en5 = int(ent5.get())
    except ValueError as error:
        en1 = 0
        en2 = 0
        en3 = 0
        en4 = 0
        en5 = 0

    joint1pos = en1
    joint2pos = en2
    joint3pos = en3
    joint4pos = en4
    joint5pos = en5

    try:
        joint_publisher(parserad(en1),parserad(en2),parserad(en3),parserad(en4),parserad(en5))
    except rospy.ROSInterruptException:
        pass
"""
def tryListener():
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
    

cbtn.config(command=enviar_pose)
act.config(command = tryListener)

root.mainloop()