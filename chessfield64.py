from datetime import timedelta
import pyinputplus as pyip
import sys


'''
POTENTIAL TODO:

------------------
OPTIONAL TODO: IF I WANT TO ADD MORE SCENARIOS/SIMULATIONS

- C) rice chess; for loop mit print (1 grain of rice bzw 1/625000 kg of 
rice (a small bag)...)

- (1 Person -> 1 person per square meter in square km)
- (option 2: 1 Haar breit; ~0,1 mm; 0.001% eines Durchschnitts-Kopfes)
- (option 5: 1 DIN A 4 blatt Fläche)
- (option 6: 1 DIN A 4 blatt Dicke)

- (((option 8: 1 rain drop (c. 0.1 lubik cm))))
- (((option 4: 1 Cent (0.01 €) (Challenge I have not solved yet:
comma every 3rd digit AND 2 digits after point) )))

for the 7 variables above I will probably need 1 dictionary for each 
variable and every dictionary will have roughly 1 ~field for each
scenario

---------------
'''


# welcome text
print(
    "You probably heard of the story about the chessboard and the",
    "grain of rice.\n",
    "Duplicate 1 grain of rice 64 times and you get an unimaginable large",
    "amount of rice.\n",
    "This program enables you to simulate 2 different simulations of such",
    "64-times-duplications.\n"
    "And the final number will be put into perspective by comparing it to",
    "other entities that can be grasped more easily.")


while True:

    # User can choose between different procedures
    print(
        "You can chooose one of the following scenarios of what is being",
        "duplicated:\n",
        "A) 1 playing dice on the ground (equals roughly 1 square cm of", 
        "space)\n",
        "B) 1 second of time")

    chosen_simulation = pyip.inputMenu(
        ['A', 'B'], lettered=False, numbered=False)

    # variables that are needed for all scenarios
    chessfield_no = 0

    # variables that are needed for the scenario with dice
    square_cm_in_square_m = 1 / 10000
    square_cm_in_square_km = square_cm_in_square_m / 1000000
    #sun_surface_square_km = 6090000000000
    earth_surface_square_km = 510072000

    # variables that are needed for the scenario with seconds
    '''
    The following variables are used for calculating the amount of time 
    which will be displayed for the user in the seconds-scenario. 
    Microseconds are used and later recalculated in seconds because with 
    seconds or milli seconds the timedelta function results in an 
    OverflowError (e.g. "OverflowError: days=1628906115; must have 
    magnitude <= 999999999").
    '''
    time_period_1_microsecond = timedelta(seconds=0.000001)
    time_period_1_year = timedelta(days=365)

    print(
        "-----------------------------------------------------",
        "--------------")

    while chessfield_no < 64:
        chessfield_no += 1

        # variables that are important vor all scenarios
        amount_on_current_chessfield = pow(2, chessfield_no - 1)

        amount_on_chessboard = pow(2, chessfield_no) - 1

        # variables that are important for dice scenario
        square_km_playing_dice_on_chessboard = amount_on_chessboard * \
            square_cm_in_square_km

        # variables for the scenario with seconds
        time_in_microseconds_on_chessboard = amount_on_chessboard * \
            time_period_1_microsecond

        time_in_years_on_chessboard = time_in_microseconds_on_chessboard / \
            time_period_1_year * 1000000

        # This output is displayed independent from the chosen scenario
        print("Chessfield number:", chessfield_no)
        print("Amount on current chessfield:",
              f"{amount_on_current_chessfield:,}")
        print("Amount on chessboard:", f"{amount_on_chessboard:,}")

        print(
            "-----------------------------------------------------",
            "--------------")

        # TODO above: display "amount of dice/seconds" instead of simply amount

    # The following output depends on the chosen simulation by the user
    if chosen_simulation == 'A':
        print(
            "---Area of playing dice (of the dice on all chessboard",
            "fields combined) in square km:",
            f"{square_km_playing_dice_on_chessboard:,}",
            "---")

        print(
            "---This equals",
            round(
                (square_km_playing_dice_on_chessboard / \
                earth_surface_square_km),
                2),
            "times the earth's surface area (510,072,000 km²).---")

    if chosen_simulation == 'B':
        print(
            "---Time of each single second on the chessboard field",
            "combined in years:",
            f"{time_in_years_on_chessboard:,}",
            "---")

        print(
            "---This equals",
            round(
                (time_in_years_on_chessboard / 4500000000),
                2),
            "times the age of the earth (roughly 4.5 billion years) or",
            round(
                (time_in_years_on_chessboard / 13800000000),
                2),
            "times the age of the universe (roughly 13.8 billion years).---")

    # TODO above: round the "...times" numbers because 2 digits after 
    # point are enough

    '''OPTIONAL TODO above: If I make more than the currently 2 
    scenarios it migh make sense to use several dictionaries, and then
    - instead of "Area" use variable "comparison_dimension" which is 
    then area/time/whatever
    - instead of "playing dice" use variable "entity_name" which is then 
    playing dice/ seconds/ whatever
    - instead of "square km" use varialbe "comparison_unit" which ist 
    then square km/ years/wahtever
    '''

    # TODO above: the "this equals...." number still has to be rounded

    """TODO_Get rid of the following  break-statement as soon as the 
    Game is finished. If I get rid of it before the game will often have 
    issues because of an eternal loop  which might raise the 
    exit-condition at some point or not """

    # break
    # User can make another calculation or quit the program
    print("Do you want to make another calculation or quit the program?")

    proceed_how = pyip.inputMenu(
        ['AGAIN', 'QUIT'], lettered=True, numbered=False)
    print(proceed_how)

    if proceed_how == 'AGAIN':
        continue

    if proceed_how == 'QUIT':
        print("Thanks for using the program!")
        sys.exit()
