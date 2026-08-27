What I Learned

OT/ICS Architecture vs. Traditional IT:

OT prioritizes availability and uptime over confidentiality and integrity, meaning many legacy ICS protocols lack authentication, encryption, or integrity checks.

The core components of SCADA systems include Supervisory Computers/HMIs (monitoring and manual overrides), PLCs/RTUs (logic controllers reading sensors and directing actuators), and the underlying communication network.

Modbus Protocol Mechanics:

Modbus operates on a master/slave (client/server) model over TCP port 502 (Modbus TCP).

The distinct register types and their read/write permissions:

Coil: 1-bit, Read/Write (typically binary outputs/actuators).

Discrete Input: 1-bit, Read-Only (binary sensors).

Input Register: 16-bit, Read-Only (analog sensors, e.g., water level).

Holding Register: 16-bit, Read/Write (setpoints, configuration, process variables).

Common Modbus function codes (e.g., Code 3 for Read Holding Registers, Code 6 for Write Single Holding Register) and how to interface with them programmatically using Python libraries like pymodbus.

ICS Discovery & Reverse Engineering:

How to map a physical process (a bottle-filling plant with initialization, filling, and moving phases) to digital registers.

Correlating physical telemetry (sensor readings like water levels and bottle positions) and physical actions (actuators like rollers and nozzles) with register address changes over time.

Attack Vectors & Impact:

How an attacker with network access to Modbus TCP can act as a rogue master or spoof HMI commands.

Writing arbitrary values to holding registers or coils to bypass safety thresholds, manipulate actuator states, and cause physical malfunction or process interruption.
