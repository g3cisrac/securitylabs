Zero trust security 

	•	comprised of a Data plane which enforces security policies, established by the control plane. The control plane defines and manages security policies. (AKA Policy Decision Point, Policy Enforcement Point. 
	•	2 key components: Policy Engine, Policy Admin
Many trust networks are open on the inside. Most importantly what you know, what you have, and what you are authenticate you. Zero Trust Architecture (ZTA) — Notes

Core principle: "Never trust, always verify." No user, device, or network segment is trusted by default, even if it's inside the traditional network perimeter.

1. Foundational Assumptions
Assume breach — attackers may already be inside the network
No implicit trust based on network location (internal vs. external)
Every access request must be authenticated, authorized, and encrypted
2. Key Tenets (NIST SP 800-207)
All data sources and computing services are treated as resources
All communication is secured regardless of network location
Access to resources is granted per-session, not persistently
Access is determined by dynamic policy — identity, device health, behavior, and environmental attributes
Organization monitors and measures the integrity/security posture of all owned/associated assets
All resource authentication and authorization is dynamic and strictly enforced before access is allowed
Organization collects as much info as possible on current state of assets, network, and communications to improve security posture
3. Core Components
Policy Engine (PE): Decides whether to grant access based on policy + inputs from trust algorithms
Policy Administrator (PA): Establishes/shuts down communication path between subject and resource; executes PE's decision
Policy Enforcement Point (PEP): Enables, monitors, and terminates connections (the actual gatekeeper)
4. Pillars / Building Blocks (commonly cited — CISA ZTMM has 5)
Identity — strong authentication (MFA), least privilege, continuous validation
Devices — device health/posture checks, EDR, compliance state
Network/Environment — micro-segmentation, encrypted traffic, no flat networks
Applications & Workloads — secure app access, runtime protections, API security
Data — classification, encryption at rest/in transit, DLP, access controls tied to data sensitivity
5. Key Technologies/Concepts Enabling ZTA
Micro-segmentation — breaking network into small zones to contain lateral movement
Least privilege access (LPA) — minimum permissions needed, just-in-time/just-enough access
MFA / strong identity verification
Continuous monitoring & analytics — behavioral baselining, anomaly detection
Software-Defined Perimeter (SDP) — hides infrastructure until authenticated
ZTNA (Zero Trust Network Access) — VPN replacement, app-level access vs. network-level
Device posture/health attestation
Policy-based access control (PBAC/ABAC) over static role-based rules alone
6. What It's NOT
Not a single product you buy — it's an architecture/strategy
Not just "more firewalls" — it shifts trust boundary from network perimeter to individual resource/session
Doesn't eliminate need for perimeter defenses, but stops relying on them as the sole control
7. Benefits
Reduces blast radius / limits lateral movement after initial compromise
Better fits hybrid/remote work and cloud-first environments (no clear "perimeter" anymore)
Improves visibility — every access request generates logs/telemetry
8. Challenges
Legacy system compatibility (older apps assume implicit trust)
Complexity of implementation — requires strong IAM foundation first
Cultural/organizational shift, not just tooling
Performance overhead of continuous verification
9. Related Frameworks/Standards
NIST SP 800-207 — the foundational ZT reference architecture
CISA Zero Trust Maturity Model — traditional → initial → advanced → optimal, across the 5 pillars
DoD Zero Trust Reference Architecture
