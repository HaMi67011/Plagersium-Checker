from difflib import SequenceMatcher

#importing files
with open('pdf_file_ name' , errors='ignore') as file1 , open( 'pdf_file_name', errors='ignore') as file2:
    #reading file 1 and storing its data
    file_1_data = file1.read()
    #reading file 2 and storing its data
    file_2_data = file2.read()
    #using Libaray function to match the data 
    Similarity = SequenceMatcher(None,file_1_data,file_2_data)
    print(Similarity.ratio())