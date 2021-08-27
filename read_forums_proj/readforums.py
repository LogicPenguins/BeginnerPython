#! python3
# readforums.py - Downloads all the threads and their first 20 messages on the first page of the Minecraft Java Discussion Forum

import requests, os, bs4, time
from pathlib import Path

# Initializes URL for website
url = 'https://www.minecraftforum.net/forums/minecraft-java-edition/discussion'

# Creates directory to store threads in Minecraft Java Discussion Forum (may have to update Path for personal needs)
os.makedirs(f'{Path.home()}\\small-projects-python\\read_forums_proj\\forums_thread_data', exist_ok=True)

print(f'Reading {url}...')
all_threads = requests.get(url)
all_threads.raise_for_status()
soup1 = bs4.BeautifulSoup(all_threads.text, 'html.parser')

# Finds the <a> elements with the class="title". They will contain all the title names.
thread_titles = soup1.find_all("a", {"class": "title"})
print(thread_titles)
time.sleep(1000)
thread_num = 1
# This iterates through each title in the list of titles found in thread_titles ([1:] is supplied since first title isn't a thread)
for thread in thread_titles[1:]:
    title = ''
    # These characters don't register as valid chars in file names, hence they are required to be altered
    for chr in thread.getText():
        if chr == '\n':
            pass
        elif chr == "?":
            title += "(question-mark)"
        elif chr == "\"":
            title += "(backwards-slash)"
        elif chr == "/":
            title += '.'
        elif chr == ":":
            title += ';'
        elif chr == "*":
            title += "(star)"
        elif chr == '<':
            title += "(point-left)"
        elif chr == ">":
            title += "(point-right)"
        elif chr == "|":
            title += "(Vert-Line)"
        else:
            title += chr
    
    # A file is opened for each thread, distinguished by their #, which updates on each new thread by adding 1 to thread_num
    thread_file = open(f"{Path.home()}\\VSCPythonProjects\\read_forums_proj\\forums_thread_data\\Thread {thread_num}.txt", 'a')
    thread_file.write(f'Thread Title: {title}')

    # Gets the href in thread and makes a link to later open to each thread on the first page of the forum
    thread_link = f"https://www.minecraftforum.net/{thread.get('href')}"
    print(f'Downloading {thread_link}...')

    # Downloads all the source code for the link above and stores in thread_contents
    thread_contents = requests.get(thread_link)
    thread_contents.raise_for_status()

    # Parses through source code with beautiful soup and finds every content body (the actual messages/replies of the thread)
    soup2 = bs4.BeautifulSoup(thread_contents.text, 'html.parser')
    thread_comments = soup2.find_all("div", {"class": "j-comment-body-container p-comment-body forum-post-body-content"})

    # Finds all the authors of each individual reply/post to thread.(Not at direct author HTML code, but near it)
    thread_comments_authors = soup2.find_all("span" ,{"class": "u-dropDown p-comment-username j-comment-username"})

    # Creates an empty list to later be appended to later by each thread reply's author. Pattern is found in each item in the 
    # special bs4 soup list called thread_comments_authors
    authors_lst = []
    for thread_comment_author in thread_comments_authors:
        thread_comments_authors_filtered = thread_comment_author.find_all(("span", {"class" : "user user-role-registered-member"}))
        authors_lst.append(thread_comments_authors_filtered[0].get_text())


    # The text of each content body is filtered from the raw source code
    # Each reply is individually written to corresponding thread.txt file along with it's author
    for index, comment in enumerate(thread_comments):
        thread_file.write(f'\nReply By: {authors_lst[index]}\n')
        thread_file.write(f'Post: {comment.get_text()}')
        thread_file.write('-.-.-.-.-.-.-.-.-.-.-.-.-.\n')
    
    thread_num += 1
    thread_file.close()


# Gets a list of all the thread text files which are stored in the forums_thread_data folder
directs = os.listdir(f"{Path.home()}\\VSCPythonProjects\\read_forums_proj\\forums_thread_data")
directs_modified = sorted(directs, key=len)

# Finds the <span> elements with the class="user user-role-registered-member". They will contain each thread creator's name.
thread_authors = soup1.find_all("span", {"class": "user user-role-registered-member"})
thread_authors_filtered = []

# Since thread_authors is a list of both the thread author and the latest reply's author, since we want the thread author
# the latest reply's author is filtered out, since every odd index value in thread_authors is a latest reply author
for author_index, thread_author in enumerate(thread_authors):
    if author_index % 2 == 1:
        continue
    thread_authors_filtered.append(thread_author.get_text())

# Each thread text file is set to the File variable and then all the lines are put into a variable called contents
# Each corresponding thread text file's author is gotten by using a for loop where i can be both the index of the 
# text file in the list of directories and the index of the author in the list of filtered author names
# and then inserted at the index 
for i in range(len(directs)):
    file = open(f'{Path.home()}\\VSCPythonProjects\\read_forums_proj\\forums_thread_data\\{directs_modified[i]}', 'r')
    contents = file.readlines()
    file.close()
    # Inserts Author Name on Index 2 of Each File (which is right after the Title and Reply By and before message contents)
    # Then the Reply By is removed using the .pop() method on the contents list
    contents.insert(2, f"Thread Author: {thread_authors_filtered[i]}\n\n{('-' * 50)}\n\n")
    contents.pop(1)
    file = open(f'{Path.home()}\\VSCPythonProjects\\read_forums_proj\\forums_thread_data\\{directs_modified[i]}', 'w')
    for content in contents:
        file.write(content)
    file.close()

print('All threads have been downloaded into their respective text files.')

