import tkinter as tk
from tkinter import filedialog
import base64
from scapy.all import sr1, IP, UDP, DNS, DNSQR


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


def send_image():
    dst_ip = ip_entry.get()
    image_path = filedialog.askopenfilename()

    if not image_path or not dst_ip:
        print("Please enter the destination IP and select a file.")
        return

    encoded_chunks = encode_image_data(image_path)

    for i, chunk in enumerate(encoded_chunks):
        send_dns_query(dst_ip, chunk)
        print(f"Chunk {i+1}/{len(encoded_chunks)} sent.", end="\r", flush=True)


# interface utilisateur
root = tk.Tk()
root.title("Image Sender via DNS")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

ip_label = tk.Label(root, text="Destination IP:")
ip_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

send_button = tk.Button(root, text="Send Image via DNS", command=send_image)
send_button.grid(row=1, columnspan=2, sticky="ew", padx=5, pady=5)

root.mainloop()
