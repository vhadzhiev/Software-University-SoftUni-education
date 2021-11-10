from math import ceil


class PhotoAlbum:
    _max_photos_per_page = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__create_photo_matrix()

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / cls._max_photos_per_page)
        return cls(pages)

    def __create_photo_matrix(self):
        photo_matrix = []
        for page in range(self.pages):
            photo_matrix.append([])
        return photo_matrix

    def add_photo(self, label):
        for row_index in range(len(self.photos)):
            row = self.photos[row_index]
            if len(row) < 4:
                self.photos[row_index].append(label)
                return f"{label} photo added successfully on page {row_index + 1} slot {len(self.photos[row_index])}"
        return "No more free slots"

    def display(self):
        separator = 11 * '-'
        result = separator + '\n'
        for row in self.photos:
            result += ' '.join(['[]' for x in row]) + '\n'
            result += separator + '\n'

        return result.strip()

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

