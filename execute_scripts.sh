#!/bin/bash
docker compose up -d --build
# Nom du conteneur
CONTAINER_NAME=data_streaming_pipeline-spark-master-1     ####  spark-structure-streaming-kafaka-master_Json
# Chemins des scripts à exécuter dans le conteneur


SCRIPT_PATH_5=/opt/spark-data/machine_num1.py
SCRIPT_PATH_6=/opt/spark-data/machine_num2.py
SCRIPT_PATH_7=/opt/spark-data/machine_num3.py
SCRIPT_PATH_8=/opt/spark-data/machine_num4.py

SCRIPT_PATH_9=/opt/spark-data/topics_producer.py
SCRIPT_PATH_10=/opt/spark-data/kafka_flask_api.py



# Fonction pour vérifier si un conteneur est en cours d'exécution
check_container_running() {
    docker ps --filter "name=${CONTAINER_NAME}" --filter "status=running" | grep ${CONTAINER_NAME} > /dev/null 2>&1
}

# Vérifier si le conteneur est en cours d'exécution
if check_container_running; then
    echo "Le conteneur ${CONTAINER_NAME} est en cours d'exécution. Exécution des scripts..."

    # Exécuter les scripts dans le conteneur
    docker exec -it -d ${CONTAINER_NAME} python ${SCRIPT_PATH_5}
    docker exec -it -d ${CONTAINER_NAME} python ${SCRIPT_PATH_6}
    docker exec -it -d ${CONTAINER_NAME} python ${SCRIPT_PATH_7}
    docker exec -it -d ${CONTAINER_NAME} python ${SCRIPT_PATH_8}
    docker exec -it -d ${CONTAINER_NAME} python ${SCRIPT_PATH_9}
    docker exec -it -d ${CONTAINER_NAME} python ${SCRIPT_PATH_10}

    echo "Tous les scripts ont été exécutés."
else
    echo "Le conteneur ${CONTAINER_NAME} n'est pas en cours d'exécution. Veuillez démarrer le conteneur avant d'exécuter ce script."
    exit 1
fi
