# Datos Cámara de Diputados de Chile

En este repositorio se analizarán las votaciones de la cámara de diputados en el periodo 2018-presente.

Los datos son descargados desde la plataforma de transparencia de la [Camara de Diputados](www.camara.cl)

## Obtención de votaciones por año
Para obtener la lista de votaciones de un año en particular usamos la siguiente URL, con el metodo `GET`
```
http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionesXAnno?prmAnno=2018
```
donde `2018` puede ser cualquier año.

