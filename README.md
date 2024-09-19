# flask-monitoring
Ejemplo de integración Flask + Prometheus + Grafana. 

Tenemos una aplicación web basada en Flask, que incluye un exportador de métricas (cliente) Prometheus. También tenemos un servidor Prometheus configurado para recopilar (scrape) las métricas de la aplicación Flask. Por último, tenemos un servidor Grafana que podemos usar, a través de su webUI, para visualizar la información de la aplicación web. 

## Elementos

El manifiesto "compose.yaml" hace las siguientes cosas

### 1. Aplicación Flask
Construye una imagen para contenedores con Flask instalado, que ejecutan una aplicación server.py, con soporte Prometheus activado

En el directorio ./api está todo lo necesario: el Dockerfile, los requisitos para la app (requirements.txt), y la app propiamente dicha (server.py)

La aplicación está disponible en http://flask-api:5000. Desde el anfitrión, su URL es http://localhost:5000. 

### 2. Prometheus
Lanza un contenedor Prometheus

El fichero ./monitoring/prometheus.yml contiene la configuración necesaria para un "scraper" de la aplicación Flask (de nombre flask-api, puerto 5000).

Prometheus está accesible en http://example-prometheus:9090. También se puede acceder desde la máquina anfitriona con http://localhost:9090, para observar las métricas que recibe.

### 3. Grafana
Lanza un contenedor Grafana

La configuración del contenedor está en ./monitoring/config.monitoring

Grafana está accesible en la máquina anfitriona como http://localhost:3000

Las credenciales de acceso son admin/pass@123

En las fuentes de datos, se debe añadir una llamada exactamente "Prometheus" (con la P mayúscula), de tipo Prometheus. El URL de acceso será http://example-prometheus:9090

Después se pueden importar paneles. Desde la máquina anfitriona (que es donde se ejecuta el navegador) podemos añadir el panel que está en ./monitoring/grafana_dashboard.json. También se puede copiar y pegar en el

## Puesta en marcha

1. Ejecutar "docker compose up -d"
2. Acceder a la webUI de Grafana http://localhost:3000 (admin/pass@123)
3. Configurar en Grafana la fuente de datos e importar el panel
4. Generar actividad en la aplicación Flask, accediendo repetidamente a http://localhost:5000 (usar el botón "cargar página de nuevo" del navegador)
5. Comprobar los cambios en el panel de Grafana. No son inmediatos, esperar unos segundos

## Parada
Ejecutar "docker compose down"