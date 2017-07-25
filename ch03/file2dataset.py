import numpy as np

def file2dataset(filename = ''):
    """invert the txt file into a certain type of python dataset"""

    #initialize the status
    input_finish = False
    print("Anytime, input q to quit!")

    #main loop
    while input_finish == False:
        #determine the input file name
        if filename:
            print("The file to input is " + filename);
        else:
            filename = input("Input the filename: ")
            if (filename == 'q'):
                print("Process interrupt!")
                break

        #read file
        with open(filename) as file_object:
            lines = file_object.readlines()
            print(lines)

        #end process
        input_finish = True



file2dataset("tree_dataset.txt")
# file2dataset()