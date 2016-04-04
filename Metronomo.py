import numpy as np
import math

class metronomo:
    def __init__(self, nota, tempo, metrica):
        self.nota = nota
        self.tempo = tempo
        self.metrica = metrica
        self.tiempo = float(60/float(tempo))


    def metrono(self):
        array = []
        
        note=0
        if self.nota == 'C':
            note=261.63
        if self.nota  == 'C#':
            note=277.18
        if self.nota  == 'D':
            note=293.66
        if self.nota  == 'D#':
            note=211.13
        if self.nota  == 'E':
            note=329.63
        if self.nota  == 'F':
            note=349.23
        if self.nota  == 'F#':
            note=369.99
        if self.nota  == 'G':
            note=392
        if self.nota  == 'G#':
            note=415.3
        if self.nota  == 'A':
            note=440
        if self.nota  == 'A#':
            note=466.16
        if self.nota  == 'B':
            note=493.88


        if self.metrica == '24.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val

        if self.metrica == '34.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '44.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '54.wav':
            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*self.tiempo)):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '28.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '68.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '78.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)


            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


        if self.metrica == '98.wav':
            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)


            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*0.001)):
                valores = math.sin((2*math.pi*0*i)/44100.0)
                array.append(valores)

            for i in range(0, int(44100*(self.tiempo/2.0))):
                valores = math.sin((2*math.pi*note*i)/44100.0)
                array.append(valores)

            val= np.asanyarray(array)
            return val


    def niveldeaudio(self, nivel, info):
                VaP=max(abs(info))
                valornivel=(10**(nivel/20.0))*((2**16)/2)
                valorajustado=valornivel/float(VaP)
                infoajustada=info*valorajustado
                return infoajustada
