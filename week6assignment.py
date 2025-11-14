def calculate_annualized_checkouts(book_tuple):
    book_id, genre, publication_year, total_checkouts = book_tuple
    current_year = 2024
    if publication_year == current_year:
        return total_checkouts
    years_since_publication = current_year - publication_year
    return total_checkouts / years_since_publication


def find_most_popular_book(library_data):
    highest_rate = -1
    best_book_id = None

    for book in library_data:
        avg_checkouts = calculate_annualized_checkouts(book)
        book_id = book[0]

        if (avg_checkouts > highest_rate) or (avg_checkouts == highest_rate and book_id < best_book_id):
            highest_rate = avg_checkouts
            best_book_id = book_id

    return best_book_id

def get_books_in_genre(library_data, genre_name):
    result = [book[0] for book in library_data if book[1] == genre_name]
    return sorted(result)
def get_genre_circulation_summary(library_data):
    genre_totals = {}
    for book in library_data:
        genre = book[1]
        total = book[3]
        genre_totals[genre] = genre_totals.get(genre, 0) + total
    return sorted(genre_totals.items())
def analyze_library(library_data):
    most_popular_book = find_most_popular_book(library_data)
    fantasy_book_ids = get_books_in_genre(library_data, "Fantasy")
    genre_summary = get_genre_circulation_summary(library_data)
    return (most_popular_book, fantasy_book_ids, genre_summary)

library_data = [
    ('B101', 'Fantasy', 2001, 506),
    ('B205', 'Sci-Fi', 1999, 600),
    ('B102', 'Fantasy', 2015, 207),
    ('B301', 'Mystery', 2020, 100),
    ('B206', 'Sci-Fi', 2018, 144)
]

result = analyze_library(library_data)
print(result)
