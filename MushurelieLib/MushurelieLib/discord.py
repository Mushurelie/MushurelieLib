import requests
import time

def send_discord_message(webhook_url, message):
    """Envoie un message simple via un webhook Discord."""
    data = {
        "content": message
    }
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("Message envoyé avec succès.")
    except requests.RequestException as e:
        print(f"Erreur lors de l'envoi du message : {e}")

def send_discord_embed(webhook_url, title=None, description=None, color=0x3498db, fields=None, thumbnail_url=None, image_url=None, footer_text=None, footer_icon_url=None):
    """Envoie un message embed via un webhook Discord."""
    embed = {
        "title": title,
        "description": description,
        "color": color,
        "fields": [],
        "thumbnail": {"url": thumbnail_url} if thumbnail_url else None,
        "image": {"url": image_url} if image_url else None,
        "footer": {
            "text": footer_text,
            "icon_url": footer_icon_url
        } if footer_text or footer_icon_url else None,
    }
    
    # Ajoute les champs s'ils sont fournis
    if fields:
        for field in fields:
            embed_field = {
                "name": field.get("name"),
                "value": field.get("value"),
                "inline": field.get("inline", False)
            }
            embed["fields"].append(embed_field)
    
    # Filtre les valeurs None
    embed = {k: v for k, v in embed.items() if v is not None}

    data = {
        "embeds": [embed]
    }
    
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("Embed envoyé avec succès.")
    except requests.RequestException as e:
        print(f"Erreur lors de l'envoi de l'embed : {e}")

def send_discord_message_multiple_times(webhook_url, message, times, delay=1):
    """Envoie le même message un nombre défini de fois avec un délai optionnel."""
    for i in range(times):
        send_discord_message(webhook_url, message)
        time.sleep(delay)
    print(f"Message envoyé {times} fois avec un délai de {delay} seconde(s) entre chaque envoi.")

def delete_webhook(webhook_url):
    """Supprime un webhook Discord."""
    try:
        response = requests.delete(webhook_url)
        response.raise_for_status()
        print("Webhook supprimé avec succès.")
    except requests.RequestException as e:
        print(f"Erreur lors de la suppression du webhook : {e}")

def send_discord_message_and_delete_webhook(webhook_url, message):
    """Envoie un message et supprime le webhook après l'envoi."""
    send_discord_message(webhook_url, message)
    delete_webhook(webhook_url)

def delete_message(webhook_url, message_id):
    """Supprime un message envoyé par le webhook."""
    try:
        response = requests.delete(f"{webhook_url}/messages/{message_id}")
        response.raise_for_status()
        print("Message supprimé avec succès.")
    except requests.RequestException as e:
        print(f"Erreur lors de la suppression du message : {e}")