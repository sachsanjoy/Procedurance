# Procedurance
Procedural generation art project
def get_column_letter(n):
    """
    Convert a column index (1-based) to an Excel column letter.
    
    Parameters:
    n (int): The column number (1-based index).
    
    Returns:
    str: The corresponding Excel column letter.
    """
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result

# Example usage
column_number = 28
column_letter = get_column_letter(column_number)
print(f"The column letter for column number {column_number} is {column_letter}")