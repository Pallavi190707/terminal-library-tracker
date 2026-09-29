
library={}
def add_series(title,total_volumes):
    "creates a new book entry"
    library[title]={"total_volumes":total_volumes,"volumes_read":0,"status":"plan to read","rating":"not rated"}
    print(f"\nSuccess:Added '{title}' to your library!")

    
def add_to_wishlist(title):
    "adds a book to read in the future without needing volume counts."
    library[title]={"total_volumes":"unknown","volumes_read":0,"status":"wishlist","rating":"not rated"}
    print(f"\nSuccess:Added '{title}' to your wishlist!")


def update_progress(title,volumes_read):
    "update how far along you are in the series"
    if title in library:
        library[title]["volumes_read"]=volumes_read
        if library[title]["total_volumes"]!="unknown"and volumes_read>=int(library[title]["total_volumes"]):
            library[title]["status"]="completed"
        elif volumes_read>0:
              library[title]["status"]="reading"
        print(f"\nSuccess:updated progress  for '{title}' .")
    else:
        print(f"\nError: series not found in your library.")


def rate_book(title,score):
    "adds a rating out to a specfic book."
    if title in library:
        if 1<= score <=10:
            library[title]["rating"]=f"{score}/10"
            print(f"\nSuccess:you rated'{title}' a {score}/10!")
        else:
            print(f"\nError: please enter a rating between 1 and 10.")
    else:
                print("\nError: Series not found in your library.")



def view_library():
    """Prints a clean summary of all saved books and wishlist items."""
    print("\n--- My Reading Log ---")
    for title, details in library.items():
        print(f"Title: {title}")
        print(f"Progress: {details['volumes_read']}/{details['total_volumes']} Volumes")
        print(f"Status: {details['status']}")
        print(f"Rating: {details['rating']}")
        print("-" * 20)


def main():
    """The main control flow of the application."""
    print("Welcome to the Terminal Library Tracker!")
    
    while True:
        print("\nMenu Options:")
        print("1. Add a New Series")
        print("2. Add to Wishlist")
        print("3. Update Progress")
        print("4. Rate a Book (Out of 10)")
        print("5. View Library & Wishlist")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            title = input("Enter the series title: ")
            vols = int(input("Enter total number of volumes/chapters: "))
            add_series(title, vols)
            
        elif choice == '2':
            title = input("Enter the wishlist book title: ")
            add_to_wishlist(title)
            
        elif choice == '3':
            title = input("Enter the series title to update: ")
            vols = int(input("Enter total volumes/chapters read so far: "))
            update_progress(title, vols)
            
        elif choice == '4':
            title = input("Enter the book title you want to rate: ")
            score = int(input("Enter your rating (1-10): "))
            rate_book(title, score)
            
        elif choice == '5':
            view_library()
            
        elif choice == '6':
            print("Closing the library. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please type a number from 1 to 6.")

main()
















            
            
    

            
        
       












