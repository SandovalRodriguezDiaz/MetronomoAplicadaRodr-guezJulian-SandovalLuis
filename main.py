


from Metronomo import metronomo
from ejecutarmetronomo import reproductor
from archivametronomo import  file
from Tkinter import *
from Tkinter import Tk
import tkMessageBox
from grabar import Grabar
import pyaudio





def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # Creacion de la ventana

    ventana = Tk()



    ventana.title("Grabadora con Metronomo")

    audio1 = Grabar(CHUNK, FORMAT, CHANNELS, RATE)



    e = BooleanVar(ventana)
    e.set(False)
    f = BooleanVar(ventana)
    f.set(False)

    global arreglo1, mtr, d

    arreglo1 = []
    d = BooleanVar(ventana)
    d.set(False)


    # Uso de frames para organizar la ventana.
    frame1 = Frame(ventana)
    frame1.pack(side=TOP)
    frame2 = Frame(ventana)
    frame2.pack(side=TOP)
    frame3 = Frame(ventana)
    frame3.pack(side=TOP)
    frame4 = Frame(ventana)
    frame4.pack(side=TOP)
    frame5 = Frame(ventana)
    frame5.pack(side=TOP)
    frame6 = Frame(ventana)
    frame6.pack(side=TOP)







    # Creacion e insercion del cuadro de texto 1.
    cuadro= Label(frame1, fg="black", padx=15, pady=10, text="Ingrese el nombre del archivo:")
    cuadro.pack(side=LEFT)



    def metrica():

        if e1.get() == '' or e4.get() == '':

            tkMessageBox._show('Error', 'No ingreso todos los datos.')

        else:

            global mtr

            s=selec.get()

            mtr=str(s)
            mtr=mtr+'.wav'



            Gmetrono = metronomo(e4.get(),cuadro3.get(), mtr)
            Rmetro = Gmetrono.metrono()
            volrajustado=Gmetrono.niveldeaudio(cuadro5.get(), Rmetro)
            doc=file(44100,16,mtr)
            doc.archive(volrajustado)






    selec=IntVar()

    cuadro2= Radiobutton(frame5,text='2/4',value=24,variable=selec,command=metrica)
    cuadro2.pack(side=LEFT)

    cuadro6= Radiobutton(frame5,text='3/4',value=34,variable=selec,command=metrica)
    cuadro6.pack(side=LEFT)

    cuadro7= Radiobutton(frame5,text='4/4',value=44,variable=selec,command=metrica)
    cuadro7.pack(side=LEFT)

    cuadro8= Radiobutton(frame5,text='5/4',value=54,variable=selec,command=metrica)
    cuadro8.pack(side=LEFT)


    cuadro9= Radiobutton(frame5,text='2/8',value=28,variable=selec,command=metrica)
    cuadro9.pack(side=LEFT)

    cuadro10= Radiobutton(frame5,text='6/8',value=68,variable=selec,command=metrica)
    cuadro10.pack(side=LEFT)

    cuadro11= Radiobutton(frame5,text='7/8',value=78,variable=selec,command=metrica)
    cuadro11.pack(side=LEFT)

    cuadro12= Radiobutton(frame5,text='9/8',value=98,variable=selec,command=metrica)
    cuadro12.pack(side=LEFT)



    cuadro3= Scale(frame3, label='Tempo', orient=HORIZONTAL,width=10, length=250,from_=40,to=240)
    cuadro3.pack(side=TOP, padx=1,pady=1)


    cuadro4= Label(frame2, fg="black", padx=15, pady=10, text="Ingrese la nota base\nEN CIFRADO AMERICANO Y MAYUSCULA:")
    cuadro4.pack(side=LEFT)

    cuadro5= Scale(frame4, label='Volumen', orient=HORIZONTAL,width=10, length=250,from_=0,to=-20)
    cuadro5.pack(side=TOP, padx=1,pady=1)


    # Creacion e insercion de cuadro de entrada 1.
    e1 = Entry(frame1, bd=5, insertwidth=1)
    e1.pack(side=LEFT, padx=15, pady=10)


    e4 = Entry(frame2, bd=5, insertwidth=1)
    e4.pack(side=LEFT, padx=15, pady=10)








    mensaje1 = Label(frame5, fg='red', padx=15, pady=10, text='Grabando...')

    # Funcion activa mensaje y grabar

    def activasms1():
        if e1.get() == '' or e4.get() == '' or selec.get()==0:

            tkMessageBox._show('Error', 'No ingreso todos los datos.')
        else:

            global d

            d.set(True)
            e1.configure(state='disabled')
            audio1.inicio()
            mensaje1.pack(side=LEFT)
            while d.get():

                audio1.grabacion()
                ventana.update()


                if d.get() is False:
                    break

    def playM():

        global d, mtr

        d.set(True)


        sonido=reproductor(1024)
        Datos=sonido.open(mtr)
        sonido.start(Datos[0],Datos[1],Datos[2])
        sonido.play(Datos[3])
        sonido.closed()





    # Funcion desactiva mensaje y para de grabar.
    def desactivasms1():
        global d

        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        global  arreglo1
        arreglo1 = audio1.parar()

        audio1.creaAudio(e1.get())
        grabarButton1.pack_forget()
        metroButton1.pack_forget()
        pararButton1.pack_forget()





    def reproduccion1():
        audio1.reproduce(e1.get())




    grabarButton1 = Button(frame6, padx=30, pady=2, text="Grabar", command=activasms1)
    grabarButton1.pack(side=LEFT)

    metroButton1 = Button(frame6, padx=30, pady=2, text="Metronomo", command=playM)
    metroButton1.pack(side=LEFT)

    pararButton1 = Button(frame6, padx=30, pady=2, text="Parar", command=desactivasms1)
    pararButton1.pack(side=LEFT)

    reproducirButton1 = Button(frame6, padx=20,pady=2, text="Reproducir", command=reproduccion1)
    reproducirButton1.pack(side=RIGHT)



    ventana.mainloop()

if __name__ == "__main__":
    main()