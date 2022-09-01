## Ejercicio 4

Importar las bibliotecas

```python3
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
import numpy as np
from scipy import stats
```

Cargá la [siguiente tabla](https://raw.githubusercontent.com/AJVelezRueda/Fundamentos_de_informatica/master/Ciencia_de_datos/practicos/recursos/practico4.csv) e inspeccionala.
Caracterizala estadísticamente.
Limpiá la tabla de las posibles anomalías que pueda contener.
Escalá las columnas que sean necesarias obteniendo un nuevo dataframe con todos los datos numéricos pertinentes.
Una empresa quiere publicitar su producto por medio de los anuncios en las redes sociales, más precisamente quiere atraer a adultos jóvenes. Para esto, esta empresa tiene en su poder información de dudosa moralidad por la cuál puede saber, desde una IP dada, cuántas horas estuvo activa esta IP y cuales fueron las redes que usó. La idea original, para poder obtener una mayor ganancia, es largar de forma diferenciada los anuncios, de manera que las personas que entran poco a internet, pero cuyo tiempo se gasta en redes sociales, van a recibir mayor cantidad de anuncios. Se quiere saber entonces, si en base a los datos disponibles se pueden generar al menos dos grupos diferenciados para este fin. Elegí las dos columnas que creas útiles para esto y realizá un proceso de clustering para obtener los grupos correspondientes.
¿Cuántos grupos se formaron?
¿El proceso de clustering fue bueno?

<details>
  <summary>Código que te puede resultar útil</summary>
  
  > Distribución
  
  ```python
  sns.histplot(data = df, x = "columna", binwidth=10, kde = True)
  # el binwidth depende de la cantidad de datos, a mayor cantidad de datos, más grande el binwidth
  ``` 
  
  > Escalado

  ```python
  scaler = StandardScaler()
  df_escalado = scaler.fit_transform(df)
  ```
  
  > Inercias según número de grupos

  ```python
  def inercias_por_k():
    inercias = {}
    for i in range(1,11):
        kmeans = KMeans(n_clusters = i, init="random", n_init=10, max_iter=300, random_state=123457)
        kmeans.fit(df_escalado)
        inercias[i] = kmeans.inertia_
    return inercias
  ```

  > Silhouette

  ```python
  silhouette_avg = silhouette_score(df_escalado, kmeans.labels_)
  sample_silhouette_values = silhouette_samples(df_escalado, kmeans.labels_)

  def graficarSilhouette (k, labels, sample_silhouette_values, silhouette_avg):
    fig, ax1 = plt.subplots(1, 1)
    y_lower = 10
    for i in range(k):
        ith_cluster_silhouette_values = \
            sample_silhouette_values[labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / k)
        ax1.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax1.set_title("Plot del silhouette de cada cluster")
    ax1.set_xlabel("Coeficiente de silhouette")
    ax1.set_ylabel("Etiqueta del cluster")
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax1.set_yticks([])

  graficarSilhouette (k, kmeans.labels_, sample_silhouette_values, silhouette_avg)
  ```


</details>
