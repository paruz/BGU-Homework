try:
    with open('input.txt', 'r', encoding="utf-8") as f1:
        course_check = input('Название курса: ')
        student_output = []
        for line in f1.readlines():
            students = line.split(':')
            courses = students[1].strip('\n, ').split(', ')
            if course_check in courses:
                student_output.append(students[0].strip(' '))
        print(student_output)
except FileNotFoundError:
    print('Файл input.txt не найден')