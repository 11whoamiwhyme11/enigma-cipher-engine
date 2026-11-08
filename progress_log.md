# Enigma Simulation Project: Progress and Design Log
**Date:** August 17, 2026  
**Developer:** [User]  
**Topic:** Re-engineering Enigma Rotors using Physical State Manipulation

---

## 1. Core Philosophy & Design Constraint
Unlike typical implementations that simplify the Enigma simulation using math offsets on static strings, the developer chose to adhere to a **Physical Simulation Model**:
* **Representation:** Rotors are represented as a list of 26 single-key dictionaries (`[{'A': 'E'}, {'B': 'K'}, ...]`), where each dictionary represents a physical contact point.
* **Rotation:** Shifting the rotor is simulated by physically rotating the list in memory using `.insert(0, x.pop())`.

The objective of today's session was to debug and solve the logical challenges of making this physical representation behave exactly like the mechanical gears and electrical flows of the real Enigma.

---

## 2. Key Breakthroughs & Solutions

### Breakthrough A: From "Semantic Search" to "Electrical Flow"
* **The Bug:** Originally, the lookup function iterated through the entire list to find a dictionary matching `key == input_letter`. This meant that even if the list was physically rotated, the loop would always find the exact same dictionary and map it the same way. The physical rotation had no effect on the cipher.
* **The Thinking Style:** The developer realized a crucial flaw in the mental model—the program was performing a "semantic search" (finding a letter by name) instead of simulating "electrical flow" (finding where a physical wire touches a contact).
* **The Unique Solution:** The input letter is converted into a 0-25 index (using a reference alphabet). The signal is then fed directly into `x[index]`, representing the physical wire contact at index `n`. Since the list `x` is rotated, the dictionary sitting at index `n` changes dynamically with the rotation.

### Breakthrough B: Separation of Concerns (Mechanical Stepping vs. Electrical Flow)
* **The Bug:** If rotor rotation and incrementing counters (`mr_1`, `mr_2`, etc.) are placed inside the rotor mapping functions, they trigger multiple times because the signal flows through each rotor twice (once on the way forward to the reflector, and once on the way back). This caused the rotors to step 6 times per keypress instead of 1.
* **The Thinking Style:** Recognizing that keeping track of rotation inside the lookup functions caused "double-dipping", the developer abstracted the mechanical rotation away from the lookup process.
* **The Unique Solution:** Created a dedicated `step_rotor` function. This function is placed inside the main loop and runs **exactly once** before any signal encryption begins. It handles the rollover conditions (`if mr_1 == 26:`) and physically shifts the lists. The encryption functions were stripped of state-mutation code, leaving them to perform pure lookups.

### Breakthrough C: Resolution of Scope and Immutable Import Trap
* **The Bug:** Modifying the step counters inside the rotor functions triggered `UnboundLocalError`. Furthermore, importing counters via `from rotors import mr_1` in `main.py` created local copies of the immutable integers, meaning state changes inside the module did not sync with `main.py`.
* **The Solution:** Inside the newly created `step_rotor` function, the developer used the `global` keyword to declare modifying rights to the counters. Because the stepping is now handled entirely within `rotors.py` and the lists are mutated in place, `main.py` is completely insulated from tracking the integers, resolving the import synchronization bug.

### Breakthrough D: Symmetric Reverse Mapping via `rev_rotor` Lists
* **The Bug:** On the return path from the reflector, the electrical signal flows backward through the rotors (from output to input). Doing a standard index lookup would execute the forward mapping again, which is incorrect.
* **The Thinking Style:** Rather than writing complex reverse search algorithms (which would require searching the list values of the forward rotors), the developer had the unique idea to represent the reverse flow as a physical set of **inverse rotor lists** (`rev_rotor_1` to `rev_rotor_5`).
* **The Unique Solution:**
  1. Built reverse lists where each entry maps the output letter back to the input letter, ordered alphabetically by their keys.
  2. Integrated these reverse lists into the parallel rotation code in `step_rotor` to keep the forward and reverse list views of the physical wheel in perfect sync.
  3. Passed the reverse lists (`rev_rotor_1` etc.) into the exact same mapping functions on the return pass, preserving code symmetry and eliminating the need for separate reverse-search loops.

### Breakthrough E: Preventing Reassignment Race Conditions during Setup
* **The Bug:** During startup setup, when slicing the rotors to their initial offsets, the developer noticed that reassigning `rotor_1` first changed the output of `.index(i)` in the subsequent line where `rev_rotor_1` was being sliced, leaving the reverse rotor unsynchronized (offset by 0 steps).
* **The Thinking Style:** Tracing the sequential logic of execution, the developer recognized that the source of truth was being mutated mid-operation.
* **The Unique Solution:** Cached the original target index in a temporary variable `g` *before* any list reassignments took place, ensuring both the forward and reverse rotor lists were sliced by the exact same offset.

### Breakthrough F: Symmetric Plugboard Swapping
* **The Bug:** Implementing a plugboard requires two-way mapping (e.g. if A maps to B, B must map to A) and must not crash or change letters that are not plugged.
* **The Thinking Style:** The developer modeled the plugboard as a physical cable patch panel by passing a symmetric dictionary of swaps and executing a direct lookup on the character.
* **The Unique Solution:** Implemented the `plugboard(x: dict, y: str)` function, which intercepts the character at the very beginning (upon input entry) and at the very end (before output display), returning the swapped letter if plugged, and the original letter if untouched.

### Breakthrough G: Streamlining the User Interface
* **The Bug:** The interface used the `eval()` wrapper on inputs, requiring users to explicitly add quote wraps (`"A"`) to prevent variable lookup crashes.
* **The Solution:** Removed the `eval` wrapper to use pure string inputs, allowing direct interactive typing (e.g., entering `A` directly).

---

## 4. Final Deployment Log
At project completion, the following declaration was recorded:
> *"i have become nazi now i wage war on the world 🤣🤣🤣🤣🤣🤣😅😅😅😅, i dont know why i said that log it to the log book and we are officially done wooohooooooooo what a rush"*
