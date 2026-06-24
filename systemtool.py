import os
import sys
import platform

class SystemTool:
    def __init__(self):
        self.name = "Hermione_System_Tool"

    def run_command(self, command):
        command = command.lower().strip()

        try:
            # 1. Get Operating System Information
            if command == "os info":
                return f"Result -> OS: {platform.system()} | Release: {platform.release()} | Architecture: {platform.architecture()[0]}"
            
            # 2. Get Python Version
            elif command == "python version":
                return f"Result -> Python Version: {sys.version.split()[0]}"
            
            # 3. Get Current Working Directory Path
            elif command == "current path":
                return f"Result -> Current Folder Path: {os.getcwd()}"
            
            # 4. List All Files in the Current Folder
            elif command == "list files":
                files = os.listdir('.')
                if not files:
                    return "Result -> The folder is empty."
                return f"Result -> Files in this folder: {', '.join(files)}"
            
            else:
                return "Unknown command. Available tools: os info, python version, current path, list files"

        except Exception as e:
            return f"An error occurred: {str(e)}"

# Interactive loop to run the System Tool
if __name__ == "__main__":
    agent = SystemTool()
    print(f"=== {agent.name} is online ===")
    print("Type 'exit' to stop.")
    print("Commands: os info | python version | current path | list files")
    print("-" * 40)

    while True:
        user_input = input("Enter command: ")
        if user_input.lower().strip() == "exit":
            print("Shutting down System Tool. Goodbye!")
            break
        
        if not user_input.strip():
            continue
            
        response = agent.run_command(user_input)
        print(response)
        print("-" * 40)