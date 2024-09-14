import tkinter as tk
import time
import webbrowser
import math
import subprocess
import os
import keyboard
#process
global file_path
variables = {} 
printer = []
clas_tydh = {} 
comments = []
windows = {}
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
def process_command(syntax, variables):
    global title
    
    global var_value
    global var_name 
    global var_type
    global window_name
    global label_text
    global font_name
    global font_size
    global params
    global command
    global run_drift

    command = syntax[len("spark."):]
    #handle spark print syntax
    if syntax.startswith("imports"):
        impots = syntax[len("imports "):]
        if impots.startswith("system"):
            if syntax.startswith("spark."):
                gop = syntax[len("spark."):]
                if gop.startswith("system."):
                    foip = gop[len("system."):]
                    if foip.startswith("file."):
                        youp = foip[len("file."):]
                        if youp.startswith("create("):
                            opiuyt = youp[len("create("):-1]
                            with open(opiuyt, "w") as file:
                                file.write("spk main class")
                                print("working")
    if syntax.startswith("spark."):
    
    
     

        command = syntax[len("spark."):]
 
        if command.startswith("createWindow("):
                    window_name = command[len("createWindow("):-1]
                    create_window(window_name)
                    
                    


        elif command.startswith("sVar "):
              
             var_command = command[len("sVar "):]
             if "=" in var_command:
                  var_name, var_value = var_command.split("=", 1)
                  var_name = var_name.strip()
                  var_value = var_value.strip()           
                
             try:
                var_value = float(var_value)
             except ValueError:
                pass
             
             variables[var_name] = var_value

        elif command.startswith("os."):
                yhu = command[len("os."):]
                if yhu.startswith("command"):
                    thu = yhu[len("command "):]
                    
                    
                        
                        
                    os.system(thu)

        elif command.startswith("getIn"):
            inr = command[len("getIn "):]
           
            while True:
                if keyboard.is_pressed(inr):
                    print(f"Key pressed: {inr}")
                # Optionally, add a small delay to prevent multiple prints for a single press
                keyboard.wait(inr)
            
            # Allow the user to exit the loop by pressing 'Esc'
                if keyboard.is_pressed('Esc'):
                    print("Exiting key listening loop.")
                    break
                 
                 
                
                    
                        

        elif command.startswith("if("):
             condition = command[len("if("):command.index(")")]
             
             condition_result = evaluate_condition(condition, variables) 
             
             
             if condition_result:
                  #get block
                  start_index = syntax.index("{") + 1
                  end_index = syntax.index("}") 
                  code_block = syntax[start_index:end_index]   

                  #execute
                  process_command(code_block.strip(), variables)
                  handle_print(code_block.strip())

        elif command.startswith("run"):
            run_drift = command[len("run "):]
            
            
            subprocess.run(["start", "cmd", "/k", "python", "D:\\.sps\\intepreter.py", {run_drift}], shell=True)
            

            

      
            
        
        elif command.startswith("sPrintvar(") and command.endswith(")"):
            var_name = command[len("sPrintvar("):-1]
            if var_name in variables:
                 print(f"{var_name} = {variables[var_name]}")
                

        elif command.startswith("sPrintvarT("):
              var_name = command[len("sPrintvarT("):-1]
              if var_name in variables:
                 
                 if var_value in digits:
                       var_type = "Number"
                       print(f"Type: {var_type}")
                 else:
                      print("Type: Else")

        elif command.startswith("openWeb("):
             site_name = command[len("openWeb("):-1]
             webbrowser.open(site_name)
             print(f"Opening {site_name}")
        
        elif command.startswith("newLabel"):
            params = command[len("newLabel('"):-2]
            params_list = params.split("', '")

            if len(params_list) == 4:
                window_name, label_text, font_name, font_size = params_list
                font_size = font_size.strip("'")  # Clean up the font_size string
                create_label(window_name, label_text, font_name, int(font_size))
            elif len(params_list) == 3:
                window_name, label_text, font_name = params_list
                create_label(window_name, label_text, font_name)
            elif len(params_list) == 2:
                window_name, label_text = params_list
                create_label(window_name, label_text)

        elif syntax.startswith("//"):
         commens = syntax[len("//"):]
         comments.append(commens)
        elif command.startswith("sPrintcmts"):
            cmts = command[len("sPrintcmts "):]
            
            if cmts.startswith("All"):
                comments[cmts] = cmts
                comments.append(cmts)
            
                print(f"All comments: {comments[cmts]}")
       
    if syntax.startswith("//"):
         commens = syntax[len("//"):]
         comments.append(commens)






                   
