# SdnThreatOptix
The SdnThreatOptix project aims at creating a machine learning model for classifying Denial of Service (DDoS) attacks within SDN networks, servers, and databases. It employs network infrastructure management tools such as Telegraf and Mininet for SDN network emulation, alongside InfluxDB for data storage and visualization.

## Setup:
This project is a derivative of my previous project,`SdnInfraOptix` which focused on monitoring SDN network infrastructure. For VM installation, RYu controller setup, Mininet configuration,Telegraph interfacing and SDN initialization, please refer to my GitHub repository at https://github.com/SRIRAM-VIGNESH-V/SDNInfraOptix.

## Hping 3
![image](https://github.com/SRIRAM-VIGNESH-V/SdnThreatOptix/assets/159048515/fc99e2cc-de44-46e5-aa1d-6e772ea9eb4e)<br>
Hping3 is a versatile command-line network tool designed for packet manipulation and testing purposes. With support for ICMP, UDP, and TCP packets, it serves as a valuable tool for diagnostics, scanning, and security testing within network environments. Notably, Hping3 is adept at simulating Denial of Service (DoS) attacks, making it a preferred choice for network administrators and security professionals seeking to assess and analyze network behavior effectively.To simulate a Denial of Service (DoS) attack using Hping3, you can execute the following command:<br>
```
sudo hping3 -V -1 -d 1400 --faster -c 1000 -q --rand-source h4
```
This command will send a flood of ICMP echo request packets (ping) to host 'h4' from host 'h1' with a bogus payload. The '-V' flag enables verbose output, '-1' specifies ICMP protocol, '-d 1400' sets the data size to 1400 bytes, '--faster' increases the transmission speed, '-c 1000' specifies to send 1000 packets, '-q' suppresses output, and '--rand-source' sets a random source IP address for each packet.
While this DoS attack is ongoing, a normal flow from 'h2' to 'h4' may fail due to the increased network traffic and potential packet loss caused by the attack.<br>
### Normal flow:<br>
```
64 bytes from 10.0.0.4: icmp_seq=14 ttl=64 time=0.881 ms
64 bytes from 10.0.0.4: icmp_seq=23 ttl=64 time=0.1863 ms
64 bytes from 10.0.0.4: icmp_seq=35 ttl=64 time=0.1165 ms
64 bytes from 10.0.0.4: icmp_seq=39 ttl=64 time=0.2542 ms
64 bytes from 10.0.0.4: icmp_seq=40 ttl=64 time=0.1473 ms
64 bytes from 10.0.0.4: icmp_seq=41 ttl=64 time=0.464 ms
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
We are going to run a telegraf instance on mininet's Host 4 whose input plugin will gather ICMP data and whose output will be a file in the VM's home directory. We'll be running a second telegraf instance in the host VM whose input will be the file containing Host 4's output and whose output will be the Influx DB hosted in the controller VM. This architecture leverages the shared filesystem and uses a second telegraf instance as a mere proxy between one of mininet's internal hosts and the controller VM, both living in entirely different networks.
### Interface telegraph to influxDB :
### Official documentation :
https://docs.influxdata.com/influxdb/v2/write-data/no-code/use-telegraf/
### InfluxDB ping plguing for Telegraph interface :
https://docs.influxdata.com/influxdb/cloud/reference/cli/influx/ping/

## Method of detecting Dos:
To detect a Denial of Service (DoS) attack, we can utilize the derivative of the rate of incoming packets. This method focuses on detecting sudden changes in incoming message rates, which are indicative of a potential attack, rather than solely relying on the volume of incoming packets.To implement this approach, you can use the provided Python script `data_gathering.py`. Running python `data_gathering.py 0` will generate `ICMP_data_class_0.csv` while conducting normal ICMP ping operations, while python `data_gathering.py 1` will produce `ICMP_data_class_1.csv` during a simulated DoS attack using Hping3.These generated CSV files can then be analyzed to identify patterns and anomalies in packet rates, enabling the detection of DoS attacks based on deviations from normal network behavior.
## Data gathering:
`data_gathering.py` is a simple python script that uses influx dB’s python API to read the data and prepare a CSV (Comma Separated Values) to later be read by the script implementing to train ML model for DOS detection.
## Model Training:
With the obtained ICMP datasets as inputs, the next step involves training a supervised Machine Learning model, specifically an XGBoost model, to classify the derivative of the pings as either normal or indicative of a DoS attack. For detailed information on the model training process, including data preprocessing, feature selection, and model evaluation, please refer to the Jupyter notebook file provided.
The Jupyter notebook file contains documentation and code illustrating each step of the model training process. By following the instructions outlined in the notebook, you can gain insights into the methodology used to develop and evaluate the XGBoost model for DoS detection based on derivative of ping data.In the repository, you will find the `XGBoost.dat file`, which contains the trained XGBoost model parameters. This file is crucial for deploying the trained model for inference or further evaluation purposes. The trained model encapsulated within `XGBoost.dat` is capable of classifying the derivative of ping data into either normal or indicative of a DoS attack with a high degree of accuracy.
## LIcense:
MIT License - Github











