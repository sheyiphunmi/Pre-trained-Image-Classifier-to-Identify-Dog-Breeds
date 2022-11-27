#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: SEYIFUNMI OWOEYE
# DATE CREATED: 11/11/2022                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# # TODO 2: Define get_pet_labels function below please be certain to replace None
# #       in the return statement with results_dic dictionary that you create 
# #       with this function
# # 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
 
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
    
    # Creates temporary label variable to hold pet label name extracted 
    low_filenames = []
    pet_label = []
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
    
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if not in_files[idx].startswith("."): #- if in_files[idx][0] != ".":
            
            
#             #print(idx)
            low_filenames.append(in_files[idx].lower()) #convert each filename into lower case then append to a list
            pet_name_list = low_filenames[idx].split("_") #Split every item in the lowercase filename by "_" 
            #
            # pet_list.append(" ".join([word for word in pet_name_list if word.isalpha()])) # - one liner

            #Loops to check if word in is only
            # alphabetic characters - if true append word
            # to pet_list separated by trailing space 
            word_list = []
            for word in pet_name_list:
                if word.isalpha(): 
                    word_list.append(word)
            pet_label.append(" ".join(word_list))  #Join all the element in the list "word_list" and then append them.
                    # Replace None with the results_dic dictionary that you created with this
                    # function
        

            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates 
            # duplicate files (filenames)
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label[idx]]
            else:
                print("** Warning: Duplicate files exist in directory:", 
                      in_files[idx])
                
                

# #             # Sets string to lower case letters
# #             # Splits lower case string by _ to break into words 
# #             pet_image = in_files[idx].lower().split("_")

# #             # Creates an empty label variable to hold pet label name extracted 
# #             pet_label = ""

# #             # Loops to check if word in pet name is only
# #             # alphabetic characters - if true append word
# #             # to pet_name separated by trailing space 
# #             for word in pet_image:
# #                 if word.isalpha():
# #                     pet_label += word + " "

# #             # Strip off starting/trailing whitespace characters 
# #             pet_label = pet_label.strip()

# #             # If filename doesn't already exist in dictionary add it and it's
# #             # pet label - otherwise print an error message because indicates 
# #             # duplicate files (filenames)
# #             if in_files[idx] not in results_dic:
# #                 results_dic[in_files[idx]] = [pet_label]

# #             else:
# #                 print("** Warning: Duplicate files exist in directory:", 
# #                       in_files[idx])

          
    print('\nPrinting all key-value pairs in dictionary results_dic:')
    for key in results_dic:
          print('\nfilename = ', key, '    pet label = ', results_dic[key][0])
            
    # count length in full dictionary
    number_of_items_full_dic = len(results_dic)
    print('\nResult dictionary has {} key-value pairs'.format(number_of_items_full_dic))
    
          
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic


    
    