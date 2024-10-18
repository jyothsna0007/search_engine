import os
word_filecount={}

def read_all_files(folder_path):
    try:
        # List all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                print(f"Reading file: {file_name}")
                print(file_path)

                # Open and read each file
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        count_freq(content,file_name)# You can process the content as needed
                except Exception as e:
                    print(f"Error reading {file_name}: {e}")

    except Exception as e:
        print(f"Error accessing folder: {e}")


def count_freq(input_string,file_name):
    word_count={}
    words = input_string.split(" ")
    for i in words:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
    for word, count in word_count.items():
        if word in word_filecount:
            word_filecount[word].append((file_name,count))
        else:
            word_filecount[word]=[(file_name,count)]

        #print(f"{word}:{count}")


folder_location = 'C:\\Users\\HP\\Documents\\from_dilip\\stories\\stories'
read_all_files(folder_location)
while True:
    user_input=input()

    print(word_filecount[user_input])
