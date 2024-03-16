# SdnThreatOptix
The SdnThreatOptix project concentrates on creating a machine learning model for classifying Denial of Service (DDoS) attacks within SDN networks, servers, and databases. It employs network infrastructure management tools such as Telegraf and Mininet for SDN network emulation, alongside InfluxDB for data storage and visualization.

## Setup:
This project is a derivative of my previous project, SdnInfraOptix, which focused on monitoring SDN network infrastructure. For VM installation, RYu controller setup, Mininet configuration,Telegraph interfacing and SDN initialization, please refer to my GitHub repository at https://github.com/SRIRAM-VIGNESH-V/SDNInfraOptix.

## Hping 3
![image](https://github.com/SRIRAM-VIGNESH-V/SdnThreatOptix/assets/159048515/fc99e2cc-de44-46e5-aa1d-6e772ea9eb4e)
Hping3 is a versatile command-line network tool designed for packet manipulation and testing purposes. With support for ICMP, UDP, and TCP packets, it serves as a valuable tool for diagnostics, scanning, and security testing within network environments. Notably, Hping3 is adept at simulating Denial of Service (DoS) attacks, making it a preferred choice for network administrators and security professionals seeking to assess and analyze network behavior effectively.<br>
To simulate a Denial of Service (DoS) attack using Hping3, you can execute the following command:
```
sudo hping3 -V -1 -d 1400 --faster -c 1000 -q --rand-source h4
```
This command will send a flood of ICMP echo request packets (ping) to host 'h4' from host 'h1' with a bogus payload. The '-V' flag enables verbose output, '-1' specifies ICMP protocol, '-d 1400' sets the data size to 1400 bytes, '--faster' increases the transmission speed, '-c 1000' specifies to send 1000 packets, '-q' suppresses output, and '--rand-source' sets a random source IP address for each packet.<br>
While this DoS attack is ongoing, a normal flow from 'h2' to 'h4' may fail due to the increased network traffic and potential packet loss caused by the attack.<br>
Normal flow:
![image](https://github.com/SRIRAM-VIGNESH-V/SdnThreatOptix/assets/159048515/767a1c19-df99-4636-bf06-8fc37432ba1f)
From h2 to h4 during DOS:
![image](https://github.com/SRIRAM-VIGNESH-V/SdnThreatOptix/assets/159048515/9073d3f1-3832-4439-8604-363f92cd9ff5)





