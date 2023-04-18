import pandas as pd
import random
import PySimpleGUI as sg

movies_df = pd.read_csv("C:/Users/Hector/OneDrive/Documents/ROBOTICA FINAL/movies.csv")


def recomendar_pelicula(genre):
    peliculas_filtradas = movies_df[movies_df['genres'].str.contains(genre, case=False)]
    if peliculas_filtradas.empty:
        return "Lo siento, no hay películas de ese género en nuestra base de datos"
    else:
        pelicula = peliculas_filtradas.sample()
        return pelicula['title'].values[0]


# Ventana principal
sg.theme('BlueMono')
layout = [    [sg.Text('¡Bienvenido a nuestro recomendador de películas!', font=('Arial', 14))],
    [sg.Text('Por favor, responde a las siguientes preguntas para recibir tu recomendación personalizada.', font=('Arial', 12))],
    [sg.Text('')],
    [sg.Text('¿Qué género de película te gustaría ver hoy?', font=('Arial', 12)), sg.InputText(key='genre')],
    [sg.Button('Agregar otro género', key='add_genre'), sg.Button('Recomendar')],
    [sg.Text('')],
    [sg.Button('Recomendar película aleatoria')],
    [sg.Text('')],
    [sg.Button('Salir', key='exit')],
    [sg.Text('')],
    [sg.Text('Recomendaciones', font=('Arial', 12))],
    [sg.Listbox([], size=(40, 8), key='recomendaciones')],
    [sg.Button('Me gusta'), sg.Button('No me gusta')],
    [sg.Text('')],
    [sg.Text('Lista de películas que te gustan', font=('Arial', 12))],
    [sg.Listbox([], size=(40, 8), key='peliculas_gustan')],
    [sg.Button('Eliminar')]
]




window = sg.Window('Películas', layout)
pelicula_recomendada = ''
peliculas_gustan = []

# Bucle principal
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'exit':
        sg.popup("Esperemos que disfrutes estas películas con amor Los Roboticos", font=("Arial", 20))
        break


    elif event == 'Recomendar':
        genero = values['genre']
        pelicula_recomendada = recomendar_pelicula(genero)
        window['recomendaciones'].update(values=[pelicula_recomendada])

    elif event == 'Recomendar película aleatoria':
        pelicula_recomendada = movies_df.sample()['title'].values[0]
        window['recomendaciones'].update(values=[pelicula_recomendada])

    elif event == 'Me gusta':
        seleccion = window['recomendaciones'].get()
        if seleccion:
            peliculas_gustan.append(seleccion[0])
            sg.popup(f'¡Te ha gustado {seleccion[0]}!')
            window['peliculas_gustan'].update(values=peliculas_gustan)

    elif event == 'No me gusta':
        seleccion = window['recomendaciones'].get()
        if seleccion:
            pelicula = seleccion[0]

    if event == 'Eliminar':

        seleccion = window['peliculas_gustan'].get()

        if seleccion:
            peliculas_gustan.remove(seleccion[0])

            window['peliculas_gustan'].update(values=peliculas_gustan)


    elif event == 'Agregar otro genero':

        otro_genero = sg.popup_get_text('¿Cuál es el otro género de película que te gustaría ver?')

        pelicula_recomendada = recomendar_pelicula(otro_genero)

        window['recomendaciones'].update(values=[pelicula_recomendada])


    elif event == "add_genre":

        new_genre = sg.popup_get_text("¿Cuál es el otro género de película que te gustaría ver?")

        if new_genre:
            values["genre"] += f", {new_genre}"


    elif event == 'Eliminar seleccion':

        seleccion = window['peliculas_gustan'].get()

        if seleccion:
            peliculas_gustan.remove(seleccion[0])

            window['peliculas_gustan'].update(values=peliculas_gustan)
