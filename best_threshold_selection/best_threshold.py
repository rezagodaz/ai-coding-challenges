from typing import List, Tuple, Optional

def best_threshold(data: List[Tuple[float, int, int, int, int]]) -> Optional[float]:
    """
    Finds the best threshold that yields recall >= 0.9.

    Parameters:
        data: List of tuples, where each tuple is (threshold, TP, TN, FP, FN).

    Returns:
        The best threshold or None if no threshold meets the criteria.
    """
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


#Example of realistic input data (threshold, TP, TN, FP, FN)
data = [
    (0.1, 95, 40, 5, 5),
    (0.2, 88, 55, 12, 7),
    (0.3, 83, 65, 17, 8),
    (0.4, 78, 75, 22, 7),
    (0.5, 72, 82, 28, 8),
    (0.6, 65, 88, 35, 12),
    (0.7, 58, 90, 42, 10),
    (0.8, 45, 93, 55, 7),
    (0.9, 33, 95, 67, 5),
]

best_t = best_threshold(data)
print(f"Best threshold: {best_t}")

