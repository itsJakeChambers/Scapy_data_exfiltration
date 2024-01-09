# Présentation du Projet Scapy

### Étape 1: Installation de Wireshark
*Wireshark est un outil de capture et d'analyse de paquets réseau. Il nous permet de visualiser les échanges réseau lors des tests.*

### Étape 2: Installation de Scapy
*Scapy est un framework Python permettant la manipulation d'enveloppes de paquets réseau. Il est utilisé pour construire, envoyer, et analyser des paquets réseau.*

### Étape 3: Test avec du Texte
*Avant de travailler avec des images, des tests préliminaires ont été effectués en envoyant et recevant du texte à l'aide de Scapy pour s'assurer que la configuration fonctionne correctement.*

### Étape 4: Désactivation du Pare-feu et Ping pour Tester la Connectivité
*Désactivation du pare-feu pour éliminer les éventuels obstacles. Ensuite, des pings ont été effectués entre les machines pour garantir une connectivité de base.*

### Étape 5: Lancement du Sniffer et Ping pour une Phase de Test
*Un sniffer est utilisé pour écouter le trafic réseau pendant que des pings sont effectués. Cela permet de vérifier la capture des paquets.*

### Étape 6: Découper le Fichier en Plusieurs Chunks
*Une fonction à été développer pour diviser un fichier, comme une image, en morceaux gérables, prêts à être envoyés via le réseau.*

### Étape 7: Création du Script
*Un script à été crée en utilisant Scapy pour envoyer ces morceaux d'image à un autre emplacement sur le réseau.*

### Étape 8: Test d'Envoi d’Image via un Script
*Des tests d'envoi d'image ont été effectués en utilisant le script créé, vérifiant la transmission réussie des chunks.*

### Étape 9: Côté Receveur, Assemblage des Morceaux pour Lire et Afficher l’Image
*Un script a été développé côté receveur pour recevoir les morceaux de l'image, les assembler et afficher l'image complète.*

### Étape 10: Tests du Script et Correction d’Éventuels Bugs
*Des tests exhaustifs ont été du script d'envoi et de réception, en identifiant et corrigeant tout problème ou bug qui pourrait survenir.*

### Étape 11: Réflexions sur une Stratégie Marketing
*Une stratégie marketing pour promouvoir l'outil, a été mis en oeuvre en mettant en avant ses fonctionnalités, sa facilité d'utilisation, et ses avantages par rapport aux autres solutions existantes.*

#### Ce projet combine des aspects techniques tels que la manipulation de paquets réseau, le développement de scripts avec Scapy, et des considérations plus larges telles que la connectivité réseau et la commercialisation de l'outil développé.
