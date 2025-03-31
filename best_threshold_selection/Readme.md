# Best Threshold Selection

## :memo: Problem Overview

This project focuses on evaluating a binary classification model by determining the best threshold that yields a recall greater than or equal to 0.9. The best threshold is selected based on the highest F1-score among those that meet the recall requirement.

### Input

The input is a list of tuples, each containing:

- **Threshold**: The confidence score threshold.
- **True Positives (TP)**: Number of correct positive predictions.
- **True Negatives (TN)**: Number of correct negative predictions.
- **False Positives (FP)**: Number of incorrect positive predictions.
- **False Negatives (FN)**: Number of incorrect negative predictions.

### Output

The function returns the best threshold that meets the criteria (recall >= 0.9). If no threshold satisfies the requirement, it returns `None`.

## :wrench: Solution Implementation

The solution is implemented in `best_threshold.py`, which:

1. Iterates over the input data (threshold, TP, TN, FP, FN).
2. Computes recall, precision, and F1-score.
3. Selects the best threshold based on the highest F1-score where recall ≥ 0.9.

Example Usage:

```python
data = [
    (0.1, 90, 50, 10, 10),
    (0.2, 85, 60, 15, 5),
    (0.3, 80, 70, 20, 10),
]
```

best_t = best_threshold(data)
print(f"Best threshold: {best_t}")

:rocket: How to Run

1. Clone the repository:

git clone https://github.com/rezagodaz/ai-coding-challenges.git
cd ai-coding-challenges/best_threshold_selection

2. Run the solution:
   python best_threshold.py

:rocket: License
This project is licensed under the MIT License.
