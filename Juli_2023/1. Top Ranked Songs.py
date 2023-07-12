1. Top Ranked Songs (Judul Ganti Nanti)

Find songs that have ranked in the top position. 
Output the track name and the number of times it ranked at the top. Sort your records by the number of times the song was in the top position in descending order.

# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

df = spotify_worldwide_daily_song_ranking.copy()

rank_1 = df[df['position'] == 1]

grup = rank_1.groupby(['trackname']).size().reset_index(name = 'times_top1')

sorting = grup.sort_values('times_top1', ascending = False)

Penjelasan Nanti : 
