import csv


def main ():
    I_Number_Index = 0
    Student_Name_Index = 1
    student_dict = read_dict("students.csv", I_Number_Index)
    I_number_input = input('Please input an I-Number: ')
    if I_number_input in student_dict:
        print(student_dict[I_number_input])
    else:
        print('No such student')

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_name_index = 1
    student_dict = {}
    with open (filename,'rt') as students_file:
        reader = csv.reader(students_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            student_dict[key] = row_list[student_name_index]
    return student_dict

if __name__ == "__main__":
    main()