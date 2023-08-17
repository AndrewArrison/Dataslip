from PIL import Image, ImageDraw
import os

def show_menu():
    print("Menu:")
    print("1. Encode")
    print("2. Decode")
    print("3. Credit")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("cls" if os.name == "nt" else "clear")
                        # Get input from the user
            user_input = input("Enter the data: ")

            # Open a text file in write mode
            file_name = "input.txt"
            with open(file_name, "w") as file:
                # Write the user input to the file
                file.write(user_input)

            def text_to_binary(text):
                binary_data = ''.join(format(ord(char), '08b') for char in text)
                return binary_data

            def read_file(file_path):
                try:
                    with open(file_path, "r") as file:
                        content = file.read()
                        return content
                except FileNotFoundError:
                    print("File not found.")
                    return None

            def write_binary_to_file(binary_data):
                try:
                    with open("binary.txt", "w") as file:
                        file.write(binary_data)
                except Exception as e:
                    print("Error writing to file:", e)

            file_path = "input.txt"
            content = read_file("input.txt")
            
            if content is not None:
                binary_data = text_to_binary(content)
                write_binary_to_file(binary_data)
                os.remove("input.txt")


            def read_binary_file(file_path):
                try:
                    with open(file_path, "r") as file:
                        binary_data = file.read().strip()
                        return binary_data
                except FileNotFoundError:
                    print("File not found.")
                    return None

            def create_image(binary_data, output_path):
                strip_width = 2
                height = 20
                image_width = strip_width * len(binary_data)
                
                image = Image.new("RGB", (image_width, height), "white")
                draw = ImageDraw.Draw(image)
                
                for i, bit in enumerate(binary_data):
                    if bit == '1':
                        strip_height = 20
                    else:
                        strip_height = 15
                    x1, y1 = i * strip_width, height - strip_height
                    x2, y2 = (i + 1) * strip_width - 1, height - 1
                    draw.rectangle([x1, y1, x2, y2], fill="black")
                
                image.save("dataslips/" + output_path)
                # print(f"Image has been created and saved as '{output_path}'.")

            file_path = "binary.txt"
            binary_data = read_binary_file(file_path)
            
            if binary_data is not None:
                output_path = input("path for dataslip output: ") + ".png"
                # output_path = outpat
                create_image(binary_data, output_path)
                os.remove("binary.txt")
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Saved as '{output_path}'.")
                print("Created by:")
                print("Andrew Arrison")
            break
        elif choice == "2":
            os.system("cls" if os.name == "nt" else "clear")
            # Load the image
            image_path = input("path to dataslip: ") + ".png"
            os.system("cls" if os.name == "nt" else "clear")
            image = Image.open("dataslips/" + image_path)

            # Get the dimensions of the image
            image_width, image_height = image.size

            # Define the step size for reading pixels
            step_size = 2

            # Initialize a list to store the converted data
            converted_data = []

            # Iterate through the top row from left to right with the specified step size
            for x in range(0, image_width, step_size):
                pixel = image.getpixel((x, 0))  # Get pixel color at (x, 0)

                # Check if the pixel is black (assuming RGB values of black are (0, 0, 0))
                if pixel == (0, 0, 0):
                    converted_data.append("1")
                else:
                    converted_data.append("0")

            # Write the converted data to a text file
            output_file = "data.txt"
            with open(output_file, "w") as f:
                f.write("".join(converted_data))

            def binary_to_text(binary_data):
                text = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
                return text
                
            def read_binary_file(file_path):
                try:
                    with open(file_path, "r") as file:
                        binary_content = file.read()
                        return binary_content
                except FileNotFoundError:
                    print("Binary file not found.")
                    return None

            binary_file_path = "data.txt"
            binary_content = read_binary_file(binary_file_path)

            if binary_content is not None:
                text = binary_to_text(binary_content)
                print("Decoded text:", text)
                os.remove("data.txt")
                print("Created by:")
                print("Andrew Arrison")

            break
        elif choice == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print("Created by:")
            print("Andrew Arrison")
            print("GitHub: github.com/andrewarrison")
            break
        elif choice == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
