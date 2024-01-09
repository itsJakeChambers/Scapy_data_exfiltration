import tkinter as tk
from tkinter import filedialog
from scapy.all import IP, ICMP, Raw, send


def send_image():
    # Destination IP address
    dst_ip = ip_entry.get()  # Use the IP entered in the Entry widget

    # File path of the selected image
    image_path = filedialog.askopenfilename()

    if not image_path or not dst_ip:
        print("Please enter the destination IP and select a file.")
        return

    # Maximum size of the raw payload
    max_payload_size = 1000  # You can adjust this value based on your network

    # Load the content of the image as binary data
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Divide the image into smaller chunks
    chunks = [image_data[i:i+max_payload_size]
              for i in range(0, len(image_data), max_payload_size)]

    # START PACKET
    icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load='start')
    send(icmp_packet, verbose=False)

    # Send each chunk as a separate ICMP packet
    for i, chunk in enumerate(chunks):
        icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load=chunk)
        send(icmp_packet, verbose=False)
        print(f"Chunk {i+1}/{len(chunks)} sent.", end="\r", flush=True)

    # END PACKET
    icmp_packet = IP(dst=dst_ip) / ICMP() / Raw(load='end')
    send(icmp_packet, verbose=False)


def open_file_dialog():
    file_path = filedialog.askopenfilename()
    file_path_label.config(text=file_path)


# Create the main window
root = tk.Tk()
root.title("Image Sender")

# Configure the grid layout manager
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

# Widgets
ip_label = tk.Label(root, text="Destination IP:")
ip_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# open_file_button = tk.Button(root, text="Open Image", command=open_file_dialog)
# open_file_button.grid(row=1, columnspan=2, sticky="ew", padx=5, pady=5)

# file_path_label = tk.Label(root, text="No file selected")
# file_path_label.grid(row=2, columnspan=2, sticky="ew", padx=5, pady=5)

send_button = tk.Button(root, text="Send Image", command=send_image)
send_button.grid(row=3, columnspan=2, sticky="ew", padx=5, pady=5)

# Run the application
root.mainloop()
