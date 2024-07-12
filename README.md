# Duplicate Remover

Duplicate Remover is a straightforward Python script designed to remove duplicate items from a text file and save the unique items to a new file.

## Installation and Usage

### Windows

1. **Ensure Python is Installed:**
   - If Python is not already installed on your system, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions.

2. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/duplicate-remover.git
   ```

3. **Navigate to the directory:**
   ```bash
   cd duplicate-remover
   ```

4. **Run the script:**
   - Double-click the `duplicate_remover.py` file to run it, or open a command prompt and execute:
     ```bash
     python duplicate_remover.py
     ```

5. **Enter the absolute file path:**
   - Provide the full path to the text file you want to process when prompted.

6. **Result:**
   - The script will read the file, remove duplicates, and save the unique items to `duplicate_removed.txt` in the same directory.
   - You will see a confirmation message indicating the file has been saved successfully or an error message if the file does not exist.

### Linux

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/duplicate-remover.git
   ```

2. **Navigate to the directory:**
   ```bash
   cd duplicate-remover
   ```

3. **Run the script:**
   - Open a terminal and execute:
     ```bash
     python3 duplicate_remover.py
     ```

4. **Enter the absolute file path:**
   - Provide the full path to the text file you want to process when prompted.

5. **Result:**
   - The script will read the file, remove duplicates, and save the unique items to `duplicate_removed.txt` in the same directory.
   - You will see a confirmation message indicating the file has been saved successfully or an error message if the file does not exist.

## Example

Suppose you have a file `sample.txt` with the following content:

```
apple
banana
apple
orange
banana
```

Running the script on `sample.txt` will produce `duplicate_removed.txt` containing:

```
apple
banana
orange
```

## Notes

- Make sure Python is installed on your system and added to your PATH environment variable.
- This script assumes the input file is a text file where each line is treated as a separate item.