def procces_if(syntax):
    
    command = syntax[len("spark."):]
    if syntax.startswith("spark."):
        command = syntax[len("spark."):]
        if command.startswith("ifState("):
             condition = command[len("ifState("):command.index(")")]
             if condition in printer:
                 
                    then = syntax[len("then{"):then.index("}")]
        
                      # Store in dictionary
                    if syntax.startswith("then{"):
                        then = syntax[len("then{"):then.index("}")]
                        if '{' in then and '}' in then:
                                    start_index = syntax.index("{")
                                    end_index = syntax.index("}") + 1
                                    command_name = syntax[:start_index].strip()  # Command before '{'
                                    code_block = syntax[start_index + 1:end_index - 1].strip()  # Inside '{}'
                                    printer[command_name] = code_block
                                    process_command(code_block.strip(), variables)
                                    math_ughftl(code_block.strip())
                                    handle_print(code_block.strip())
                                    print("yo")



def evaluate_condition(condition, variables):
    # Simplified condition evaluation
    # For now, it supports only comparisons between variables and literals
    try:
        # Example: condition is "var1 == 5"
        left, operator, right = parse_condition(condition, variables)
        left_value = variables.get(left, left)
        right_value = variables.get(right, right)

        if operator == "==":
            return left_value == right_value
        elif operator == "!=":
            return left_value != right_value
        elif operator == "<":
            return left_value < right_value
        elif operator == ">":
            return left_value > right_value
        elif operator == "<=":
            return left_value <= right_value
        elif operator == ">=":
            return left_value >= right_value
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    except Exception as e:
        print(f"Error evaluating condition: {condition}")
        print(e)
        return False

def parse_condition(condition, variables):
    # Parse the condition into left, operator, and right components
    # This is a very basic parser
    for operator in ["==", "!=", "<=", ">=", "<", ">"]:
        if operator in condition:
            left, right = condition.split(operator)
            return left.strip(), operator, right.strip()
    raise ValueError(f"Invalid condition: {condition}")            
         
def ne_cls(syntax):
    


 if syntax.startswith("newFunc"):
    command = syntax[len("newFunc "):].strip()

    # Split command and code block
    if '{' in command and '}' in command:
        start_index = command.index("{")
        end_index = command.index("}") + 1
        command_name = command[:start_index].strip()  # Command before '{'
        code_block = command[start_index + 1:end_index - 1].strip()  # Inside '{}'
        
        clas_tydh[command_name] = code_block  # Store in dictionary
       
    else:
        print("No code block found")
    
      # Debugging

 elif syntax.startswith("call"):
    call = syntax[len("call "):].strip()
      # Debugging
    
    if call in clas_tydh:
        code_block = clas_tydh[call]  # Access the stored code block
          # Debugging
        
        # Execute the stored code block
        process_command(code_block.strip(), variables)
        math_ughftl(code_block.strip())
        handle_print(code_block.strip())
        
    else:
        print("Func not found in Func list")
              

             
