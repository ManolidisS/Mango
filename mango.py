import os
version = "1.0.0"

####################################################################################################

def compile(filename:str):
    contents = (open(filename)).read()
    contents = contents.splitlines()
    contents_array = []
    for i in range(len(contents)):
        contents_array.append(contents[i].split("!"))
    for i in range(len(contents_array)):
        for x in range(len(contents_array[i])):
            mango = contents_array[i][x]
            mango = [ango for  ango in mango]
            mango = mango[1:] # Removes "M-"
            mango = mango[:-3] # Removes "-ngo"
            mango = len(mango) # No. of "a"s.
            contents_array[i][x] = mango # Each mango gets replaced with the no. of "a"s.
    for i in range(len(contents_array)):
        for x in range(len(contents_array[i])):
            contents_array[i][x] = chr(contents_array[i][x]) # Converts ascii number into character.
    for i in range(len(contents_array)):
        contents_array[i] = "".join(char for char in contents_array[i]) # Joins the characters together to make lines.
    contents = "\n".join(line for line in contents_array) # Joins the lines together in one string, with line breaks.
    return contents

def commands():
    print('''List of commands:
          commands (/help/cmds): This command; shows a list of all commands and aliases.
          exit (/quit): Terminates this process.
          compile [mangofile].mango [pythonfile].py: Compiles the .mango file into the .py file.
          run [pythonfile].py: runs the python file.''')
    
def full_compile(mangofile:str,pythonfile:str):
    compiled = compile(mangofile)
    with open(pythonfile, "w") as file:
        file.write(compiled[:-1]) # There was an extra null byte on the end, I'd rather remove it than fix my code.

def start():
    print("""
 __   __                       _ 
|  \\ /  |                     | |
|   v   | __  ___  ___   _ ___| |
| |\\_/| |/  \\/ / |/ ( \\ / ) _ \\_|
| |   | ( ()  <| / / \\ v ( (_) ) 
|_|   |_|\\__/\\_\\__/   | | \\___(_)
                      | |        
                      |_|        
""")
    print("Mango; the programming language.")
    print(f"Version {version} - © Spyridon Manolidis 2024; MIT License")

def main():
    command = input(">>> ")
    if (command.lower()).strip() in ["help", "commands", "cmds"]:
        commands()
    elif (command.lower()).strip() in ["exit", "quit"]:
        exit()
    elif ((command.strip()).split(" ")[0]).lower() in ["compile"]:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        try:
            full_compile(script_dir+"\\"+((command.strip()).split(" ")[1]),script_dir+"\\"+((command.strip()).split(" ")[2])) # Uses os to get the directory, I do this complex thing instead of just saying the file normally because my computer specifically somehow has a rare glitch where this doesn't work, so I have to give the full path.
        except Exception as err:
            print(err)
    elif ((command.strip()).split(" ")[0]).lower() in ["run", "execute"]:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        exec(open(script_dir+"\\"+((command.strip()).split(" ")[1])).read())
    elif (command.lower()).strip() == "":
        pass
    else: 
        print("Invalid command. Please use the command 'commands' for a list of all commands.")

####################################################################################################

start()
while True:
    main()
