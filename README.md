# Enigma Cipher Engine: Physical-State Rotor Simulation in Python

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)

An authentic electro-mechanical simulation of the WWII German Wehrmacht Enigma I cipher machine in pure Python.

Unlike traditional implementations that simplify Enigma mathematics using static string modular arithmetic, this engine implements a **Physical State Manipulation Model**—faithfully simulating electrical contact points, physical rotor stepping mechanisms, symmetric reverse current paths, and plugboard wire swapping.

---

## 🏛️ Architecture Overview

The simulation models the complete physical electrical circuit of the Enigma I machine:

```
Keypress ──► [Plugboard] ──► [Rotor III] ──► [Rotor II] ──► [Rotor I]
                                                                │
[Lampboard] ◄── [Plugboard] ◄── [Rev Rotor III] ◄── [Rev Rotor II] ◄── [Rev Rotor I] ◄── [Reflector B]
```

### Key Engineering Primitives

1. **Physical Contact Representation**:
   * Rotors (I through V) are represented as ordered lists of single-key mappings corresponding to physical wire contact points on the wheel circumference.
   * Rotor rotation is achieved through physical in-memory list shifts (`x.insert(0, x.pop())`).

2. **Electrical Flow Simulation**:
   * Instead of semantic letter lookups, the signal flows as an indexed electrical impulse (`0` to `25`) mapping directly into the physical wire contact at index `n`.

3. **Mechanical Odometer Stepping**:
   * Rotor stepping is decoupled from encryption lookups. The `step_rotor` function executes once per keypress before current flows, correctly handling rollover carry-overs across right, middle, and left rotors.

4. **Symmetric Inverse Rotors (`rev_rotor`)**:
   * Electrical current flows forward to the reflector, then backward through the rotors. Inverse rotor lists provide mathematical and physical symmetry for the return circuit.

5. **Plugboard (*Steckerbrett*)**:
   * Symmetric bidirectional cable patch panel swapping paired letters at entry and exit.

---

## 🚀 Quickstart

### Prerequisites
* Python 3.8+ (zero external dependencies).

### Running the Simulator
```bash
git clone https://github.com/11whoamiwhyme11/enigma-cipher-engine.git
cd enigma-cipher-engine
python main.py
```

### Example Usage
```text
enter the charcter to encrypt : H
Q
enter the charcter to encrypt : E
C
enter the charcter to encrypt : L
V
enter the charcter to encrypt : L
X
enter the charcter to encrypt : O
M
enter the charcter to encrypt : !
```

*(Enter `!` to terminate the simulation).*

---

## ⚙️ Configuration

Initial rotor ground settings (*Grundstellung*) and plugboard cables are configured in `main.py`:

```python
# Set initial rotor positions (Rotors I through V)
r1_set("A")
r2_set("J")
r3_set("O")

# Configure plugboard cable pairs
l = {
    'A': 'B', 'B': 'A',
    'C': 'D', 'D': 'C'
}
```

---

## 📜 Historical Specifications
* **Rotors Implemented**: Rotors I, II, III, IV, and V (Standard Enigma I German military wiring).
* **Reflector**: Standard *Reflektor B* (*Umkehrwalze B*).
* **Stepping Logic**: Anomaly-free mechanical stepping with carry-over counters.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
