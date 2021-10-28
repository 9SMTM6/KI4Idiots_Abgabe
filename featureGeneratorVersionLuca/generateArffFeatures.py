#functions to generate a feature
import feature_functions as ff

#array with posts
posts=["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.","Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."]


#array of features to generate
#format: (<name of feature>,<arff type of feature>,<function to generate feature>,<parameter for function, "" if not needed>)
feature_arr=[
("total_word_count", "numeric", ff.countWords,"")
]

#array with all words to count
word_count_features=["Lorem","dolor","ipsum"]
#quickly add all word count features
for word in word_count_features:
    feature_arr.append((f"occ_{word}","numeric",ff.countSpecificWord,word))

#open file for writing
with open('newarff.arff', 'w') as f:   
    f.write("@relation 'whatisthisfor'\n") 

    #declare attributes
    for (name,arff_type,feature_func,search_param) in feature_arr:
        f.write(f"@attribute {name} {arff_type} \n")

    #start data
    f.write("@data \n") 
    
    #generate features for each post
    for post in posts:
        is_first_in_row=True

        #iterate over every feature
        for (name,arff_type,feature_func,search_param) in feature_arr:
            #no semicolon when first in row
            if is_first_in_row:
                is_first_in_row=False
            else:
                f.write(";")
            
            #write feature
            f.write(f"{feature_func(post,search_param)}")
        
        #new line
        f.write("\n")
        
