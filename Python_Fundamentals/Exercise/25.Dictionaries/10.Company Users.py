"""
Input 1

SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End

Output1
SoftUni
-- AA12345
-- BB12345
Microsoft
-- CC12345
HP
-- BB12345


Input 2

SoftUni -> AA12345
SoftUni -> CC12344
Lenovo -> XX23456
SoftUni -> AA12345
Movement -> DD11111
End

Output2
SoftUni
-- AA12345
-- CC12344
Lenovo
-- XX23456
Movement
-- DD11111

"""
text = input().split(" -> ")
company = dict()

while text[0] != "End":

    company_name = text[0]
    id = text[1]
    if company_name not in company.keys():
        company[company_name] = list()
    if id not in company[company_name]:
        company[company_name].append(id)

    text = input().split(" -> ")

for (key, value) in company.items():
    print(f"{key}")
    for names in (value):
        print(f"-- {names}")







