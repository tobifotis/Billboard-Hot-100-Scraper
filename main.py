import requests
from bs4 import BeautifulSoup

#input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD")

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-19/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

number_one_song = soup.find("h3").getText().strip()

raw_songs = soup.find_all("h3",
                          id="title-of-a-story",
                          class_="c-title a-no-trucate a-font-"
                                 "primary-bold-s u-letter-spacing-0021 "
                                 "lrv-u-font-size-18@tablet lrv-u-font-size-16 "
                                 "u-line-height-125 u-line-height-normal@mobile-max "
                                 "a-truncate-ellipsis u-max-width-330 "
                                 "u-max-width-230@tablet-only")

song_list = [number_one_song, ]
for each_song in raw_songs:
    song_title = each_song.getText().strip()
    song_list.append(song_title)
print(song_list)




