##demonstrates how to drill down into a dictionary, that has a list of 
##dictionaries and access the values inside
contacts = {
    "number": 4,
    "students":
        [
            {"name":"Sarah Holderness", "email":"sarah@example.com"},
            {"name":"Homelander", "email":"homelander@example.com"},
            {"name":"Derek Jeter", "email":"jeter@example.com"},
            {"name":"Peyton Manning", "email":"pmanning18@example.com"}      
        ]
}

print("Student emails:")
for student in contacts["students"]:
    print(student["email"])