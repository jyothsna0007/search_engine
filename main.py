'''
a: [(s.txt, 3), (m.txt, 1)]
bb: [(s.txt, 3), (m.txt 2)]
ccc: [(s.txt, 2), (m.txt 2)]
d: [(s.xtx, 1), (m.txt 4)]
e:[(m.txt,1)]

index_map={
    'a':[('s.txt', 3), ('m.txt', 1)],
    'bb': [('s.txt', 3), ('m.txt', 2)],
    'ccc': [('s.txt', 2), ('m.txt' ,2)],
    'd': [('s.txt', 1), ('m.txt', 4)],
    'e':[('m.txt',1)]
}
qs=input()
sorted_pairs = sorted(index_map[qs], key=lambda x: -x[1])
print(sorted_pairs)
'''


'''
count the frequency of each string in the given string
input: if you fire the fire i will fire you i am the fire
output: if : 1
        you : 2
        fire : 4
        the : 2
        i :2
        will : 1
        am : 1
'''


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





folder_location = 'C:\\Users\\HP\\Documents\\from_dilip\\stories\\stories'
read_all_files(folder_location)



while True:
    user_input=input()
    if user_input in word_filecount:
        a=word_filecount[user_input]
        sorted_list = sorted(a, key=lambda x: x[1], reverse=True)
        top_five=sorted_list[:5]
        print(top_five)





