def math_nore(syntax):
    command = syntax[len("spark."):]
    if command.startswith("mathnoReF."):
            
            # Handle the rest of the command
            addition_param = command[len("mathnoReF."):]
            
            if addition_param.startswith("addition("):
                adding = addition_param[len("addition("):-1]
                try:

                    a,b = adding.split("+")
                    
                   
                    result = a + b
                    print(f"Result of addition: {result}")
                except ValueError:
                    print(f"Invalid parameters for addition: '{adding}'")

            if addition_param.startswith("subtraction("):
                subbing = addition_param[len("subtraction("):-1]
                try:
                    a,b = subbing.split("-")
                    
                    
                    result = a - b
                    print(f"Result of addition: {result}")
                except ValueError:
                    print(f"Invalid parameters for addition: '{subbing}'")

            if addition_param.startswith("divide("):
                 diving = addition_param[len("divide("):-1]
                 try: 
                      
                      a,b = diving.split("/")
                     
                      result = a / b
                      print(f"The division result is {result}")
                 except ValueError:
                      print(f"Invalid parameters for division: '{diving}'")

            if addition_param.startswith("mul("):
                 muling = addition_param[len("mul("):-1]
                 try: 
                      
                      a,b = muling.split("*")
                      
                      result = a * b
                      print(f"The multiplication result is {result}")
                 except ValueError:
                      print(f"Invalid parameters for multiplication: '{muling}'")

            if addition_param.startswith("sqrt("):
                 sqrt = addition_param[len("sqrt("):-1]
                 try: 
                     
                     if len(sqrt) == 1:
                        variable_name_sqrt = sqrt[0].strip()
                        a = get_vale(variable_name_sqrt, variables)
                     lastresult = math.sqrt(a)
                     
                     
                     print(f"The sqrt result is {lastresult}")
                 except ValueError:
                      print(f"Invalid parameters for sqrt: '{sqrt}'")
                      


    
def math_ughftl(syntax):
     global last_result
     global result
     command = syntax[len("spark."):]
     if command.startswith("mathF."):
            
            # Handle the rest of the command
            addition_param = command[len("mathF."):]
            
            if addition_param.startswith("addition("):
                adding = addition_param[len("addition("):-1]
                try:

                    operand = adding.split("+")
                    a = get_value(operand[0].strip())
                    b = get_value(operand[1].strip())
                    result = a + b
                    print(f"Result of addition: {result}")
                except ValueError:
                    print(f"Invalid parameters for addition: '{adding}'")

            if addition_param.startswith("subtraction("):
                subbing = addition_param[len("subtraction("):-1]
                try:
                    operand = subbing.split("-")
                    a = get_value(operand[0].strip())
                    b = get_value(operand[1].strip())
                    result = a - b
                    print(f"Result of addition: {result}")
                except ValueError:
                    print(f"Invalid parameters for addition: '{subbing}'")

            if addition_param.startswith("divide("):
                 diving = addition_param[len("divide("):-1]
                 try: 
                      
                      operand = diving.split("/")
                      a = get_value(operand[0].strip())
                      b = get_value(operand[1].strip())
                      result = a / b
                      print(f"The division result is {result}")
                 except ValueError:
                      print(f"Invalid parameters for division: '{diving}'")

            if addition_param.startswith("mul("):
                 muling = addition_param[len("mul("):-1]
                 try: 
                      
                      operand = muling.split("*")
                      a = get_value(operand[0].strip())
                      b = get_value(operand[1].strip())
                      result = a * b
                      print(f"The multiplication result is {result}")
                 except ValueError:
                      print(f"Invalid parameters for multiplication: '{muling}'")

            if addition_param.startswith("sqrt("):
                 sqrt = addition_param[len("sqrt("):-1]
                 try: 
                     
                     if len(sqrt) == 1:
                        variable_name_sqrt = sqrt[0].strip()
                        a = get_vale(variable_name_sqrt, variables)
                     last_result = math.sqrt(a)
                     
                     variables[variable_name_sqrt] = last_result
                     print(f"The sqrt result is {last_result}")
                 except ValueError:
                      print(f"Invalid parameters for sqrt: '{sqrt}'")
                      if syntax.startswith("reassign.value.sqrt"):
                            variables[sqrt[0].strip()] = last_result

def get_vale(variable_name, variables):
    # Retrieve the value of a variable from the dictionary
    return variables.get(variable_name, 0)  # Default to 0 if variable not found

