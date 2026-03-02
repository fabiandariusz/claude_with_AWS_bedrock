from main import calculate_pi

def test_pi_calculation():
    """
    Test the calculate_pi function to verify it calculates Pi accurately.
    """
    # Calculate Pi to 5 decimal places
    result = calculate_pi(5)
    
    # The value of Pi to 5 decimal places is 3.14159
    expected = 3.14159
    
    # Compare the result with the expected value
    if result == expected:
        print(f"✓ Test passed! Pi calculated correctly: {result}")
    else:
        print(f"✗ Test failed! Expected {expected}, but got {result}")

if __name__ == "__main__":
    print("Testing Pi calculation function...")
    test_pi_calculation()
    
    # You can also test with different precision levels
    print("\nCalculating Pi with different precision levels:")
    for digits in [1, 2, 3, 4, 5, 6, 7]:
        pi_value = calculate_pi(digits)
        print(f"Pi to {digits} digit{'s' if digits > 1 else ''}: {pi_value}")