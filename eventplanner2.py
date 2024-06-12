# Task 2: Catering Choices

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

veggie_food = input("Would you like to have vegetarian food? Yes/No")

if veggie_food == "Yes":
    print("We recommend Veggie Delight Caterers for your choice of food!!")
else:
    print("We recommend Gourmet Meals Caterers for your choice of food!!")