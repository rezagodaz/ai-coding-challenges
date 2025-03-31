def validate_binary_input(func):
    """Decorator to validate that the input is a non-empty binary string."""
    def wrapper(self, binary_str):
        if not isinstance(binary_str, str) or not binary_str:
            raise ValueError("Input must be a non-empty binary string.")
        if any(bit not in '01' for bit in binary_str):
            raise ValueError("Input must only contain '0' and '1'.")
        
        return func(self, binary_str)  # Call the original function

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
        state = self.initial_state  # Reset state
        for bit in binary_str:
            state = self.transitions[state][bit]
        return state

# Example usage with error handling
fsm = Mod3FSM()

def safe_fsm_call(binary_str):
    try:
        return fsm.process(binary_str)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    return None

# Test cases
print(safe_fsm_call("1101"))  # Output: 1
print(safe_fsm_call("1110"))  # Output: 2
print(safe_fsm_call("1111"))  # Output: 0
print(safe_fsm_call("abc"))   # Input Error
print(safe_fsm_call(""))      # Input Error
print(safe_fsm_call("10102")) # Input Error
