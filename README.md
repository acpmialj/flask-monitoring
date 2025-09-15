# flask-monitoring
Ejemplo de integración Flask + Prometheus + Grafana. Para ejecutarlo, clonar este repositorio, cambiar al directorio "~/flask-monitoring" y seguir las instrucciones aquí dadas. 

## Presentación
Tenemos una aplicación web basada en Flask, que incluye un exportador de métricas (cliente) Prometheus. También tenemos un servidor Prometheus configurado para recopilar (scrape) las métricas de la aplicación Flask. Por último, tenemos un servidor Grafana que podemos usar, a través de su webUI, para visualizar la información de la aplicación web. 

## Elementos

Docker compose lee el manifiesto "compose.yaml" y hace las siguientes cosas:

### 1. Aplicación Flask
Construye una imagen para contenedores con Flask instalado, que ejecutan una aplicación server.py, con soporte Prometheus activado. En el directorio ./api está todo lo necesario: el Dockerfile, los requisitos para la app (requirements.txt), y la app propiamente dicha (server.py).

Lanza una instancia de esta aplicación, que expone su API usando http://flask-api:5000. Desde el anfitrión, su URL es http://localhost:5000. 

### 2. Prometheus
Lanza un contenedor Prometheus. El fichero ./monitoring/prometheus.yml contiene la configuración necesaria para un "scraper" de la aplicación Flask (de nombre flask-api, puerto 5000).

Prometheus está accesible en http://example-prometheus:9090. También se puede acceder desde la máquina anfitriona con http://localhost:9090, para observar las métricas que recibe. Por ejemplo:

```
# HELP flask_exporter_info Information about the Prometheus Flask exporter
# TYPE flask_exporter_info gauge
flask_exporter_info{version="0.23.1"} 1.0
# HELP flask_http_request_duration_seconds Flask HTTP request duration in seconds
# TYPE flask_http_request_duration_seconds histogram
flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_count{method="GET",path="/data",status="200"} 8.0
flask_http_request_duration_seconds_sum{method="GET",path="/data",status="200"} 0.002831260000675684
...
```

### 3. Grafana
Lanza un contenedor Grafana. La configuración del contenedor está en ./monitoring/config.monitoring. Grafana está accesible en la máquina anfitriona como http://localhost:3000.

Las credenciales de acceso son admin/pass@123

En las fuentes de datos, se debe añadir una de tipo Prometheus, que por omisión se llamará "prometheus". Solo es necesario configurar el URL de acceso, que es http://example-prometheus:9090.

Después se pueden importar paneles. Desde la máquina anfitriona (que es donde se ejecuta el navegador) podemos añadir el panel que está en ./monitoring/flaskapp_dashboard.json. También se puede copiar y pegar en el recuadro correspondiente de Grafana. Usará la fuente de datos configurada en el paso anterior. 

## Puesta en marcha, paso a paso

1. Ejecutar "docker compose up -d"
2. Acceder a la webUI de Grafana http://localhost:3000 (admin/pass@123)
3. Configurar en Grafana la fuente de datos e importar el panel
4. Generar actividad en la aplicación Flask, accediendo repetidamente a http://localhost:5000 (usar el botón "cargar página de nuevo" del navegador)
5. Comprobar los cambios en el panel de Grafana. No son inmediatos, esperar unos segundos

## Parada
Ejecutar "docker compose down"

## Prueba del API
```
curl http://localhost:5000
"Accessing root"
curl -X GET http://localhost:5000/data
"Reading data"
curl -X POST -d '{"data": "algodeinfo"}' -H "Content-Type: application/json" http://localhost:5000/data
"Added record: algodeinfo"
curl -X DELETE localhost:5000/data/4
"Deleting record 4"
```