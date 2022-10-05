amount_of_needed_experience = float(input())
count_battles = int(input())

experience = 0

for i in range(1, count_battles+1):
    experience_earned_per_battle = float(input())
    if i % 3 == 0:
        experience += experience_earned_per_battle + (experience_earned_per_battle * 0.15)
    elif i % 5 == 0:
        experience += experience_earned_per_battle - (experience_earned_per_battle * 0.10)
    elif i % 15 == 0:
        experience += experience_earned_per_battle + (experience_earned_per_battle * 0.05)
    else:
        experience += experience_earned_per_battle
    if experience >= amount_of_needed_experience:
        battles_number = i
        break
if experience >= amount_of_needed_experience:
    print(f"Player successfully collected his needed experience for {battles_number} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(amount_of_needed_experience-experience):.2f} more needed.")






