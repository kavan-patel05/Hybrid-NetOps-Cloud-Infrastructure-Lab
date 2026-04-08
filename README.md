# Hybrid-NetOps-Cloud-Infrastructure-Lab


# Overview

This project simulates an enterprise-grade network environment integrating switching, routing, cloud services, and monitoring automation.

The lab focuses on real-world network operations, troubleshooting, and incident response scenarios.

---

# Architecture

* VLAN-based network segmentation
* Layer 2 & Layer 3 switching
* Static and dynamic routing
* Linux server for monitoring
* AWS cloud integration
* Python-based monitoring scripts

---

# Technologies Used

 Technology              Purpose 
 Cisco Packet Tracer     Network simulation 
 Cisco IOS CLI           Device configuration 
 VirtualBox              Virtualization platform 
 Ubuntu Server 24.04     Linux server OS 
 AWS Free Tier           Cloud infrastructure 
 Python 3                Monitoring automation 
 GitHub                  Version control and portfolio 

---

# Key Features

* End-to-end packet flow analysis
* VLAN and inter-VLAN routing
* Real-world troubleshooting scenarios
* Network monitoring automation using Python
* Simulated enterprise network design

---

# Troubleshooting Scenarios

* VLAN misconfiguration
* ARP issues
* Routing failures
* Packet loss and latency debugging

---

# Learning Outcomes

* Strong understanding of Layer 2 & Layer 3 networking
* Hands-on troubleshooting experience
* Exposure to cloud-integrated networking
* Basics of network automation

---

# Project Structure

Hybrid-NetOps-Cloud-Infrastructure-Lab/
│
├── configs/
│   ├── R1-config.txt        # Router running configuration
│   ├── Sw_Core-config.txt   # Core switch configuration
│   ├── Sw_Office-config.txt # Office access switch configuration
│   ├── Sw_IT-config.txt     # IT access switch configuration
│   └── Sw_Guest-config.txt  # Guest access switch configuration
│
├── docs/
│   └── network-overview.txt # Network design documentation
│
├── monitoring/
│   └── monitor.py           # Python NOC monitoring script
│
├── topology/
│   ├── NOC_Lab_Enterprise.pkt      # Cisco Packet Tracer file
│   └── NOC_Lab_Enterprise_Topology.png  # Network diagram
│
├── troubleshooting/
│   └── (scenarios coming in Phase 2)
│
└── README.md

---

# Future Improvements

* Add SNMP-based monitoring
* Integrate real cloud networking (AWS VPC)
* Enhance automation using APIs

---

# Author

Kavan Patel
