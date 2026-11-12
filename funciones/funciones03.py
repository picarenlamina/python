# Return multiple values from a function
def calculate_stats(numbers):
    """Return multiple statistics about a list of numbers"""
    if not numbers:
        return None, None, None  # Handle empty list
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    
    return total, average, maximum  # Return multiple values

# Use the returned values
scores = [85, 92, 78, 96, 88]
total, avg, max_score = calculate_stats(scores)

print(f"Total: {total}, Average: {avg:.1f}, Max: {max_score}")
