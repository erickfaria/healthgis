# healthgis (Work in progress !!!)

The project aims to automate the process of obtaining and analyzing health data in Brazil. The language adopted will be Python version 3.7 and the visualization will be using pyQGIS.

## Getting Started


### Prerequisites

System os

### Installing

First software to install it's QGIS software

```
sudo apt-get install qgis
```

Install Anaconda

```
sudo apt-get anaconda
```

# Geocode
```
install.packages("osrm")
library(osrm)
```

```
database <- read.table ("Diretório", header=TRUE, sep="\t") #Para os iniciantes em R ver as diferenças entre leituras de arquivo.
```

```
distancias <-osrmTable(loc = database[1:44, c("id","lon","lat")])
```

```
write.table(distancias, file = "matriz.txt", sep="\t")
```
