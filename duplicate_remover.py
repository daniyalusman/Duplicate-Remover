while True:
    def duplicate_remover(file_path):
        unique_items = []
        try:
            # Opening file in read mode
            with open(file_path, 'r') as input_file:
                # Reading File Content
                for line in input_file:
                    line = line.strip()
                    if line not in unique_items:
                        unique_items.append(line)
            # Writing unique items in file
            with open('duplicate_removed.txt', 'w') as output_file:
                for value in unique_items:
                    output_file.write(f'{value}\n')
                print("File saved successfully.")
            return True
        except FileNotFoundError:
            print("File does not exist. Please check the file path and try again.")
            return False
    file_path = input("Enter absolute file path e.g (E:\\Folder\\sample.txt): ")
    file_path = r"{}".format(file_path)

    if duplicate_remover(file_path):
        break

    






