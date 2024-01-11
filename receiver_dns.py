from io import BytesIO
from PIL import Image
from scapy.all import sniff, DNS, DNSQR
import dns.resolver

dns_server = '8.8.8.8'  # Utilisez le serveur DNS de Google comme exemple
domain_name = 'example.com'  # Remplacez par le domaine que vous souhaitez résoudre

result = b''  # Utilisez des octets pour les données binaires


def resolve_dns_and_capture(packet):
    global result

    if DNS in packet and DNSQR in packet:
        dns_query = packet[DNSQR].qname.decode()

        # Vérifiez si la requête DNS correspond au domaine que vous recherchez
        if dns_query == domain_name + '.':
            # Résolvez le domaine pour obtenir l'adresse IP
            resolver = dns.resolver.Resolver(configure=False)
            resolver.nameservers = [dns_server]
            try:
                answer = resolver.query(domain_name)
                target_ip = str(answer[0])
                print(f"Resolved DNS query to IP: {target_ip}")

                # Ensuite, envoyez votre requête DNS à l'adresse IP cible
                # Vous devrez construire une requête DNS appropriée ici

            except dns.resolver.NXDOMAIN:
                print("DNS resolution failed (NXDOMAIN)")


def display_image(data):
    # Ouvrez l'image à partir des données binaires
    image = Image.open(BytesIO(data))
    # Affichez l'image
    image.show()


# Utilisez la fonction sniff pour capturer les paquets DNS
# Utilisez le paramètre prn pour spécifier la fonction de rappel à appeler pour chaque paquet
sniff(prn=resolve_dns_and_capture, filter=f'dst port 53', store=0)
