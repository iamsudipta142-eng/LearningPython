daily_beneficiary_count = int(input("daily beneficiary count"))
if daily_beneficiary_count <20:
    print("Result : Low Turnout")
elif daily_beneficiary_count <=50:
    print("Result : Normal Turnout")
else: 
    print("Result : High Turnout")
