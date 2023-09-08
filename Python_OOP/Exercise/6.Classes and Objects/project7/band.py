from project7.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = list()

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                if not album.published:
                    self.albums.remove(album)
                    return f"Album {album.name} has been removed."
                else:
                    return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        details = [f"Band {self.name}"]
        [details.append(f"{album.details()}") for album in self.albums]
        return "\n".join(details)
