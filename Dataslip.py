from PIL import Image, ImageDraw
import os

def show_menu():
    print("Menu:")
    print("1. Encode")
    print("2. Decode")
    print("3. Credit")
    print("4. Exit")

def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

def binary_to_text(binary_data):
    text = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    return text

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")
        return None

def write_to_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            file.write(data)
    except Exception as e:
        print("Error writing to file:", e)

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
        strip_height = 20 if bit == '1' else 15
        x1, y1 = i * strip_width, height - strip_height
        x2, y2 = (i + 1) * strip_width - 1, height - 1
        draw.rectangle([x1, y1, x2, y2], fill="black")
    
    image.save("dataslips/" + output_path)
    print(f"Image has been created and saved as '{output_path}'.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("cls" if os.name == "nt" else "clear")

            user_input = input("Enter the data: ")
            file_name = "input.txt"
            write_to_file(file_name, user_input)

            file_path = "input.txt"
            content = read_file(file_path)
            
            if content is not None:
                binary_data = text_to_binary(content)
                write_to_file("binary.txt", binary_data)
                os.remove("input.txt")

                output_path = input("Path for dataslip output: ") + ".png"
                create_image(binary_data, output_path)
                os.remove("binary.txt")
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Saved as '{output_path}'.")
                print("Created by:\nAndrew Arrison")
            break

        elif choice == "2":
            os.system("cls" if os.name == "nt" else "clear")

            image_path = input("Path to dataslip: ") + ".png"
            os.system("cls" if os.name == "nt" else "clear")
            image = Image.open("dataslips/" + image_path)

            image_width, image_height = image.size
            step_size = 2
            converted_data = []

            for x in range(0, image_width, step_size):
                pixel = image.getpixel((x, 0))
                converted_data.append("1" if pixel == (0, 0, 0) else "0")

            output_file = "data.txt"
            write_to_file(output_file, "".join(converted_data))

            binary_file_path = "data.txt"
            binary_content = read_binary_file(binary_file_path)

            if binary_content is not None:
                text = binary_to_text(binary_content)
                print("Decoded text:", text)
                os.remove("data.txt")
                print("Created by:\nAndrew Arrison")

            break

        elif choice == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print("Created by:\nAndrew Arrison")
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
