# Text-Based RPG Simulator

A terminal-based combat simulator built in Python to practice Core Object-Oriented Programming (OOP) concepts.

## 🚀 Features
- **Object-Oriented Design:** Built using custom `Character` and `Boss` classes.
- **Inheritance & Polymorphism:** The `Boss` class inherits from `Character` but features doubled health pools and a unique `mega_attack()` method.
- **Dynamic Math Scaling:** Damage variance and critical hits scale dynamically based on the opponent's current health.
- **Robust Loop Control:** Real-time game state evaluation to prevent invalid post-knockout turns.

## 🛠️ Concepts Practiced
- Python Class Structures (`class`, `__init__`, `self`)
- Subclassing & Parent Class Linking (`super()`)
- Error Exception Handling (Fixing floating-point `TypeError` limitations using floor division)
- Standard Library Integrations (`random.randint`, `random.random`)
