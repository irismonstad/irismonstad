# Cross-referencing actors on TV-shows
As a curious person and avid TV-watcher, I've often found myself wondering which actors have featured on multiple of my favourite shows. This is a program to do just that.

## The data
The data is fetched from [TMDB's](https://www.themoviedb.org) API. This is comparable to IMDB, however TMDB's API access is free and very well documented. The data is returned as .json-files with easily usable dictionaries. 

## The program
**In essence:**

The program first compares the dictionaries of data from both shows, and adds all actors featured in both into a separate dictionary -  along with the amount of episodes they are featured in.

The second part looks at the dictionary of actors featured in both shows, and adds only actors with multiple episodes on each show to a new dictionary. 

The dictionary of returning actors *(featured in multiple episodes)* is printed. 

## Further development
**Some areas that could be developed further going forward:**

- Reformatting the output to be easier to read
  - E.g. newline between actors
  - Sorting actors based on episode count
  - **Or:** creating a UI for the user to interact with the results (could have an option to turn on/off requirement of multiple episode features)
- Restructuring code to reduce nesting
  - The part of the program that compares the data is quite nested. Fixing this would make the code easier to read and edit/debug. 

# Run the program:
1. To run the program yourself you will need to install the python libraries imported at the start of the program. 
2. You will also need an API-key. This is as simple as creating an account on [TMDB](https://www.themoviedb.org) and [requesting one](https://developer.themoviedb.org/docs/faq#how-do-i-apply-for-an-api-key). Put this key in a .env file with the format `FILM_API_TOKEN = 'xxxxxx'`.
3. Set `id1` and `id2` to the IDs of the shows you'd like to compare. You can find these in the url of a show's page on [TMDB](https://www.themoviedb.org)*.
4. To remove the multiple episode requirement, simply change the last print statement to `print(data)`


*www.themoviedb.org/tv/**94605**-arcane (94605 is the ID)