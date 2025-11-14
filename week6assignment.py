library_data = [
        ('B101', 'Fantasy', 2001, 506),    # Annualized: 506 / 23 = 22.0
        ('B205', 'Sci-Fi', 1999, 600),     # Annualized: 600 / 25 = 24.0
        ('B102', 'Fantasy', 2015, 207),    # Annualized: 207 / 9 = 23.0
        ('B301', 'Mystery', 2020, 100),    # Annualized: 100 / 4 = 25.0
        ('B206', 'Sci-Fi', 2018, 144)      # Annualized: 144 / 6 = 24.0
    ]



def calculate_annualized_checkouts(book_tuple):
    book_id, genre, publication_year, total_checkouts = book_tuple
    current_year = 2024
    if publication_year == current_year:
        return total_checkouts
    years_passed = current_year - publication_year
    return total_checkouts / years_passed


def find_most_popular_book(library_data):
    highest_rate = -1
    best_book_id = None
    for book in library_data:
        avg = calculate_annualized_checkouts(book)
        book_id = book[0]
        if avg > highest_rate or (avg == highest_rate and book_id < best_book_id):
            highest_rate = avg
            best_book_id = book_id

    return best_book_id


def get_books_in_genre(library_data, genre_name):
    result = []
    for book in library_data:
        if book[1] == genre_name:
            result.append(book[0])
    result.sort()
    return result


def get_genre_circulation_summary(library_data):
    summary_list = []

    for book in library_data:
        genre = book[1]
        total = book[3]
        found = False
        for i in range(len(summary_list)):
            if summary_list[i][0] == genre:
                # update old total
                old_genre, old_total = summary_list[i]
                summary_list[i] = (old_genre, old_total + total)
                found = True
                break
        if not found:
            summary_list.append((genre, total))
    summary_list.sort()
    return summary_list


def analyze_library(library_data):
    most_popular = find_most_popular_book(library_data)
    fantasy_ids = get_books_in_genre(library_data, "Fantasy")
    genre_summary = get_genre_circulation_summary(library_data)
    return (most_popular, fantasy_ids, genre_summary)


print(analyze_library(library_data))
