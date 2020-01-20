# Movies-ETL
### Important files:
#### 1) challenge.py
#### 2) challenge.ipynb
#### 3) config.py

Please note that I couldn't upload the ratings.csv and kaggle_metadata.csv files since they were too large.  I tried the lfs but it didn't work either.  I asked the TA they told me its okay as long as I can upload the code.

### Assumptions:

1) We are assuming that data in some of the columns (i.e. budget, box office, running time, and release date) has a certain set of expressions, while we can actually get them in different forms if we get new data. By using our current function wse won't be able to capture all the new forms of data that might come with new data, especially if its making up a big percentage of the new data.
 
2) We are assuming that the alternate titles list is only a certain set of languages columns that we found in the wiki data file we got. However, if we got new data we might get columns of alternate langauge titles that were not defined in our list or vice versa we can might not have some of the columns that are defined in the list. In this second case we can create a try except block inside the clean_movie function created:
 
         > try:
    
            > for key in ['Also known as','Arabic','Cantonese','Chinese','French',
                'Hangul','Hebrew','Hepburn','Japanese','Literally',
                'Mandarin','McCune–Reischauer','Original title','Polish',
                'Revised Romanization','Romanized','Russian',
                'Simplified','Traditional','Yiddish']:
                if key in movie:
                    alt_titles[key] = movie[key]
                    movie.pop(key)
        
         > except NameError:
     
            > print("An error occured. One of the columns isn't found")
  
 3) When transforming and cleaning data after merging the kaggle data with wiki data, we did some exploratory analysis to decide which columns should we drop from wiki or kaggle data and which one should we keep from wiki or kaggle data. However, when if we get new data, this might not be the case in this case that will affect the validity of the data we will have in the new movie table created.
  
 4) One of the limitations of the function that it only accepts 2 csv files, and one json file.  So if one of the files that are used as an input file isn't in a csv format then the function is going to through an error and it won't work. In this case we can also create a try except block when calling the function:
 
         > try:
    
            > etl(wiki_movies_raw, kaggle_metadata_file,ratings_file)
        
         > except TypeError:
     
            > print("An error occured. One of the files is not a csv and can't read it")
            
 
 5) One of the limitation of the function that it can only take 3 arguments and not more than that, this means it can only extract, and transform 3 files.
 
         
 
 
  
