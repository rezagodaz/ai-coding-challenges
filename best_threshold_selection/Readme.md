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

```python
from typing import List, Tuple, Optional

def best_threshold(data: List[Tuple[float, int, int, int, int]]) -> Optional[float]:
    best_threshold = None
    best_f1 = 0

    for threshold, TP, TN, FP, FN in data:
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        print(f"Threshold: {threshold}, Recall: {recall:.2f}, Precision: {precision:.2f}, F1-score: {f1_score:.2f}")

        if recall >= 0.9 and f1_score > best_f1:
            best_threshold = threshold
            best_f1 = f1_score

    return best_threshold
```

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
