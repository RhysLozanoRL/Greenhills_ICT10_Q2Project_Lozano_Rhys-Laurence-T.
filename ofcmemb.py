# Set Operators
from pyscript import display, document # type: ignore # type: 

grade_7 = {'Georgina Sarmiento', 'Elianna Co'}
grade_8 = {'Miishka Eugenio', 'Aiva Suson'}
grade_9 = {'Mallorie Micu', 'Liesl Pascual'}
grade_10 = {'Savannah Reyes', 'Zoe Reyes'}

members = grade_7.union(grade_8, grade_9, grade_10)

def student_members(e):
    
    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value

# Combines the students' first and lastname
    student_fullname = firstname + ' ' + lastname

#Updates the members status, meaning when you add another new member the last member added before still remains
    members.update({student_fullname})

# Adds the member
    members.add(student_fullname)
    display("All members : ", members, target='output')

#Displays the total number of members 
    display("Total number of members now : ", len(members), target='output')


  