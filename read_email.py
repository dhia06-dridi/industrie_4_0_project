from imap_tools import MailBox
import time

MAIL_PASSWORD = "pxweapnypsfmmdou"
MAIL_USERNAME = "dhiadridi06@gmail.com"
action_file_path = r"F:\projet\raia_2\industry_4.0\action_python.txt"
data_file_path = r"F:\projet\raia_2\industry_4.0\data_email.txt"

# Fonction pour vérifier et modifier le fichier si "action" est présent
def process_action_file():
    try:
        # Ouvrir le fichier et lire son contenu
        with open(action_file_path, "r") as file:
            content = file.read()
        
        # Si "action" est trouvé, retourner True pour signaler que l'on peut traiter l'email
        if "action" in content:
            return True
        return False
    except FileNotFoundError:
        print(f"Le fichier {action_file_path} n'a pas été trouvé.")
        return False

# Fonction pour mettre à jour le fichier data_email.txt avec un seul email (le dernier)
def update_email_in_file(new_email):
    try:
        # Ouvrir le fichier data_email.txt et remplacer tout son contenu avec le nouvel email
        with open(data_file_path, "w") as file:
            file.write(new_email + "\n")  # Écrire seulement le nouvel email
        
        print(f"L'adresse email {new_email} a été enregistrée dans le fichier.")
    
    except FileNotFoundError:
        print(f"Le fichier {data_file_path} n'a pas été trouvé.")

# Fonction pour remplacer "action" par "end" dans le fichier action_python.txt
def replace_action_with_end():
    try:
        # Ouvrir le fichier et lire son contenu
        with open(action_file_path, "r") as file:
            content = file.read()

        # Remplacer "action" par "end"
        content = content.replace("action", "end")

        # Réécrire le fichier avec "end"
        with open(action_file_path, "w") as file:
            file.write(content)

        print("'action' remplacé par 'end' dans le fichier action_python.txt.")

    except FileNotFoundError:
        print(f"Le fichier {action_file_path} n'a pas été trouvé.")

# Connexion au serveur Gmail et traitement de l'email
with MailBox("imap.gmail.com").login(MAIL_USERNAME, MAIL_PASSWORD, "Inbox") as mailbox:
    # Attendre que le fichier contienne "action" avant de traiter l'email
    while not process_action_file():
        print("En attente du message 'action' dans le fichier...")
        time.sleep(5)  # Attendre 5 secondes avant de vérifier à nouveau

    print("'action' trouvé. Traitement de l'email en cours...")
    
    # Récupérer uniquement le dernier email
    last_email = next(mailbox.fetch(limit=1, reverse=True, mark_seen=True))

    # Afficher les informations de l'email
    print("Sujet :", last_email.subject)
    print("Expéditeur :", last_email.from_)
    print("Date :", last_email.date)
    print("Contenu :", last_email.text)

    # Vérifier si l'objet est "data_iot" et le message contient "RAIA2"
    if last_email.subject == "data_iot" and "RAIA2" in last_email.text:
        # Mettre à jour le fichier avec le nouvel email
        update_email_in_file(last_email.from_)

        # Après l'enregistrement de l'email, remplacer "action" par "end"
        replace_action_with_end()

    else:
        print("L'email ne correspond pas aux critères.")
