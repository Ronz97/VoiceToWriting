# vai converter audio em escrita
#Instalar as Bibliotecas : SpeechRecognition e PyAudio
#PyAudio : install pyaudio seu_sistema_operativo
import  speech_recognition as sr
from googletrans import Translator
trans = Translator()
rec = sr.Recognizer()
print(sr.Microphone.list_microphone_names()) #microphones que esta conectado no pc
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic) # eliminar o ruido do microfone
    print('Pode falar')
    audio = rec.listen(mic) # falar
    text = rec.recognize_google(audio, language='pt') #Tranformar audio em texto em portugues
    print(text)
    print(trans.translate(text,dest='en').text) #traduzir para ingles
