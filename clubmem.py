# Homepage
from pyscript import display, document # type: ignore

def student_club(e):
    document.getElementById('result').innerHTML = ' '
    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value
    # Combines the first and last names to form the students' full name  
    student_fullname = firstname + ' ' + lastname

    # List of members 
    science_names = ['Elianna Co','Georgina Sarmiento','Mallorie Micu', 'Aiva Suson', 'Miishka Eugenio']

    # Checks if student's name inputted matches a current member 
    member_checker = student_fullname in science_names

    # Displays acceptance or rejection 
    display_message = (f'Sorry, you are not a part of the OBGH Science Club.', f'Congratulations {student_fullname}, you are now part of the OBGH Science Club!')

    document.getElementById('result').innerHTML = (display_message[member_checker])