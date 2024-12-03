# Chatbot
Este Chatbot utiliza Inteligencia Artificial para procesar mensajes. Los diferentes tipos de mensajes están definidos en el archivo intents.json, el cual contiene patrones de entrada y sus respectivas respuestas. En el archivo training.py, estos datos se convierten a una representación binaria (0 y 1) y se entrenan utilizando un modelo de red neuronal con 3 capas. Finalmente, en el archivo chatbot.py, se analiza un mensaje introducido por el usuario y se genera una predicción basada en el modelo entrenado. La interacción con el usuario se realiza a través de una interfaz gráfica creada con Tkinter.

Para el funcionamiento de la aplicación, se tendrán que seguir los siguientes pasos:
  1. Editar y personalizar los patrones de entrada y las respuestas en el archivo intents.json.
  2. Entrenar el modelo en el archivo training.py, ajustando los parámetros del modelo y el optimizador según sea necesario.
  3. Ejecución del archivo chatbot.py para probar el chatbot.
