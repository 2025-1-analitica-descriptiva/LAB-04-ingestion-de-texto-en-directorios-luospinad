# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import os
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    
    input_path = 'files/input'
    output_path = 'files/output'

    sets_lista = {
        "train": [],
        "test": []
    }
        
    target_lista = ['neutral', 'positive', 'negative']

    current_df = ''
    current_target = ''

    # Leer cada carpeta dentro de input
    
    for root, dirs, files in os.walk(input_path):

        folder_name = os.path.basename(root)
        
        # si la carpeta es test o train guardamos para seleccionar el dataset
        if (folder_name == 'test' or folder_name == 'train'):
            current_df = folder_name

        if (folder_name in target_lista):
            current_target = folder_name

        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                contenido = f.read().replace('\n', ' ')

            # despues de leer el contenido de cada archivo lo guardamos en el dataset correcto con su target
            if (current_df != '' and current_target != ''):
                sets_lista[current_df].append({
                    "phrase": contenido,
                    "target": current_target
                })


    #Crear carpeta output si no existe
    os.makedirs(output_path, exist_ok=True)

    for name, data in sets_lista.items():
        df = pd.DataFrame(data)
        df.reset_index(inplace=True)
        df.to_csv(os.path.join(output_path, f'{name}_dataset.csv'), index=False)




if __name__ == "__main__":
    pregunta_01()