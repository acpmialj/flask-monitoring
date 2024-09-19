# flask-monitoring
Flask + Prometheus + Grafana

## Elementos

El manifiesto "compose.yaml" hace las siguientes cosas

* Construye una imagen para contenedores con Flask instalado, que ejecutan una aplicación server.py, con soporte Prometheus activado

En el directorio ./api está todo lo necesario: el Dockerfile, los requisitos para la app (requirements.txt), y la app propiamente dicha (server.py)

La aplicación está disponible en http://flask-api:5000

* Lanza un contenedor Prometheus

El fichero ./monitoring/prometheus.yml contiene la configuración necesaria para un "scraper" de la aplicación Flask (de nombre flask-api, puerto 5000).

Prometheus está accesible en http://example-prometheus:9090

* Lanza un contenedor Grafana

La configuración del contenedor está en ./monitoring/config.monitoring

Grafana está accesible en la máquina anfitriona como http://example-grafana:3000

Las credenciales de acceso son admin/pass@123

En las fuentes de datos, se debe añadir una llamada exactamente "Prometheus" (con la P mayúscula), de tipo Prometheus. El URL de acceso será http://example-prometheus:9090

Después se pueden añadir paneles. Desde la máquina anfitriona (que es donde se ejecuta el navegador) podemos añadir el panel que está en ./monitoring/grafana_dashboard.json




