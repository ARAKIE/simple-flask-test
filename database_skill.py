# import sqlite3

# db = sqlite3.connect("app.db")

# cr = db.cursor()

# # function commit and close
# def commit_and_close():
#     db.commit()
    
#     db.close()
#     print(" connection to db is closed ")

# # user id
# uid = 1

# input_message = """
# What do you want to do ?
# "s" => Show all
# "a" => Add New Skill
# "d" => Delete A skill 
# "u" => Update Skill Progress
# "q" => Quit the App
# Choose option "

# """






# user_input = input(input_message).strip().lower()

# #Command list

# command_list = ["s" , "a" , "d" , "u" , "q"]

# def show_skill():
#     print("show skill")
    
#     commit_and_close()
    
# def add_skill():
#     sk = input("write skill name ").strip().capitalize()
#     prog = input("writer skill progress ").strip()
    
#     cr.execute(f"insert into skills (name , progress , user_id) values('{sk}' , '{prog}' , '{uid}')")
    
#     commit_and_close()
    
# def delete_skill():
#     sk = input("write skill name ").strip().capitalize()
    
    
#     cr.execute(f"delete from  skills where name = '{sk}' and user_id ='{uid}' ")
    
#     commit_and_close()
    
# def update_skill():
#     print("update skill")
    
#     commit_and_close()
    

    




# #check
# if user_input in command_list:
    
    
#     if user_input == "s":
#         show_skill()
#     elif user_input =="a":
#         add_skill()
#     elif user_input =="d":
#         delete_skill()
#     elif user_input == "u":
#         update_skill()
#     else:
#         print("app is closed")
    
    
# else:
#     print(f"command {user_input} not found ")
    
    
    
    
