# Terminal Library Tracker

A command-line application for tracking your reading progress, managing a wishlist, and rating books and manga series.

## Features

- **Add Series**: Track book or manga series by title and total volumes
- **Wishlist Management**: Add titles to a wishlist without needing volume counts upfront
- **Progress Tracking**: Update how many volumes you've read in each series
- **Auto Status Updates**: Automatically marks series as "reading" or "completed" based on progress
- **Rating System**: Rate books on a scale of 1-10
- **View Library**: Display a clean summary of all your books and wishlist items

## How to Use

### Running the Application

```bash
python "terminal library tracker.py"
```

### Menu Options

1. **Add a New Series**
   - Enter the series title and total number of volumes/chapters
   - Creates a new entry with status "plan to read"

2. **Add to Wishlist**
   - Enter a book title to add to your wishlist
   - No need to specify volume count (marked as "unknown")

3. **Update Progress**
   - Enter the series title and number of volumes read
   - Status automatically updates to "reading" (if volumes > 0) or "completed" (if all volumes read)

4. **Rate a Book**
   - Enter the book title and your rating (1-10)
   - Rating is saved and displayed in your library

5. **View Library & Wishlist**
   - Displays all entries with their details:
     - Progress (volumes read / total volumes)
     - Status (plan to read, reading, completed, wishlist)
     - Rating (1-10 or "not rated")

6. **Exit**
   - Close the application

## Example Workflow

```
Welcome to the Terminal Library Tracker!

Menu Options:
1. Add a New Series
2. Add to Wishlist
3. Update Progress
4. Rate a Book (Out of 10)
5. View Library & Wishlist
6. Exit

Choose an option (1-6): 1
Enter the series title: Attack on Titan
Enter total number of volumes/chapters: 34
Success: Added 'Attack on Titan' to your library!

Choose an option (1-6): 3
Enter the series title to update: Attack on Titan
Enter total volumes/chapters read so far: 15
Success: updated progress for 'Attack on Titan'.

Choose an option (1-6): 4
Enter the book title you want to rate: Attack on Titan
Enter your rating (1-10): 9
Success: you rated 'Attack on Titan' a 9/10!

Choose an option (1-6): 5
--- My Reading Log ---
Title: Attack on Titan
Progress: 15/34 Volumes
Status: reading
Rating: 9/10
--------------------
```

## Data Storage

Currently, the application stores all data in memory. This means your library will be cleared when you exit the application. Consider enhancing the project by:
- Saving data to a JSON or CSV file
- Loading saved data on startup
- Implementing persistent storage

## Requirements

- Python 3.x

## Project Structure

- `terminal library tracker.py` - Main application file containing all functions and the menu loop

## Functions

| Function | Description |
|----------|-------------|
| `add_series(title, total_volumes)` | Creates a new book entry with specified volume count |
| `add_to_wishlist(title)` | Adds a book to wishlist with unknown volume count |
| `update_progress(title, volumes_read)` | Updates reading progress and auto-updates status |
| `rate_book(title, score)` | Adds a 1-10 rating to a book |
| `view_library()` | Displays all books and wishlist items |
| `main()` | Main control flow with menu loop |

## Future Enhancements

- Persistent storage (JSON/CSV)
- Search functionality
- Filter by status or rating
- Delete entries
- Update total volumes
- Export library as PDF or text file
- Statistics (total series, completion rate, average rating)

## License

This project is open source and available under the MIT License.

## Author

Created by Pallavi190707
