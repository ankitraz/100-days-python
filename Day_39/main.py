if __name__ == "__main__":
    def add_employee():
        '''
        it gets the data of employee from user and writes it to file.
        '''
        with open(
            "D:\\my_workspace\\100_days_python\\Day_39\\data.txt", "a", encoding="utf-8") as student_data:
            emp_id = input("Enter a unique id for employee: ")
            emp_design = input("Enter the designation of employee: ")
            emp_name = input("Enter the name of employee: ")
            emp_salary = input("Enter salary of employee: ")

            emp_details = [f"{emp_id},{emp_design},{emp_name},{emp_salary}"]
            # print(emp_details[0])
            # class1 = ["21,a,Ankit, 44444"]
            student_data.writelines(f"{emp_details[0]}\n")


    def get_emp_with_id():
        """
        Reads employee data from a text file and prompts the user to enter an employee ID to retrieve data for.
        """
        user_input = int(input("Enter the id of the employee you want to fetch details: "))
        print("-----------------------")
        with open("D:\\my_workspace\\100_days_python\\Day_39\\data.txt", "r", encoding="utf-8") as student_data:
            for line in student_data:
                fields = line.strip().split(",")
                emp_id = fields[0]
                design = fields[1]
                name = fields[2]
                salary = fields[3]

                if user_input == int(emp_id):
                    print(f"id: {emp_id}")
                    print(f"Designation: {design}")
                    print(f"Name: {name}")
                    print(f"Salary: {salary}")
                    print("-----------------------")
                    return  # exits the function after finding the employee with the given ID
            # The for loop completes without finding the employee with the given ID
            print("User not found!")

    while True:
        print("====================================")
        user_input = int(input('''Enter a choice:
1. Add an Employee
2. Show an employee data
3. Exit
    '''))
        print("====================================")
        match user_input:
            case 1:
                add_employee()
                usr_input = input("Do you want to continue? y or n\t")
                if usr_input == "n":
                    print("Thanks for visiting!")
                    break
            case 2:
                get_emp_with_id()
                usr_input = input("Do you want to continue? y or n\t")
                if usr_input == "n":
                    print("Thanks for visiting!")
                    break
            case _:
                print("Thanks for visiting!")
                break
