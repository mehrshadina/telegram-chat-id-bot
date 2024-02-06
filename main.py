from Packages.Connection import get_updates ,get_last_update_id
from Packages.Database import check_database_file, create_database_and_tables
from Packages.Decision import decision_making
#from Packages. import *
#from Packages. import *
#from Packages. import *
#from Packages. import *
#from Packages. import *
#from Packages. import *

def main():
    last_update_id = None

    if check_database_file() == False:
        create_database_and_tables()

    while True:
        getUpdates = get_updates(last_update_id)

        for update in getUpdates["result"]:
            decision_making(update)
            last_update_id = get_last_update_id(update) + 1

if __name__ == '__main__':
    print("You are now connected to telegram bot!")
    print("And you can stop bot with: ((ctrl+c))")
    print("Good luck!")
    main()
