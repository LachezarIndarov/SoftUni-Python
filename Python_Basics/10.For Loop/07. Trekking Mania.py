"""
input1
10
10
5
1
100
12
26
17
37
40
78

output1
1.84%
6.75%
5.21%
31.60%
54.60%

input2
5
25
41
31
250
6

output2
0.00%
1.70%
7.08%
8.78%
82.44%

"""
#GitHub  - 100% Judge
numbers_of_groups = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
all_climbing_people = 0



for i in range(1,numbers_of_groups + 1):
    climbing_people = int(input())

    if climbing_people  <= 5:
        musala += climbing_people
    elif 6 <= climbing_people  <= 12:
        mont_blanc += climbing_people
    elif 13 <= climbing_people  <= 25:
        kilimanjaro += climbing_people
    elif 26 <= climbing_people  <= 40:
        k2 += climbing_people
    else:
        everest += climbing_people

all_climbing_people = musala + mont_blanc + kilimanjaro + k2 + everest



percentage_musala = musala / all_climbing_people * 100
percentage_mont_blanc = mont_blanc / all_climbing_people * 100
percentage_kilimanjaro = kilimanjaro / all_climbing_people * 100
percentage_k2 = k2 / all_climbing_people * 100
percentage_everest = everest / all_climbing_people * 100


print(f"{percentage_musala:.2f}%")
print(f"{percentage_mont_blanc:.2f}%")
print(f"{percentage_kilimanjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")



