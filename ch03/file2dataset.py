import numpy as np
import types

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

        #delete the space in txt file
        number_of_datasets = len(lines)
        lines_no_space = []
        for line in lines:
            lines_no_space.append(line.rstrip())

        # split_in_columns = input("By default, the dataset is splitted in rows. If you want to split it in columns, input 'column':")
        split_in_columns = 'row'
        # if split_in_columns == "column":
        #     #split in column
        #
        # else:
            # print("Input which column is the label. Input '-1' to define the last column as the label.")
            # number_of_label_column = input("Which column is the label: ")

        first_row, number_of_elements = deal_row(lines_no_space[0], ',')

        #create an empty numpy matrix to save the dataset
        return_mat = np.zeros((number_of_datasets, number_of_elements))
        return_list = []
        list_row_index = 0
        for line in lines_no_space:
            list_row, number_of_elements = deal_row(lines_no_space[list_row_index], ',')

            return_list.append(list_row)

            list_row_index += 1


        #end process
        input_finish = True
        print(return_list)
        return return_list


def deal_row(string, delimiter):
    """return the processed row of data and the number of features of each row"""
    number_of_element = 0
    list_of_row = []
    while len(string):
        delimiter_position = string.find(delimiter)
        if delimiter_position != -1:
            element_to_append = string[0:delimiter_position]
            print(type(element_to_append))
            print(element_to_append.isdigit())
            if element_to_append != '':
                if element_to_append.isdigit():
                    element_to_append = float(element_to_append)
                list_of_row.append(element_to_append)
                number_of_element += 1
                string = string[delimiter_position + 1:]
        else:
            if string != '':
                if string.isdigit():
                    string = float(string)
                element_to_append = string
                list_of_row.append(element_to_append)
                number_of_element += 1
                string = []

    return list_of_row,number_of_element


file2dataset("tree_dataset.txt")
# file2dataset()