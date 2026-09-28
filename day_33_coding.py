def student_profile():
    student_information = {
        "name" : "Elio leon",
        "age" : 20,
        "grade" : "A"
    }
    print(student_information["name"])
    student_information["grade"] = "b"
    print(student_information["grade"])
    student_information["school"] = 'South miami senoir high'
    print(student_information["school"])



def phone_book():
    people_I_know = {
        "elio leon jr" : "343-256-4914",
        "Elio leon sr" : "334-234-1273",
        "mom" : "602-323-0945",
        
    }
    people_I_know["friend"] = "456-231-0546"
    people_I_know["elio leon jr"] = "245-8775-4356"
    people_I_know.pop("mom")
    print(people_I_know)
    
phone_book()