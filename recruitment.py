# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from

def get_skills():

    skills = ["eating", "dancing", "watching tv"]
   


   
    
return skills
    

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    for index, skill in enumerate(skills, 1):

        print (f"{index}. {skill}")


skills= get_skills()
    




    


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    input_skill = int(input("choose a skill"))
    input_skill2 = int(input("choose a second skill"))
    users_skills_list = [skills[input_skill - 1], skills[input_skill2 - 1]]
    print(users_skills_list)
    return users_skills_list
skills = get_user_skills
get_skills(skills)
    








# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
   cv = {}



   cv["name"] = input("what's your name?")
   cv["age"] = int(input("How old are you?"))
   cv["experience"] = int(input("How many years of experience do you have?"))

   
   cv["skills"]= get_user_skills(skills)
   print(cv)

    
    
    return cv
    get_user_cv(get_skills())



# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    desired_skill = ["eating", "dancing"]
    if 25 <= cv["age"] <= 40 and cv["experience"] > 3 and desired_skill in cv["skills"]:
        return True
        else:
            False

def main():
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    user_cv = get_user_cv(skills)
    is_accepted = check_acceptance(user_cv, [desired_skill])
    if is_accepted:
        print(f"you have been accepted, {user_cv["name"]}")
    else:
        print(f"you have been rejected, try next time!")

    


if __name__ == "__main__":
    main()
