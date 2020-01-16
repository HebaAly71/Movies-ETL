# %%
# Import Dependencies
import json
import pandas as pd
import numpy as np

# %%
file_dir='/Users/hebamaly/Movies-ETL/' 
# %%
with open(f'{file_dir}/wikipedia.movies.json', mode='r') as file:
    wiki_movies_raw = json.load(file)

# %%
len(wiki_movies_raw)

# %%
# First 5 records
wiki_movies_raw[:5]

# %%
# Last 5 records
wiki_movies_raw[-5:]


# %%
# Some records in the middle
wiki_movies_raw[3600:3605]

# %%
#Transform kaggle files into dataframes
kaggle_metadata = pd.read_csv(f'{file_dir}movies_metadata.csv', low_memory=False)
ratings = pd.read_csv(f'{file_dir}ratings.csv')

# %%
kaggle_metadata.head()

# %%
ratings.head()

# %%
ratings.sample(n=5)

# %%
wiki_movies_df = pd.DataFrame(wiki_movies_raw)

# %%
wiki_movies_df.head()

# %%
wiki_movies_df.columns.tolist()

# %%
# filters movies that has directors and imdb links
wiki_movies = [movie for movie in wiki_movies_raw
               if ('Director' in movie or 'Directed by' in movie)
                   and 'imdb_link' in movie
                   and 'No. of episodes' not in movie]
len(wiki_movies)

# %%
wiki_movies_df_filt = pd.DataFrame(wiki_movies)

# %%
wiki_movies_df_filt.head()

# %%
wiki_movies_df_filt[wiki_movies_df_filt['Arabic'].notnull()]

# %%
def clean_movie(movie):
    movie = dict(movie) #create a non-destructive copy
    alt_titles={}
    for key in ['Also known as','Arabic','Cantonese','Chinese','French',
                'Hangul','Hebrew','Hepburn','Japanese','Literally',
                'Mandarin','McCune–Reischauer','Original title','Polish',
                'Revised Romanization','Romanized','Russian',
                'Simplified','Traditional','Yiddish']:
                if key in movie:
                    alt_titles[key] = movie[key]
                    movie.pop(key)
    if len(alt_titles) > 0:
        movie['alt_titles'] = alt_titles
    return movie

# %%
clean_movies = [clean_movie(movie) for movie in wiki_movies]


# %%
wiki_movies_df = pd.DataFrame(clean_movies)
sorted(wiki_movies_df.columns.tolist())

# %%
