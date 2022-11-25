"""
Input1
Peter-Java-84
George-C#-84
George-C#-70
Katy-C#-94
exam finished

Output1
Results:
Peter | 84
George | 84
Katy | 94
Submissions:
Java - 1
C# - 3

Input2
Peter-Java-91
George-C#-84
Katy-Java-90
Katy-C#-50
Katy-banned
exam finished

Output2
Results:
Peter | 91
George | 84
Submissions:
Java - 2
C# - 2

"""
def ban(dict: dict, name):
    for key in dict.keys():
        if name == key[0]:
            dict.pop(key)
            return True
    return False


def print_results(dict: dict):
    print('Results:')
    [print(f"{key[0]} | {points}") for key, points in dict.items()]


def print_submissions(dict: dict):
    print('Submissions:')
    [print(f"{lang} - {count}") for lang, count in dict.items()]


if __name__ == '__main__':
    students_data = {}
    language_data = {}

    while True:

        line = input().split('-')
        if line[0] == 'exam finished':
            break
        elif line[1] == 'banned':
            if ban(students_data, line[0]):
                ban(students_data, line[0])
        else:
            username = line[0]
            language = line[1]
            points = int(line[2])

            if (username, language) not in students_data:
                students_data[(username, language)] = points
            else:
                if students_data[(username, language)] < points:
                    students_data[(username, language)] = points

            if language not in language_data:
                language_data[language] = 0
            language_data[language] += 1

    print_results(students_data)
    print_submissions(language_data)