# SdnThreatOptix
The SdnThreatOptix project concentrates on creating a machine learning model for classifying Denial of Service (DDoS) attacks within SDN networks, servers, and databases. It employs network infrastructure management tools such as Telegraf and Mininet for SDN network emulation, alongside InfluxDB for data storage and visualization.

## Setup:
This project is a derivative of my previous project,`SdnInfraOptix` which focused on monitoring SDN network infrastructure. For VM installation, RYu controller setup, Mininet configuration,Telegraph interfacing and SDN initialization, please refer to my GitHub repository at https://github.com/SRIRAM-VIGNESH-V/SDNInfraOptix.

## Hping 3
![image](https://github.com/SRIRAM-VIGNESH-V/SdnThreatOptix/assets/159048515/fc99e2cc-de44-46e5-aa1d-6e772ea9eb4e)<br>
Hping3 is a versatile command-line network tool designed for packet manipulation and testing purposes. With support for ICMP, UDP, and TCP packets, it serves as a valuable tool for diagnostics, scanning, and security testing within network environments. Notably, Hping3 is adept at simulating Denial of Service (DoS) attacks, making it a preferred choice for network administrators and security professionals seeking to assess and analyze network behavior effectively.
To simulate a Denial of Service (DoS) attack using Hping3, you can execute the following command:<br>
```
sudo hping3 -V -1 -d 1400 --faster -c 1000 -q --rand-source h4
```
This command will send a flood of ICMP echo request packets (ping) to host 'h4' from host 'h1' with a bogus payload. The '-V' flag enables verbose output, '-1' specifies ICMP protocol, '-d 1400' sets the data size to 1400 bytes, '--faster' increases the transmission speed, '-c 1000' specifies to send 1000 packets, '-q' suppresses output, and '--rand-source' sets a random source IP address for each packet.<br>
While this DoS attack is ongoing, a normal flow from 'h2' to 'h4' may fail due to the increased network traffic and potential packet loss caused by the attack.<br>
### Normal flow:<br>
```
64 bytes from 10.0.0.4: icmp_seq=14 ttl=64 time=881 ms
64 bytes from 10.0.0.4: icmp_seq=23 ttl=64 time=1863 ms
64 bytes from 10.0.0.4: icmp_seq=35 ttl=64 time=1165 ms
64 bytes from 10.0.0.4: icmp_seq=39 ttl=64 time=2542 ms
64 bytes from 10.0.0.4: icmp_seq=40 ttl=64 time=1473 ms
64 bytes from 10.0.0.4: icmp_seq=41 ttl=64 time=464 ms
64 bytes from 10.0.0.4: icmp_seq=42 ttl=64 time=0.050 ms
64 bytes from 10.0.0.4: icmp_seq=43 ttl=64 time=0.063 ms
64 bytes from 10.0.0.4: icmp_seq=44 ttl=64 time=0.040 ms
64 bytes from 10.0.0.4: icmp_seq=45 ttl=64 time=0.181 ms
64 bytes from 10.0.0.4: icmp_seq=46 ttl=64 time=0.125 ms
```
### From h2 to h4 during DOS:<br>
```
root@test:-* ping -W 0.1 10.0.0.4
PING 10.0.0.4 (10.0.0.4) 56(84) bytes of data.
From 10.0.0.2 icmp_seq=1 Destination Host Unreachable
From 10.0.0.2 icmp_seq=2 Destination Host Unreachable
From 10.0.0.2 icmp_seq=3 Destination Host Unreachable
From 10.0.0.2 icmp_seq=4 Destination Host Unreachable
From 10.0.0.2 icmp_seq=5 Destination Host Unreachable
From 10.0.0.2 icmp_seq=6 Destination Host Unreachable
```
## Bandwidth limitation: 
To impose bandwidth limitations on Mininet channels, you can use the TCLink parameter. This allows you to set network capacity limits independently of the host machine's capabilities. Below is an example of how to create a Mininet network with bandwidth restrictions:<br>
```python
net = Mininet(topo = None,
              build = False,
              host = CPULimitedHost,
              link = TCLink,
              ipBase = '10.0.0.0/8')
net.addLink(s1, h1, bw = 10)
net.addLink(s1, h2, bw = 10)
net.addLink(s1, s2, bw = 5, max_queue_size = 500)
net.addLink(s3, s2, bw = 5, max_queue_size = 500)
net.addLink(s2, h3, bw = 10)
net.addLink(s2, h4, bw = 10)
net.addLink(s3, h5, bw = 10)
net.addLink(s3, h6, bw = 10)
```
thus , links with bandwidth restrictions have added.

## Telegraph:
We are going to run a telegraf instance on mininet's Host 4 whose input plugin will gather ICMP data and whose output will be a file in the VM's home directory. We'll be running a second telegraf instance in the host VM whose input will be the file containing Host 4's output and whose output will be the Influx DB hosted in the controller VM. This architecture leverages the shared filesystem and uses a second telegraf instance as a mere proxy between one of mininet's internal hosts and the controller VM, both living in entirely different 






