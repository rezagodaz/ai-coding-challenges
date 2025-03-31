### **Modulo 3 Using FSM - `README.md`**

# Modulo 3 Using Finite State Machine (FSM)

## :memo: Problem Overview

This project implements a **Finite State Machine (FSM)** to compute the remainder when a binary string is divided by 3. The FSM transitions between three states based on the binary input, and the final state represents the remainder.

## :wrench: Solution Implementation

The solution is implemented in `Mod3FSM.py`, using an FSM with three states (0, 1, 2), which correspond to the remainders when dividing by 3.

Summary of Highlights of this project:
✅ Error Handling: Prevents crashes due to invalid input.
✅ Input Validation: Ensures input correctness before processing.
✅ Encapsulation – Keeps validation logic separate from process(), making the class cleaner.
✅ Reusability – The decorator can be applied to other methods if needed.
✅ Readability – The process() method is now focused only on FSM logic.

```python
def validate_binary_input(func):
    """Decorator to validate binary input."""
    def wrapper(self, binary_str):
        if not isinstance(binary_str, str) or not binary_str:
            raise ValueError("Input must be a non-empty binary string.")
        if any(bit not in '01' for bit in binary_str):
            raise ValueError("Input must only contain '0' and '1'.")

        return func(self, binary_str)

    return wrapper

class Mod3FSM:
    def __init__(self):
        self.initial_state = 0
        self.transitions = {
            0: {'0': 0, '1': 1},
            1: {'0': 2, '1': 0},
            2: {'0': 1, '1': 2}
        }

    @validate_binary_input
    def process(self, binary_str):
        state = self.initial_state
        for bit in binary_str:
            state = self.transitions[state][bit]
        return state
```

Example Usage:

```python
fsm = Mod3FSM()

print(fsm.process("1101"))  # Output: 1
print(fsm.process("1110"))  # Output: 2
print(fsm.process("1111"))  # Output: 0
```

:rocket: How to Run

1. Clone the repository:

```
   git clone https://github.com/rezagodaz/ai-coding-challenges.git
   cd ai-coding-challenges/Mod3FSM
```

2. Run the solution:

```
python Mod3FSM.py
```

:rocket: License

This project is licensed under the MIT License.
