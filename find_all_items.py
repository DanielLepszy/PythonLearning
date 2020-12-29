# Write a Python function to index all items in a list
# Input: list to search, value to search for
# Output: list of indices 
# Lists can contain other list

def search_index_in_list(list_to_search,value):
     
   index = [idx for idx,w in enumerate(list_to_search) if(w==value)]
   return index

def search_index(list_to_search,value):
    

    
    for idx,x in enumerate(list_to_search):
        if(isinstance(x,int)):
            if(x==value):
                print('[{0}]'.format(idx))
        if(isinstance(x,list)):
            print('[{0}]{1}'.format(idx,search_index_in_list(x,value)))
      

# # # # # # #

list_to_search = [[0,3],1,3,[0,3]]
value = 3
search_index(list_to_search,value)
