# Chatbot
El Chatbot realizado funciona con Inteligencia Artificial, donde recibe distintos parámetros de diferentes tipos de mensajes del archivo llamado intents.json. La siguiente parte se realiza en el archivo training.py, donde se estructuran los datos en función de 0 o 1 y se realiza un modelo de red neuronal, formado por 3 capas. Finalmente, en el archivo chatbot.py se realiza el mismo proceso con un mensaje introducido por el usuario y donde se realiza una predicción de la respuesta a este mensaje en base al modelo de red neuronal creado anteriormente, todo esto aparecerá en una especia de interfaz de chat creada con tkinter.

Para el funcionamiento de la aplicación, se tendrán que seguir los siguientes pasos:
  1. La creación y edición de los patrones de entrada y respuestas en el archivo intents.json
  2. Entrenar el modelo en el archivo training.py, modificando los parámetros adecuados en el modelo y el optimizador
  3. Ejecución del archivo chatbot.pyy.
