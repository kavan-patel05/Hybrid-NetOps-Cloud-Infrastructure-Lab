# Hybrid-NetOps-Cloud-Infrastructure-Lab

![Hybrid NetOps Lab Banner](assets/banner.png)

A self-directed, hands-on lab simulating an enterprise-grade network environment - covering switching, routing, VLAN segmentation, Linux server administration, cloud infrastructure, and Python-based monitoring automation.

Built to mirror real-world NOC and network operations workflows.

---

## Lab Architecture

### 1. Physical / Virtual Infrastructure
- Edge Router: Cisco/pfSense/VyOS (simulated) handling NAT, DHCP, and inter-VLAN routing.
- - Internal Network: Managed L2/L3 switches with three distinct VLANs:
  - - VLAN 10 (Management): For infrastructure control and SSH access.
    - - VLAN 20 (Server): Hosting Linux application servers and databases.
      - - VLAN 30 (Users): Simulating end-user devices.
       
        - ### 2. Cloud Integration (AWS)
        - - Site-to-Site VPN / VPC: Connected the local network to AWS VPC using an IPSec tunnel.
          - - EC2 Instances: Running in AWS to simulate offsite backup and cloud-native services.
           
            - ### 3. Monitoring & Automation
            - - Python Monitoring: Custom script using ping and SNMP to track device health and latency.
              - - Dashboards: Real-time logging of network performance metrics.
               
                - ---

                ## Tech Stack & Skills
                - Networking: VLANs, Subnetting, OSPF/BGP, ACLs, VPN (IPSec).
                - - Linux: CentOS/Ubuntu Server, Bash scripting, systemd, SSH hardening.
                  - - Cloud: AWS VPC, EC2, IAM, Security Groups.
                    - - Automation: Python (Netmiko/Napalm), YAML for configuration drafts.
                     
                      - ---

                      ## Future Roadmap
                      - [ ] Implement Ansible for automated device provisioning.
                      - [ ] - [ ] Integrate Grafana/Prometheus for advanced visualization.
                      - [ ] - [ ] Transition local VM workloads to Docker containers.
                     
                      - [ ] ---
                     
                      - [ ] ## Contact
                      - [ ] Kavan Patel
                      - [ ] - [LinkedIn](https://www.linkedin.com/in/kavan-patel-cloud-specialist/)
                      - [ ] - [Portfolio](https://kavan-patel05.github.io/kavanpatel.dev/)
                      - [ ] 
