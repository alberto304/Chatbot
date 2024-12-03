import random
import json
import pickle
import numpy as np
import tkinter as tk
from tkinter import *

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

lemmatizer = WordNetLemmatizer()

#Importamos los archivos generados en el código anterior
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

#Pasamos las palabras de oración a su forma raíz
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

#Convertimos la información a unos y ceros según si están presentes en los patrones
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]=1
                if True:
                    print ("found in bag: %s" % w)
    print(bag)
    return np.array(bag)

#Predecimos la categoría a la que pertenece la oración
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_index = np.where(res ==np.max(res))[0][0]
    category = classes[max_index]
    return category

#Obtenemos una respuesta aleatoria
#Revisar porque es diferente al visto en la web
def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i["tag"]==tag:
            result = random.choice(i['responses'])
            break
    return result

def respuesta(message):
    ints = predict_class(message)
    res = get_response(ints, intents)
    return res

patterns_despedida = [intent["patterns"] for intent in intents["intents"] if intent["tag"] == "despedida"][0]


'''
while True:
    message = input()
    if predict_class(message) == "despedida":
        print(respuesta(message))
        break
    else:
        print(respuesta(message))
'''

def send():
    msg = EntryBox.get("1.0",'end-1c').strip() # Se obtiene el texto del EntryBox
    EntryBox.delete("0.0",END) # Se limpia el EntryBox
    if msg: # Si existe mensaje o no es vacío
        ChatLog.config(state=tk.NORMAL) # Habilitar edición en ChatLog
        ChatLog.insert(END, "You: " + msg + '\n\n') # Mostrar mensaje del usuario
        ChatLog.config(foreground="#442265", font=("Verdana", 12 )) # Configuración del Chat
        
        res = respuesta(msg) # Obtención de la respuesta del Bot
        ChatLog.insert(END, "Bot: " + res + '\n\n') # Mostrar respuesta del bot
        ChatLog.config(state=tk.DISABLED) # Deshabilitar edición en ChatLog
        ChatLog.yview(END) # Desplazar la vista al final del ChatLog

# Crear la ventana principal
base = tk.Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=False, height=False)

# Crear ventana de chat
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", wrap=tk.WORD)
ChatLog.config(state=tk.DISABLED)

# Crear barra de desplazamiento
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

# Crear botón para enviar mensaje
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Enviar", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg="#ffffff", command=send)

# Crear cuadro de entrada para mensajes
EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial", wrap=tk.WORD)

# Posicionar todos los componentes en la ventana
scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

# Iniciar bucle principal de Tkinter
base.mainloop()