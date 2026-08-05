students = {
    101: {
        "name": "Aditya",
        "age": 21,
        "city": "Ahmedabad",
        "course": "BCA",
        "phone": "9876543210"
    },

    102: {
        "name": "Rahul",
        "age": 20,
        "city": "Surat",
        "course": "B.Tech",
        "phone": "9123456789"
    },

    103: {
        "name": "Priya",
        "age": 22,
        "city": "Vadodara",
        "course": "B.Com",
        "phone": "9988776655"
    }
}


def add_student(roll):
        name = input("Enter your new name: ")
        age = int(input("Enter your new age: "))
        city = input("Enter your city: ")
        course = input("Enter your course: ")
        phone = input("Enter your phone number: ")
        
        students[roll]  = {"name": name, "age": age, "city": city, "course": course, "phone": phone}
    
def search_student(roll):    
        print(students[roll])
        
def update_student(roll):
        field = input("Which field you want to update (name/age/city/course/phone): ")
        
        if field in students[roll]:
            new_value = input(f'Enter your new {field}: ')
            
            students[roll][field] = new_value
            print(f'Field updated successfully')
        else:
            print(f'The field {field} not found!!')
            
def delete_student(roll):
        del students[roll]
        print(f'Student delete successfully ')
        
        
while True:
    print("================== Student Management System ===================")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = int(input("Choice is yours: "))
    
    
    if choice == 1:
        roll = int(input("Enter your new roll number: "))
        if roll in students:
            print(f'Student already exists!!')
        else:
            add_student(roll)
            
    elif choice == 2:
        roll = int(input(f'Enter your roll number: '))
        if roll in students:
            search_student(roll)
        else:
            print(f'Invalid student not found!!')
    
    elif choice == 3:
        roll = int(input(f'Enter your roll number: '))
        if roll in students:
            update_student(roll)
        else:
            print(f'The Student not found!!')
    
    elif choice == 4:
        roll = int(input(f'Enter your roll number to delete: '))
        if roll in students:
            delete_student(roll)
            print(students)
        else:
            print(f'The roll number not found')
            
    elif choice == 5:
        print("Thank You for visiting !!")
        print(f'Goodbye')
        
        break
    else:
        print(f'Please Enter a valid Menu')
            