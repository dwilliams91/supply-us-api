# Overview:

Supply Us is a full-CRUD, single page application which allows teachers to upload supply lists for their classes and allows parents and students to see one single list with all the supplies they need. 

By creating a standardized way for teachers to create their lists, items on lists can be added together to produce the total amount of an item needed. For example, if one teacher wants students to have 2 packs of mechanical pencils, and another teacher wants students to have 1 pack of pre-sharpened pencils, parents and students can see in one line that they need to buy 3 packs of pencils, with detials to show the specific breakdown. 

#Technologies:
This repo holds the RESTful API made with Django. 
https://github.com/dwilliams91/Supply-Us-React This link is the react based front end. 

#Features:
Supply Us allows for teachers to add classes, then create a supply list for that class. They can find an item through a dropdown menu, and they can filter that dropdown menu through a search bar or another dropdown. Once they select an item, select from a list of associated package types. Then they put in the a number of that item students need to buy, and can add any other description. Teachers can also edit supplies in the database or add an item. Lastly, teachers can delete items from a list or entire classes.

Parents can login and see a dropdown menu of all the classes available. Once they select a class, they can save it and see that class's supply list. They can add as many classes as needed and see the cumulative added lists. Lastly, they can view each individual list.
