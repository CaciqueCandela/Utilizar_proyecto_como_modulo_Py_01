import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");

'''En resumen, este código toma un DataFrame, identifica los países principales según el valor
en una columna específica, asigna colores a ciertos países de acuerdo con una lista proporcionada
y luego crea un gráfico de barras utilizando Seaborn para visualizar estos datos. El gráfico
resultante muestra la región de América Latina en un contexto global.
'''

def top_countries(df:pd.DataFrame, countries_for_hue:list, number_top = 20):
    top_countries_df = (
    df
    .select_columns(["country_region", "value"])
    .groupby(["country_region"])
    .aggregate("sum")
    .sort_values("value", ascending=False)
    .reset_index()
    .head(number_top)
    .transform_column(
        column_name="country_region",
        function=lambda x: "red" if x in countries_for_hue else "lightblue",
        dest_column_name="color"
        )
    )
    return top_countries_df

def plot_top_countries(*args, **kargs):
    top_countries_df = top_countries(*args,**kargs)

    sns.barplot(
        data=top_countries_df,
        x="value",
        y="country_region",
        hue="color",  
        legend=False
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");


'''
función top_countries:

- Toma un DataFrame (df), una lista de países para el parámetro countries_for_hue, y un número
opcional (number_top, con valor predeterminado de 20).
- Selecciona las columnas "country_region" y "value" del DataFrame.
- Agrupa los datos por "country_region" y suma los valores.
- Ordena el DataFrame resultante por el valor en orden descendente.
- Toma los primeros number_top registros.
- Transforma la columna "country_region" utilizando una función lambda que asigna "red" si el país está en la lista countries_for_hue, y "lightblue" de lo contrario.
- Devuelve el DataFrame resultante.

función plot_top_countries:

- La función recibe argumentos posicionales *args y argumentos de palabra clave **kargs, pero no
los utiliza directamente en el código proporcionado.
Llama a otra función llamada top_countries con los mismos argumentos que recibió (*args y
**kargs) y almacena el resultado en top_countries_df.
- Llama a la función top_countries con los argumentos proporcionados y guarda el resultado en
top_countries_df.
- Utiliza Seaborn (sns) para crear un gráfico de barras (barplot).
- Configura el gráfico con el eje x como "value", el eje y como "country_region", y utiliza la
variable de tonalidad (hue) especificada por el parámetro "color".
Desactiva la leyenda del gráfico (legend=False).
Etiqueta los ejes x e y como "Value" y "Country Region" respectivamente.
Establece el título del gráfico como "Latam countries in a global context"
'''