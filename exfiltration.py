import tkinter as tk
from tkinter import filedialog
from scapy.all import IP, ICMP, Raw, send


def send_image():
    # Adresse IP de destination
    dst_ip = "172.16.47.180"

    # Chemin vers l'image que vous souhaitez envoyer
    image_path = "linux.jpg"

    # Taille maximale du payload brut (Raw payload)
    max_payload_size = 1000  # Vous pouvez ajuster cette valeur en fonction de votre réseau

    # Charger le contenu de l'image sous forme de données binaires
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Diviser l'image en morceaux plus petits
    chunks = [image_data[i:i+max_payload_size]
              for i in range(0, len(image_data), max_payload_size)]

    # START PACKET
    icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load='start')
    send(icmp_packet, verbose=False)
    # print(f"Chunk START envoyé.")

    # Envoyer chaque morceau comme un paquet ICMP séparé
    for i, chunk in enumerate(chunks):
        icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load=chunk)
        send(icmp_packet, verbose=False)
        print(f"Chunk {i+1}/{len(chunks)} envoyé.", end="\r", flush=True)

    # END PACKET
    icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load='end')
    send(icmp_packet, verbose=False)
    # print(f"Chunk END envoyé.")y


def open_file_dialog():
    file_path = filedialog.askopenfilename()
    file_path_label.config(text=file_path)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Image Sender")

# Configuration du gestionnaire de disposition grid
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)


# Widgets
ip_label = tk.Label(root, text="Destination IP:")
ip_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

open_file_button = tk.Button(root, text="Open Image", command=open_file_dialog)
open_file_button.grid(row=1, columnspan=2, sticky="ew", padx=5, pady=5)

file_path_label = tk.Label(root, text="No file selected")
file_path_label.grid(row=2, columnspan=2, sticky="ew", padx=5, pady=5)

send_button = tk.Button(root, text="Send Image", command=send_image)
send_button.grid(row=3, columnspan=2, sticky="ew", padx=5, pady=5)


# lancer l'app
root.mainloop()
