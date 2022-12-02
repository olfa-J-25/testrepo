#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
db_loc=sqlite3.connect('Esb.db')
cursor=db_loc.cursor()
cursor.execute(''' CREATE TABLE etudiant(id INTEGER PRIMARY KEY , name TEXT , first name TEXT)''')

