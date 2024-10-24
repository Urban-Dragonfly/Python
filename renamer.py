import os

def rename_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    for filename in files:
        # Check if the file starts with "zadanie"
        if filename.startswith("zadanie"):
            # Construct the full file path
            old_file = os.path.join(directory, filename)
            
            # Skip directories
            if os.path.isdir(old_file):
                continue
            
            # Construct the new file name
            new_filename = filename.replace("zadanie", "cwiczenie", 1)
            new_file = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

#usage
directory = 'C:\AiProjects\Kodilla\Python'
rename_files(directory)
