# Movies-ETL
#### Important files:
##### 1) challenge.py
##### 2) challenge.ipynb

##### Assumptions:

1) We are assuming that data in some of the columns (i.e. budget, box office, running time, and release date) has a certain set of expressions, while we can actually get them in different forms if we get new data. We can solve this by adding a try and except block.  For example for budget data:

         > try:
    
            > wiki_movies_df['budget'] = budget.str.extract(f'({form_one_bud}|{form_two_bud})', flags=re.IGNORECASE)  [0].apply(parse_dollars)
        
         > except:
     
            > print("An error occured. The regular expression in not defined")
 
 The output should be the error message if we got a different form of budget data that the ones already defined, and this will be the same for all other columns that go with the same logic. If we get this error then we will know that there is new data format that is different that the regular expressions already defined. Please note: In this case we should, remove the last case in the parse_dollar function so we can get the exception message.
 
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
  
  3) 
