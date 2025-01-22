import os
from dotenv import load_dotenv
import subprocess

# Charger les variables depuis le fichier .env
load_dotenv('.env')

# Exécuter une commande DBT (exemple : dbt run)
subprocess.run(["dbt", "run"])