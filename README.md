# airflow

# obtener misma version(este paso ya no se hace ya que esta descargado en el repositorio y no es necesario)
- curl -LfO "https://airflow.apache.org/docs/apache-airflow/2.4.2/docker-compose.yaml"

# ejecutar este comando solo una vez 
- docker-compose up airflow-init
- docker-compose up -d

# ejecutar este comando ya ejecutado el de arriba para levantar el compose
- docker-compose up -d
