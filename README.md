# Connect DePIN: P2P Energy Settlement on Stellar

**Connect** is a decentralized energy-sharing protocol that enables peer-to-peer (P2P) energy trading using **Stellar/Soroban** smart contracts and hardware-integrated smart meters. We turn idle solar capacity into a liquid asset.

## 🚀 Overview

In West Africa, energy poverty is often a distribution and trust problem. **Connect** solves this by:

1.  **Verifying Consumption:** Putting hardware meter data "on-chain" via an Oracle.
2.  **Automating Payments:** Using Soroban smart contracts to settle micro-payments in real-time.
3.  **Inclusive Access:** Providing a USSD interface for users without smartphones or consistent data.

-----

## 🛠 Technical Architecture

### 1\. Hardware Layer (The Meter)

  * **PCB & Firmware:** Custom-designed boards using ESP32/Arduino for energy monitoring.
  * **The Energy Oracle:** A bridge that signs and pushes real-time heartbeats (kWh) to the Stellar network.

### 2\. Smart Contract Layer (Soroban)

  * **Escrow Contract:** Holds buyer funds (USDC/NGNC).
  * **Settlement Logic:** Releases payment to the seller's wallet based on validated energy consumption events.

### 3\. Interface Layer (USSD & Web)

  * **USSD Gateway:** A bridge for feature phone users to interact with the Stellar ledger.

-----

## 📟 USSD Flow & Balance Management

We prioritize accessibility. Users can manage their energy wallet and trade power via a simple USSD string (e.g., `*384*100#`).

### User Commands:

| Command | Action | Description |
| :--- | :--- | :--- |
| `*1` | **Check Balance** | View current USDC/NGNC balance in the Stellar wallet. |
| `*2` | **Authorize Energy** | Set a maximum spend limit for the next 24 hours. |
| `*3` | **Top-up Wallet** | Get instructions to deposit NGN via local Stellar anchors. |
| `*4` | **Earnings (Seller)** | View daily revenue generated from energy sales. |

-----

## 📂 Project Structure

```bash
├── hardware/
│   ├── pcb-design/       # Schematics and Gerber files
│   └── firmware/         # C++/Arduino code for meter logic
├── contracts/
│   ├── src/              # Soroban Rust contracts (Settlement & Escrow)
│   └── tests/            # Contract testing suite
├── oracle/
│   └── heartbeat.py      # Script to push hardware data to Stellar
└── interface/
    ├── ussd-bridge/      # Logic for USSD-to-Stellar transactions
    └── web-dashboard/    # Frontend for real-time monitoring
```

-----

## ⚙️ Setup & Installation

### Prerequisites

  * [Rust & Soroban CLI](https://soroban.stellar.org/docs/getting-started/setup)
  * [Stellar SDK](https://www.google.com/search?q=https://github.com/stellar/py-stellar-base)
  * [Arduino IDE](https://www.arduino.cc/en/software) (for hardware firmware)

### Deploying Contracts

1.  Build the contract:
    ```bash
    soroban contract build
    ```
2.  Deploy to Futurenet/Testnet:
    ```bash
    soroban contract deploy --wasm target/wasm32-unknown-unknown/release/connect_settlement.wasm --source-account <YOUR_SECRET> --rpc-url https://soroban-testnet.stellar.org:443 --network-passphrase 'Test SDF Network ; September 2015'
    ```

-----

## 🎯 Roadmap (First 30 Days)

  - [ ] **Week 1:** Finalize PCB schematics and order initial prototypes.
  - [ ] **Week 2:** Deploy the base Settlement Smart Contract on Soroban Testnet.
  - [ ] **Week 3:** Integrate the Hardware-to-Chain Oracle (pushing simulated data).
  - [ ] **Week 4:** Launch USSD simulation for balance management and authorization.

-----

## 👥 Team

  * **Anosike Mmerichukwu** – Product Strategy & Operations (COO, Switch Electric)
  * **Godwin Igwurude** – Hardware Design & Soroban Developmen

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
