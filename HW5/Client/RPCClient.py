import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    while True:
        print("Enter an option ('s', 'm', 'f', 'x'):\n  (S)ort numbers\n  (M)essage (send)\n  (F)ile (request)\n  e(X)it")
        option = input().lower()

        if option == 's':
            numbers = input("Enter your numbers: ").split()
            numbers = list(map(int, numbers))
            sorted_numbers = proxy.sort_list(numbers)
            print(' '.join(map(str, sorted_numbers)))

        elif option == 'm':
            message = input("Enter your message:\n")
            messages = proxy.print_message(message)
            for msg in messages:
                print(msg)

        elif option == 'f':
            filename = input("Which file do you want?\n")
            file_content = proxy.get_file(filename)
            if file_content:
                with open(filename, 'wb') as file:
                    file.write(file_content.data)
                print(f"File {filename} has been downloaded.")
            else:
                print("File does not exist!")

        elif option == 'x':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
