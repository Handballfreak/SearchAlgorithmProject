import utils
import sorts

#import of lists
bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
# for book in bookshelf:
  # print(book["title"])


#comparisson function
def by_title_ascending(book_a, book_b):
  if book_a["title_lower"] > book_b["title_lower"]:
    return True
  else:
    return False


#comparisson function
def by_author_ascending(book_a, book_b):
  if book_a["author_lower"] > book_b["author_lower"]:
    return True
  else:
    return False


#comparisson function
def by_total_length(book_a, book_b):
  len_a = len(book_a["author"]) + len(book_a["title"])
  len_b = len(book_b["author"]) + len(book_b["title"])
  if len_a > len_b:
    return True
  else:
    return False


#testing algorithmen
ordered_v1_bookshelf = sorts.bubble_sort(bookshelf, by_title_ascending)
# for book in ordered_v1_bookshelf:
  # print(book["title"])

ordered_v2_bookshelf = sorts.bubble_sort(bookshelf, by_author_ascending)
# for book in ordered_v2_bookshelf:
  # print(book["author"])

ordered_v3_bookshelf = bookshelf[:]
sorts.quicksort(ordered_v3_bookshelf, 0, len(ordered_v3_bookshelf) - 1, by_author_ascending)
# for book in ordered_v3_bookshelf:
  # print(book["author"])

ordered_v4_bookshelf = sorts.bubble_sort(long_bookshelf, by_total_length)
# for book in ordered_v4_bookshelf:
  # print(book["author"] + " " + book["title"])

ordered_v5_bookshelf = long_bookshelf[:]
sorts.quicksort(ordered_v5_bookshelf, 0, len(ordered_v5_bookshelf) - 1, by_total_length)
for book in ordered_v5_bookshelf:
  print(book["author"] + " " + book["title"])
