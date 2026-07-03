student={"name":"archana","age":12,"course":"python"}
print(student)
print("name:",student["name"])
student["collage"]="mangalam college of engineering"
print(student)
student["age"]=22
print(student)
student.pop("course")
print("after removing",student)
