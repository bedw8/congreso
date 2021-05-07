# Datos Cámara de Diputados de Chile

En este repositorio contiene datos de las votaciones de la cámara de diputados en el periodo 2018-presente, para su posteriro análisis. Los datos son descargados desde la plataforma de transparencia de la [Camara de Diputados](www.camara.cl). Sin embargo estos vienen en fomrato XML, por lo que acá los guardaremos en fomrato CSV.

## Descarga de datos
Los scripts `DiputadosPA.py`, `ListaVotaciones.py` y `DetalleVotaciones.py` descargan los datos desde la API pública de la cámara de diputados y lo guardan en formato CSV.

- `DiputadosPA.py` descarga la lista de diputados del periodo actual
- `ListaVotaciones` descarga la lista de votaciones ocurridas durante los años 2018,2019 y 2020. Sin embargo, este script es facilmente editable para obtener las votaciones realizadas en otros años.
- `DetalleVotaciones.py` descarga el detalle de las votaciones. Este incluye una metadata variada, incluyendo un conteo explícito de los votos, señalando el voto de cada parlamentario.
