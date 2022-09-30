#Importando librerías a usar
import pyttsx3
import time
import webbrowser as wb
import os
import pywhatkit

#Solicitando hora mediante python
hora = time.strftime("%H")
hora = int(hora)

#Condicional para determinar si es día,tarde o noche
if hora<=12:
    hour = "buenos días"
elif hora>12 and hora<=19:
    hour = "buenas tardes"
elif hora>19:
    hour = "buenas noches"

#Saludo de bienvenida
engine = pyttsx3.init()
engine.say("Hola creador, "+ hour)
engine.say("Preparado y listo para recibir instrucciones señor")
x=engine.runAndWait()
print(x)

#Ejecucion y proceso de los comandos de voz realizados
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es")
        print(text)
        if text == "Google":
            wb.open("https://www.google.com/")
            pyttsx3.speak("Abriendo google")
        elif text == "WhatsApp":
            wb.open("https://web.whatsapp.com/")
            pyttsx3.speak("Abriendo WhatsApp")
        elif text == "Facebook":
            wb.open("https://www.facebook.com/")
            pyttsx3.speak("Abriendo Facebook")
        elif text == "YouTube":
            wb.open("https://www.youtube.com/")
            pyttsx3.speak("Abriendo Youtube")
        elif text == "celebración":
            wb.open("https://www.youtube.com/watch?v=9jK-NcRmVcw")
            pyttsx3.speak("Felicidades amo, eres un grande y estoy orgulloso de ti. Disfruta de tu canción, te la ganaste bro")
        else:
            pyttsx3.speak("Lo siento puedes volver a repetirlo por favor")
    except:
        pyttsx3.speak("No te puede entender")

#Envio de mensajes vía whatsapp
try:
    hola = pyttsx3.speak("Desea enviar algun mensaje señor")
    print(hola)
    if hola=="Sí" or hola=="Si":
        pyttsx3.speak("A continuación ingrese el numero telefónico de su contacto")
        contacto=input(int("Ingrese su numero telefónico de su contacto, recuerde ingresar el +51"))
        pyttsx3.speak("Ingrese el contenido de su mensaje usando el comando de voz")
        mensaje = r.recognize_google(audio, language="es")
        print(mensaje)
        pywhatkit.sendwhatmsg_instantly(contacto, mensaje)
    else:
        pyttsx3.speak("Entendido, ejecute de nuevo el programa en caso me necesite")
except:  
    pyttsx3.speak("Entendido, ejecute de nuevo el programa en caso me necesite")          
        
     
        
            