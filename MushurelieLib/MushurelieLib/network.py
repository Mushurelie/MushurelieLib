import requests
import os
import subprocess
import platform
import psutil

def get_public_ip():
    """Retourne l'adresse IP publique de l'utilisateur."""
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération de l'adresse IP : {e}")
        return None

def get_current_username():
    """Retourne le nom d'utilisateur de l'utilisateur actuellement connecté."""
    try:
        username = os.getlogin()
        print(f"Nom d'utilisateur actuel : {username}")
        return username
    except Exception as e:
        print(f"Erreur lors de la récupération du nom d'utilisateur : {e}")
        return None

def list_system_users():
    """Liste les utilisateurs enregistrés sur le système (Windows uniquement)."""
    try:
        if platform.system() == "Windows":
            users = subprocess.check_output("net user", shell=True, text=True)
            print("Liste des utilisateurs du système :")
            print(users)
            return users
        else:
            print("Cette fonction est uniquement disponible pour Windows.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la récupération des utilisateurs : {e}")
        return None

def find_software_by_process(software_name):
    """Recherche un logiciel installé en fonction de son nom de processus."""
    try:
        for process in psutil.process_iter(['name']):
            if software_name.lower() in process.info['name'].lower():
                print(f"Le logiciel '{software_name}' est en cours d'exécution.")
                return True
        print(f"Le logiciel '{software_name}' n'est pas en cours d'exécution.")
        return False
    except Exception as e:
        print(f"Erreur lors de la recherche du logiciel par processus : {e}")
        return None

def find_software_by_path(software_name):
    """Recherche un logiciel installé par son chemin d'installation (Windows uniquement)."""
    try:
        if platform.system() == "Windows":
            program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
            software_paths = []
            
            for root, dirs, files in os.walk(program_files):
                if software_name.lower() in root.lower():
                    software_paths.append(root)
            
            if software_paths:
                print(f"Le logiciel '{software_name}' a été trouvé dans :")
                for path in software_paths:
                    print(path)
                return software_paths
            else:
                print(f"Le logiciel '{software_name}' n'a pas été trouvé.")
                return None
        else:
            print("Cette fonction est uniquement disponible pour Windows.")
            return None
    except Exception as e:
        print(f"Erreur lors de la recherche du logiciel par chemin d'installation : {e}")
        return None

def list_disks():
    """Liste les disques disponibles sur le système."""
    try:
        partitions = psutil.disk_partitions()
        disks = [partition.device for partition in partitions]
        print("Disques disponibles :")
        for disk in disks:
            print(disk)
        return disks
    except Exception as e:
        print(f"Erreur lors de la récupération des disques : {e}")
        return None