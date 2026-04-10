# Connect DePIN: P2P Energy Settlement on Stellar

**Connect DePIN** is a decentralized energy sharing protocol that allows solar owners to sell excess power to their neighbors. By linking **Smart Meter Hardware** to **Soroban Smart Contracts**, we ensure that every watt consumed is automatically verified and settled on the Stellar blockchain.

-----

## ⚡ The Problem

In West Africa, energy poverty persists despite an abundance of private solar installations. Owners of these systems often have 40-60% idle capacity, while neighbors suffer from grid outages. Current P2P sharing is hindered by:

  * **Trust Deficits:** No transparent way to prove exactly how much energy was used.
  * **Payment Friction:** High bank fees make micro-payments for small energy amounts unviable.
  * **Manual Billing:** No automated system to link real-time consumption to financial settlement.

## 🚀 The Solution

Connect DePIN creates a "Trustless Energy Market" using:

1.  **IoT Smart Meters:** Custom hardware that monitors energy flow ($kWh$).
2.  **The Energy Oracle:** A bridge that pushes meter data to the blockchain.
3.  **Soroban Smart Contracts:** Logic that handles automated, real-time escrow and payments in stablecoins (USDC/NGNC).

-----

## 🛠 Technical Architecture

### 1\. Hardware Layer (The Meter)

  * **PCB Design:** Custom board utilizing the **ESP32** for connectivity and the **PZEM-004T** for high-precision energy monitoring.
  * **Firmware:** Written in C++/Arduino, handling the calculation of Active Power, Voltage, and Cumulative $kWh$.
  * **Data Transmission:** Uses MQTT/HTTPS to push heartbeats to the Oracle Bridge.

### 2\. Blockchain Layer (Stellar/Soroban)

  * **The Settlement Contract:** A Soroban smart contract that:
      * Holds buyer deposits in escrow.
      * Releases payment to the provider based on verified $kWh$ inputs.
      * Implements a "Rate Per Watt" logic defined by the provider.
  * **On-Chain Events:** Every "heartbeat" from the meter is recorded as a contract event, providing a transparent audit trail.

### 3\. Gateway Layer (The Oracle)

  * A Python-based middleware that validates hardware signatures and pushes the data to the Stellar Network. It ensures that only authorized meters can trigger payment releases.

-----

## 📂 Repository Structure

```text
├── hardware/
│   ├── pcb-design/      # Schematics and Gerber files
│   └── firmware/        # ESP32 source code for energy monitoring
├── contracts/
│   └── settlement/     # Soroban (Rust) smart contract source
├── oracle/
│   └── bridge.py        # Hardware-to-Chain data relay script
└── docs/                # Architecture diagrams and API specs
```

-----

## 📅 30-Day Roadmap (Stellar Residency)

  - [ ] **Week 1:** Finalize PCB routing and order first prototype batch.
  - [ ] **Week 2:** Deploy "Settlement Contract" to Stellar Testnet (Futurenet).
  - [ ] **Week 3:** Integrate Firmware with the Soroban Oracle script.
  - [ ] **Week 4:** End-to-end "Hardware-to-Payment" pilot test with a 100W load.

-----

## 👥 Team

  * **Anosike Mmerichukwu** – Product Strategy & Operations (COO, Switch Electric)
  * **Godwin Igwurude** – Hardware Design & Soroban Developmen

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
