def hello():
    print("hello how are you ?")
    
def calculate_pi(digits=5):
    """
    Calculate the value of Pi to the specified number of digits using the Nilakantha series.
    
    Args:
        digits (int): Number of decimal digits of precision (default: 5)
        
    Returns:
        float: The value of Pi with the specified precision
    """
    # Start with the first term of the series
    pi = 3.0
    
    # The Nilakantha series converges relatively quickly
    # We'll use a large number of iterations to ensure 5 digit precision
    iterations = 100000
    
    # Starting with the first term (k=1)
    sign = 1
    for k in range(1, iterations + 1):
        # Formula: 4/(2k*(2k+1)*(2k+2))
        denominator = (2 * k) * (2 * k + 1) * (2 * k + 2)
        term = 4 / denominator
        pi += sign * term
        sign *= -1
    
    # Round to the specified number of digits
    return round(pi, digits)