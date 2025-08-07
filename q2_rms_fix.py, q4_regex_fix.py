# Q2: Fixing bug in RMS calculation
import numpy as np

def calculate_rms(data):
    """
    Calculates the root mean square (RMS) of a list of numbers.
    Args:
        data (list): List of numeric values
    Returns:
        float: RMS value
    """
    data_array = np.array(data)
    mean_of_squares = np.mean(data_array ** 2)
    rms_value = float(np.sqrt(mean_of_squares))  # Corrected: removed dtype argument
    return rms_value

# Input data
numbers = [1, 2, 3, 4, 5]  # Must be a list, not a set

# Calculate and print RMS
result = calculate_rms(numbers)
print(f"The calculated RMS is: {result:.4f}")  # Expected: 3.3166


# Q4: Fixing regex to correctly identify generic image URLs
import re

def is_generic_image(image_url):
    """
    Checks if the image URL matches a known generic pattern.
    """
    # Updated regex to match width starting from 1700–1999
    generic_patterns = [r".*height=\d+&width=1[7-9]\d\d"]
    return any(re.search(pattern, image_url) for pattern in generic_patterns)

# Test URL
image_url = "https://cdn.mathpix.com/cropped/2025_04_01_7b93083882288e619e6bg-01.jpg?height=332&width=1787&top"

# Determine and print result
if is_generic_image(image_url):
    x = 1
else:
    x = 0

print(x)  # Expected output: 1

