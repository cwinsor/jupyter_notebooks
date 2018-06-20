
# coding: utf-8

# In[ ]:


import os.getpass



def get_username_password():
    import getpass
    username = input("JAMA username>")
#    password = getpass.getpass("JAMA password>")
    password = getpass("JAMA password>")
    return[username,password]


def get(url):
    response = requests.get(url, auth=(username, password))
    return json.loads(response.text)

