from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages # това ни трябва, за да създадем албума
        self.photos = [[] for _ in range(pages)] # репрезентира албума

    @classmethod
    def from_photos_count(cls, photos_count: int): #получаваме класа, а не инстанцията
        return cls(ceil(photos_count / 4)) # вдигаме инстанция

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos): # за номер на страница и страница [] в албума
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        page_separator = "-" * 11 + "\n"
        result = page_separator
        for page in self.photos:
            result += " ".join("[]" for _ in page) + "\n"
            result += page_separator
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