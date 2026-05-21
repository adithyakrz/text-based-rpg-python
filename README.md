# ⚔️ Modular Text-Based RPG Simulator

[cite_start]A terminal-based, object-oriented Python combat engine simulating a real-time tactical battle loop between a Player and an automated Boss[cite: 330, 340]. 

[cite_start]This project demonstrates foundational software engineering architectures essential for production-grade machine learning pipelines, specifically focusing on **Object-Oriented Programming (OOP)**, **inheritance mapping**, and **multi-file module decoupling**[cite: 12, 101, 102].

---

## 🏗️ Architecture & Module Layout

[cite_start]To break away from a single monolithic script and enforce the **Single Responsibility Principle**, the application has been refactored into independent, specialized modules[cite: 4, 22]:

```text
├── Charecter.py                 
├── Boss.py                      
└── TextBasedRPGSimulator.py
```

  

### 🧠 Core Concepts Mastered

* **Object-Oriented Programming (OOP):** Encapsulation of discrete states (`health`, `name`, `attack_power`) and behaviors (`attack()`) into clean, reusable class blueprints.
* **Inheritance Mapping:** The `Boss` class inherits directly from `Charecter`, utilizing `super().__init__()` to seamlessly pass data up and dynamically double the baseline health pool.
* **Encapsulated Scope Isolation:** Each file functions as an entirely isolated programming context. Global standard library utilities (like `randint`) are imported explicitly within the unique module executing them, rather than relying on an entry-point leak.
* **Dynamic Boundary Evaluation:** Prevents floating-point precision limitations by utilizing floor division (`//`) and enforces strict mathematical boundaries via `max()` to eradicate runtime `TypeError` issues during random damage generation.

---

### 🎮 Game Mechanics

* **Dynamic Critical Hits:** Damage includes a randomized variance factor scaled strictly to a fraction of the enemy's current health pool, triggering a unique execution block upon critical thresholds.
* **Aggressive Boss AI:** Features an automated $30\%$ probability matrix overriding standard attacks to execute a devastating `mega_attack` dealing $2\times$ baseline damage.
* **Synchronous Turn Resolution:** Strict game loop state evaluations guarantee that knockout conditions trigger breaks instantly upon health dropping $\le 0$, preventing lingering "ghost attacks" or out-of-order text rendering.

---

### 🚀 How to Run the Project

Ensure you have Python installed locally. Clone the repository, navigate to the project directory, and execute the main application entry point module:

```bash
python TextBasedRPGSimulator.py
```

##Sample Gameplay Trace

```
Plaintext
Player info:
Name: Pikachu
Health: 4000
Attack Power: 200

Boss info:
Name: Charizard
Health: 3000
Attack Power: 150

Pikachu Attacks
Hit! Damage: 490

Charizard Attacks
Critical Hit!! Damage: 726
-> Status: Pikachu HP: 3274 | Charizard HP: 5510

...
Pikachu Attacks
Critical Hit!! Damage: 200

Final Status: Pikachu HP: 301 | Charizard HP: -9
🏆 Pikachu Wins the match against Charizard!
```
