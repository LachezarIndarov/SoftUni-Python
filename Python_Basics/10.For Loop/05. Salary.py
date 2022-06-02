"""
input1
10
750
Facebook
Dev.bg
Instagram
Facebook
Reddit
Facebook
Facebook

output1
You have lost your salary.

input2
3
500
Github.com
Stackoverflow.com
softuni.bg

output2
500

"""
#GitHub  - 100% Judge

number_of_open_tabs = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50


for tab in range(0,number_of_open_tabs):
    site = str(input())

    if site == 'Facebook':
        salary -= facebook
    elif site == 'Instagram':
        salary -= instagram
    elif site == 'Reddit':
        salary -= reddit

    if salary <= 0:
        print(f'You have lost your salary.')
        break
if salary > 0:
    print(f'{salary}')




