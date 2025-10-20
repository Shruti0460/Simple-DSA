
# Problem: Check if a triplet exists with given sum


def has_triplet_sum(arr, target):
    """
    Function to check if there exists a triplet in arr[] with sum equal to target.
    Returns True if found, False otherwise.
    """
    n = len(arr)
    
    # Brute-force approach: check all triplets
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False

def main():
    arr = [1, 4, 45, 6, 10, 8]
    target = 13
    
    if has_triplet_sum(arr, target):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
