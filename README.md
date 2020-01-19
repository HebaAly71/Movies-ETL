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
 
 The output should be the error message if we got a different form of budget data that the ones already defined, and this will be the same for all other columns that go with the same logic.
