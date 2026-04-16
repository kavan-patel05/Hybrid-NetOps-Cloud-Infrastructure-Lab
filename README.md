# Hybrid-NetOps-Cloud-Infrastructure-Lab
![Banner](assets/banner.png)
A self-directed, hands-on lab simulating an enterprise-grade network environment.

## Lab Architecture
### 1. Physical / Virtual Infrastructure
- Edge Router: Cisco/pfSense/VyOS (simulated) handling NAT, DHCP, and inter-VLAN routing.
- Internal Network: Managed L2/L3 switches with three distinct VLANs.
  - VLAN 10 (Management): For infrastructure control and SSH access.
    - - VLAN 20 (Server): Hosting Linux application servers and databases.
      - - VLAN 30 (Users): Simulating end-user device
