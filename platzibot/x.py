import openai 
from tkinter import*

print('Extración de datos para DataNova')

#Creamos una función que abstraiga los datos de openai

openai.api_key = ''

def openai(prompt, engine = 'text-davinci-003',temperature = 0.9,max_tokens = 300,):
    response = openai.Completion.create(
                                        engine = engine,
                                        prompt = prompt,
                                        temperature = temperature,
                                        max_tokens = max_tokens,

    )
    return response.choice[0].text.strip()

# Luego hacemos la función que crea el código de tkinter

aplicacion = Tk()
aplicacion.geometry('700x700')

cabidad1 = Label(aplicacion, text= 'Chat made in DataNova', fg= 'white', bg= 'black', justify= CENTER)
cabidad1.pack(fill = BOTH,expand= False)

cabidad2 = Label(aplicacion,)




aplicacion.mainloop()
