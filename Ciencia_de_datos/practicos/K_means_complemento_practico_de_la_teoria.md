## Ejercitacion_k_means_teorico



**Paso 0:** Importar las bibliotecas

```python3
# %matplotlib inline
import pandas as pd #Pandas para usar dataframes
import matplotlib.pyplot as plt #Para graficar
import matplotlib.cm as cm #Para graficar el silhouette
import seaborn as sns #Para graficar
import numpy as np #Para realizar operaciones númericas con matrices y arrays
from sklearn import datasets #sklearn es LA biblioteca de machine learning de python
from sklearn.cluster import KMeans, DBSCAN #Para usar kmeans
from sklearn.preprocessing import StandardScaler #Para estandarizar nuestros datos
from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
from sklearn.cluster import AgglomerativeClustering #Para clustering jerárquico
from sklearn.metrics import pairwise_distances #Para las distancias a pares
from scipy.cluster.hierarchy import dendrogram, cophenet, linkage #Para graficar los dendrogramas y calcular el coeficiente cofenetico
from scipy.cluster import hierarchy #Para graficar los dendrogramas
from scipy.spatial.distance import pdist #Para calcular la distancia con el coeficiente cofenetico
import community as community_louvain #Para louvain
import networkx as nx #Para grafos
```

**Paso 1:** cargar los datos

```python3
stock_data = pd.read_csv("dataset_clustering_teorico.csv")
stock_data.head()
```

**Paso 1** Inspeccioná el DataFrame y caracterizalo



**Paso 2** Normaliza los datos y guardálos en una variable llamada stock_data_normalizado



**Paso 3** Aplicá el método k-means usando k=14



**Paso 4** Evaluá tus resultados
