# Contact management system

App user should be able to create and see contacts. User also must be able to 
update the records and delete them. Application saves all information in JSON file.



##  UI
This is CLI application


## QA
- Contact 
    - Name
    - Telephone number
    - Email

What operations should be able?
- Create contact
- Update contact
- Delete contact
- Read contacts
- *Filter contacts

Is it possible to reuse data from previous session?
- Yes. Program should store all update on disk. There should be option,
to not save last updates.

Is it okay to have fullname? Or we should store name and surname separately? 
- Fullname is okay for now.

Is it possible to have same name contacts?
- Yes. It is okay to have two `Goga` in contacts


How to choose contact which I want to delete or update? 
- Does not matter for me.

What is contacts list max size?
- 150 contact is expected. 

What validations are required for inputs?
- Name - not required any validation
- Telephone number - length must be more than 8 and less than 15, Only numbers.
- Email - length must be more than 5 and less than 25. @ symbol must be present.



## Technical design document
Which data structure will be used to store contacts information? - dict
Which classes will be there?
- Contact  - contains all info about contact and should support all CRU (D) operation needed methods
- FileHandlerClass - helps to store and read data from files
- Contacts, ContactManager - stores contacts and manages CRUD operations
- Validator class - contains methods for validating various data inputs
- Operator, UserAction - is responsible to communicate possible operations to user and act on user input
Will be classes at all? May be only functions is better?
- create contact - gets contact info and adds contact in contacts store
- update contact - gets id and kwargs(name, email, number) and updates appropriate contact in contacts store
- delete contact - gets id  and deletes contact from contacts store
- read contacts - gets id and prints contact on screen
- validate_{x} - where x is email, name, or phone number
- read contacts from file
- store contacts in file
- function which asks user what they want to do
