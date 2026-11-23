# Diseña programa para calcular con una funcion valores estadisticos de media y maximo 
def estadisticas(numbers):
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