def reassign_value(syntax, variables):
    global last_result
    
    # Check if the syntax starts with 'reassign.value(' and ends with ')'
    if syntax.startswith("reassign.value."):
        # Extract the variable name inside the parentheses
        
        care = syntax[len("reassign.value."):]
        if care.startswith("sqrt(") and care.endswith(")"):

            variable_name_sqrt = care[len("sqrt("):-1].strip()
            if last_result is not None:
                # Reassign the last result to the variable
                variables[variable_name_sqrt] = last_result
                print(f"Reassigned variable '{variable_name_sqrt}' with last result {last_result}")
            else:
                print("Error: No result to reassign")
       

          
                 

                 
                      
                      
                 
                      

                


                           
            
    


            
def get_value(operand):
    
     if operand in variables:
          return  variables[operand]
     else:
          try:
               return float(operand) #attempt to return float
          except ValueError:
               raise KeyError(operand)
          
     
                    
          
            
   
    
    
def handle_math(syntax):
    if syntax.startswith("spark."):
            # Remove "spark." prefix
            comman = syntax[6:]
            
            if comman.startswith("wait(") and comman.endswith(")"):
                time_param = comman[5:-1].strip()  # Extract what's inside the parentheses
                try:
                    wait_time = float(time_param)  # Convert to float
                    time.sleep(wait_time)  # Pause for the specified time
                except ValueError:
                    print(f"Invalid time value: '{time_param}'")


def handle_print(syntax):
    
    
    if syntax.startswith("sPrint("):
        command = syntax[len("sPrint("):-1]
        if command.startswith("'") and command.endswith("'"):
            command = command[1:-1]
            print(command)
            printer.append(command)

        
        else:
            print("Syntax error: single quotes expected")


def open_op(syntax):
    try:
        if syntax.startswith("open"):
            # Extract the window name from the syntax
            window_name = syntax[len("open "):].strip()
            if window_name in windows:
                    windows[window_name].deiconify()  # Show the window if it's minimized or hidden
                    print(f"Opening window '{window_name}'")
                # Create or show the window
                    if window_name not in windows or not windows[window_name].winfo_exists():
                        create_window(window_name)
            
            
        
    except Exception as e:
        print(f"Error processing open command '{syntax}': {e}")

def create_window(syntax):
    #create a window
    global window
    try:
        if window_name not in windows or not windows[window_name].winfo_exists():
            window = tk.Toplevel() if windows else tk.Tk()
            window.title(window_name)
            windows[window_name] = window
            window.geometry("500x400")
            print(f"Window '{window_name}' created")  # Debugging
        else:
            print(f"Window '{window_name}' already exists")
        return windows[window_name]
    except Exception as e:
        print(f"Error creating window '{window_name}': {e}")

def create_label(window_name, label_text, font_name="Arial", font_size=12):
    if window_name in windows and windows[window_name].winfo_exists():
        print(f"Adding label to window '{window_name}'")  # Debugging
        label = tk.Label(windows[window_name], text=label_text, font=(font_name, font_size))
        label.pack(pady=20)
        print(f"Label '{label_text}' added to window '{window_name}' with font '{font_name}' and size '{font_size}'")  # Debugging
    else:
        print(f"Error: Window '{window_name}' not found or has been destroyed!")

def run_new(file_path):
  try:
        with open(file_path, "r") as file:
            content = file.readlines()
           
            for line in content:
                line = line.strip()
                handle_print(line)
                handle_math(line)
                process_command(line, variables)
                math_ughftl(line)
                ne_cls(line)
                procces_if(line)
                open_op(line)
                root.update()
                
                
                
               
                
                
  except Exception as e:
        print(f"An error occured: {e}")

def run_script(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.readlines()

            for line in content:
                line = line.strip()
                handle_print(line)
                handle_math(line)
                process_command(line, variables)
                math_ughftl(line)
                ne_cls(line)
                procces_if(line)
                open_op(line)
                root.update()
                math_nore(line)
                
                
               
                
                
    except Exception as e:
        print(f"An error occured: {e}")
        






     

root = tk.Tk()
root.withdraw()  # Hide the root window


file_path = input(".sps file path here: ")
run_script(file_path)
root.mainloop()
