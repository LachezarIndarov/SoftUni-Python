"""
Input1
212
20
2

Output1
5

Input2
432
15
4

Output2
7

"""
#GitHub  - 100% Judge

count_pages = int(input())
pages = int(input())
days = int(input())

total_time_to_read_book = count_pages / pages
required_hours_per_day = total_time_to_read_book / days


print(round(required_hours_per_day))


