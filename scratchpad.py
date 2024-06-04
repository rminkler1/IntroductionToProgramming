# # bug_counter = 0
# # days = 5
# #
# # for each_day in range(1, days + 1):
# #     bugs_collected_today = int(input(f'Enter the bugs collected on day {each_day}: '))
# #     bug_counter += bugs_collected_today
# #
# # print(f'Total bugs collected was {bug_counter}.')
# #
# # calories_per_minute = 4.2
# # for minutes in range(10, 31, 5):
# #     print(f'{minutes * calories_per_minute} calories burned in {minutes}.')
#
#
# budget = float(input("What is your budget for this month? "))
#
# expense_item = float(input('Enter an expense amount. Enter 0 to calculate your expenses: $'))
#
# total_expenses = 0
#
# while expense_item != 0:
#     total_expenses += expense_item
#     expense_item = float(input('Enter an expense amount. Enter 0 to calculate your expenses: $'))
#
# if total_expenses <= budget:
#     print(f'You spent ${total_expenses:,.2f} of your ${budget:,.2f} budget, '
#           f'leaving ${(budget - total_expenses):,.2f} left to spend.')
# else:
#     print(f'You spent ${total_expenses:,.2f} of your ${budget:,.2f} budget, '
#           f'leaving you over budget by ${abs(budget - total_expenses):,.2f}.')

# print('Your salary begins at $0.01 per day. Then doubles each day you work.')
# days = int(input('How many days are you ready to work? '))
# salary = 0.01
# for day in range(1, days + 1):
#     print(f'On day {day} your salary is ${salary:,.2f}')
#     salary *= 2
#
# range(3)

def main():
    while True:  # Forever loop
        wait_for_button_press()  # Wait for button press before starting
        user_text = transcribe_audio()
        paste_text(user_text)
        if keyboard.is_pressed('space'):  # Check if space bar was pressed during transcription
            print("Space bar pressed, stopping...")
            break  # Exit the loop
        else:
            print("No spacebar press detected. Continuing...")  # Optional
            

if __name__ == "__main__":
    main()
