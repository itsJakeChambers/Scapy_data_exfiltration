
from io import BytesIO
from PIL import Image
from scapy.all import sniff, IP, ICMP

your_ip_address = '172.27.64.1'

result = b''  # Use bytes for binary data


def packet_callback(packet):
    global result
    if IP in packet and ICMP in packet:
        payload = packet[ICMP].payload.load
        print(payload)
        if payload == b'start':
            result = b''
        elif payload == b'end':
            display_image(result)
        else:
            result += payload


def display_image(data):
    # Open the image from binary data
    image = Image.open(BytesIO(data))
    # Display the image
    image.show()


# Use the sniff function to capture packets
# The prn parameter specifies the callback function to call for each packet
# Use iface="lo" to capture local packets
sniff(prn=packet_callback,
      filter=f"icmp and not src host {your_ip_address}", store=0)
