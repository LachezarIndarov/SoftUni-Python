from project7.song import Song


class Album:
    def __init__(self, name, *args: Song):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):
        if song not in self.songs and not song.single and not self.published:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        else:
            if song.single:
                return f"Cannot add {song.name}. It's a single"
            elif self.published:
                return "Cannot add songs. Album is published."
            else:
                return "Song is already in the album."

    def remove_song(self, song_name):
        if not self.published:
            for song in self.songs:
                if song.name == song_name:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
            return "Song is not in the album."
        else:
            return "Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        details = [f"Album {self.name}"]
        [details.append(f"== {song.get_info()}") for song in self.songs]
        return "\n".join(details)
