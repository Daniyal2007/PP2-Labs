
import os

def count_lines(file_path):
    counter = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                counter += 1
    except FileNotFoundError:
        print("Error: File not found. Check the file name and path.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    return counter

file_path = r"C:\Users\Baha\Desktop\vzlom fifa\example.txt"
line_count = count_lines(file_path)

if line_count is not None:
    print("Number of lines:", line_count)
