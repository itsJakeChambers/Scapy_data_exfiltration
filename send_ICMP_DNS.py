import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from scapy.all import IP, ICMP, Raw, send
import base64
from scapy.all import sr1, IP, UDP, DNS, DNSQR

# Fonction pour envoyer une image via ICMP


def send_image_icmp():
    dst_ip = icmp_ip_entry.get()
    image_path = filedialog.askopenfilename()

    if not image_path or not dst_ip:
        print("Please enter the destination IP and select a file.")
        return

    max_payload_size = 1000
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    chunks = [image_data[i:i+max_payload_size]
              for i in range(0, len(image_data), max_payload_size)]

    icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load='start')
    send(icmp_packet, verbose=False)

    for i, chunk in enumerate(chunks):
        icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load=chunk)
        send(icmp_packet, verbose=False)
        print(f"Chunk {i+1}/{len(chunks)} sent.", end="\r", flush=True)

    icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load='end')
    send(icmp_packet, verbose=False)

# Fonction pour envoyer une image via DNS


def send_image_dns():
    dst_ip = dns_ip_entry.get()
    image_path = filedialog.askopenfilename()

    if not image_path or not dst_ip:
        print("Please enter the destination IP and select a file.")
        return

    def encode_image_data(image_path):
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
        encoded_data = base64.urlsafe_b64encode(image_data)
        max_length = 63
        return [encoded_data[i:i + max_length] for i in range(0, len(encoded_data), max_length)]

    def send_dns_query(dst_ip, encoded_chunk):
        response = sr1(IP(dst=dst_ip)/UDP(dport=53)/DNS(rd=1,
                       qd=DNSQR(qname=encoded_chunk + b"aforp.fr")), timeout=2)
        return response

    encoded_chunks = encode_image_data(image_path)

    for i, chunk in enumerate(encoded_chunks):
        send_dns_query(dst_ip, chunk)
        print(f"Chunk {i+1}/{len(encoded_chunks)} sent.", end="\r", flush=True)


# Créez la fenêtre principale
root = tk.Tk()
root.title("Image Sender")

# Créez un widget de gestion des onglets
tab_control = ttk.Notebook(root)

# Créez les onglets
tab_icmp = ttk.Frame(tab_control)
tab_dns = ttk.Frame(tab_control)

tab_control.add(tab_icmp, text="ICMP")
tab_control.add(tab_dns, text="DNS")

# Interface utilisateur pour l'onglet ICMP
icmp_label = tk.Label(tab_icmp, text="Destination IP:")
icmp_label.pack(pady=10)
icmp_ip_entry = tk.Entry(tab_icmp)
icmp_ip_entry.pack(pady=5)
icmp_button = tk.Button(
    tab_icmp, text="Send Image via ICMP", command=send_image_icmp)
icmp_button.pack(pady=10)

# Interface utilisateur pour l'onglet DNS
dns_label = tk.Label(tab_dns, text="Destination IP:")
dns_label.pack(pady=10)
dns_ip_entry = tk.Entry(tab_dns)
dns_ip_entry.pack(pady=5)
dns_button = tk.Button(
    tab_dns, text="Send Image via DNS", command=send_image_dns)
dns_button.pack(pady=10)

# Pack the tab control widget
tab_control.pack(expand=1, fill="both")

# Exécutez la boucle principale
root.mainloop()
