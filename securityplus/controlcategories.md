Control Categories

Technical (logical) security controls.
Carried out by software, hardware, firmware.
* IAM
    * MFA
    * PoLP
    * RBaC
    * SSO
* Network
    * Firewalls -> “Next-Generation Firewalls” are stateful which means they follow rules in-context of the network’s connection history. Application awareness is an evolution of stateful rules. A NGFW uses stateful rules to figure out whether or not a packet belongs to a known connection. (NEW, ESTABLISHED, RELATED, INVALID).
    * IDS/IPS -> detect policy violations. IPS is the one to drop it automatically.
    * VPN
    * Network Segmentation -> Division of network into subnets based on authorization
* Endpoint
    * EDR (Endpoint Detection and Response) -> Will automatically detect attacks, and even investigate malicious activity. How does it do that? It monitors behavior, by identifying what’s normal on a network and flags anomalies. (Establishes a baseline)
    * Antivirus -> references known software signatures.
* Data protection
    * Encryption
    * DLP (Data Loss Prevention) -> PII, PCI (Payment Card Industry) prevents data from being uploaded to unauthorized cloud servers. 
* Vulnerability and Config Mgmt 
    * Systems that automatically apply Patches, Updates, Firmware
    * Vuln Scanners -> Nessus, Qualys, which will surprise systems with a scan for open ports and misconfigurations, missing patches.
* Security Monitoring
    * SIEM (Security Information and Event Management) -> correlates events in real time, alerts analysts to IoC’s. 
Preventive 	Firewalls w/ rules, MFA, whitelisting, AV software, encryption, 
Detective	SIEM, IDS, audits, monitoring, CCTV
Corrective	Backup restoration, updates and patches, IRPs and activating DRPs
** Compensationg -> MFA? 
** Detterent -> Warning signs, lighting, surveillance, Fence

Administrative (managerial) security controls. 
Documentation, policies, procedures, guidelines planning. 
* Information Security Policy
* Acceptable Use Policy 
* Framework Alignment

* Personnel Security & Operational Practices 
    * Background Checks
    * Separation of Duties
    * Mandatory Vacations & Job Rotation -> Important for organizations with high turnover to uncover fraud, unauthorized configuration
    * Onboarding and Offboarding
* Training
    * Phishing awareness
    * Security awareness 
* Risk Management 
* Reviewing third party vendors for risk before granting N/W Access
* Incident Response 
Physical controls
* Access control vestibule -> that’s a physical checkpoint. 
* Firewall, data backups, access management. 

Side note: AAA Framework
* RADIUS -> for remote access and dialup, TACACS+ -> separates authentication authorization and accounting into 3 distinct things. 
