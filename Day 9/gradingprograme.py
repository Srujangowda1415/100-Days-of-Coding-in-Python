# create a new dictionary 
# uske keys me naam hona chahiye isi dictionary se
# or uske values me marks leke if else se values update kara


# values kaise add hogi?
#  dict["loop"]="joker"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 100
}
student_grades={

}
for i in student_scores:
    
    if student_scores[i]>91 and student_scores[i]<100 :
        y="Outstanding"
        student_grades[i]=y
    elif student_scores[i]>81 and student_scores[i]<90 :
        y="Exceeds Expectations"
        student_grades[i]=y
    elif student_scores[i]>71 and student_scores[i]<80 :
        y="Acceptable"
        student_grades[i]=y
    elif student_scores[i]<70 :
        y="Fail"
        student_grades[i]=y

dict1={
    "pehla key":["pehla value","doosra value","teesra value"],
    "doosra key":["tumko kya","kyu"]
}

travel_log={
    "France":{
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
    },
    "Germany":{
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    }
}

# print(travel_log["Germany"]["cities_visited"][2])

print(max(student_scores,key=student_scores.get))