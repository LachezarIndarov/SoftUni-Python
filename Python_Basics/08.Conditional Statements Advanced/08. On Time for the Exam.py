"""
input1
9
30
9
50

output1
Late
20 minutes after the start

input2
9
00
8
30

output2
On time
30 minutes before the start

input3
16
00
15
00

output3
Early
1:00 hours before the start


input4
9
00
10
30

output4
Late
1:30 hours after the start

input5
14
00
13
55

output5
On time
5 minutes before the start

input6
11
30
8
12

output6
Early
3:18 hours before the start

input7
10
00
10
00

output7
On time

input8
11
30
10
55

output8
Early
35 minutes before the start

input9
11
30
12
29

output9
Late
59 minutes after the start

"""
#!!!! #GitHub  - 100% Judge
exam_time = int(input())
exam_minutes = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())



exam_time_to_minutes = (exam_time * 60) + exam_minutes
time_arrive_to_minutes = (hour_arrive * 60) + minutes_arrive

if time_arrive_to_minutes > exam_time_to_minutes:

    delay = time_arrive_to_minutes - exam_time_to_minutes

    if delay < 60:
        print(f"Late")
        print(f"{delay} minutes after the start")
    else:
        hh = delay // 60
        mm = delay % 60
        if mm < 10:
            print(f"Late")
            print(f"{hh}:0{mm} hours after the start")
        else:
            print("Late")
            print(f"{hh}:{mm} hours after the start")
elif exam_time_to_minutes >= time_arrive_to_minutes:

    early = exam_time_to_minutes - time_arrive_to_minutes

    if early == 0:
        print("On Time")
    elif 0 < early <= 30:
        print("On Time")
        print(f"{early} minutes before the start")
    elif early > 30 and early < 60:
        print("Early")
        print(f"{early} minutes before the start")
    elif early >= 60:
        hh = early // 60
        mm = early % 60

        if mm < 10:
            print(f"Early")
            print(f"{hh}:0{mm} hours before the start")
        else:
            print(f"Early")
            print(f"{hh}:{mm} hours before the start")






