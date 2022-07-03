from sys import argv

class LMS():
    #Constructor to initialize the variables 
    def __init__(self):
            self.courses=[] #List of couses stored in List
            self.reg_emp_details={}  # Registerd employees stored in dictionary
            self.c_id=(i for i in range(1001,1999)) # Course ids will be generated from generator
            self.course_id={} # Dictionary for course id to get list index for that particular course 
            self.course_registration=[] #Course registration details stored in list
            self.course_allot=[] #Alloted courses list
    #Function to create a course, each course details stored in dictionary and that dictionary stored in list     
    def add_couse(self,cn,ins,dt,mine,maxe):
            self.course_id[cn.upper()]=next(self.c_id)
            self.course_details={
                "course_name":cn,
                 "instructor":ins,
                 "date":dt,
                 "min_emp":mine,
                 "max_emp":maxe
                                  }        
            self.courses.append(self.course_details)
    #Function for course registration        
    def register_couse(self,cn,email):
            if cn in self.reg_emp_details.keys():
                self.reg_emp_details[cn].append(email)
            else:
                self.reg_emp_details[cn]=[email]
            if int(self.courses[(self.course_id.get(cn))-1001]['max_emp'])>=len(self.reg_emp_details.get(cn)):
                course_registration_id= "REG-COURSE"+"-"+email.split('@')[0].upper()+"-"+cn.upper()
                self.course_registration.append(course_registration_id)
                return course_registration_id+" "+"ACCEPTED"
            else:
                self.reg_emp_details.get(cn).pop()
                return "COURSE_FULL_ERROR"
    #Function to allot course                     
    def allot_course(self,cod):
           self.course_allot.append(cod.split('-')[1])
           allot=""
           #Course will be cancelled here if minimum no of employees are not registered 
           if len([x for x in self.reg_emp_details.get(cod.split('-')[1])])<int(self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['min_emp']):
                self.course_registration.sort()
                for i in self.course_registration:
                    if cod.split('-')[1] in i: allot= allot+i+" "+"COURSE_CANCELED"+str([x for x in self.reg_emp_details.get(cod.split('-')[1]) if i.split('-')[2].lower() in x][0].upper())+" "+cod.split('-')[1]+" "+cod.split('-')[2]+" "+self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['date']+"\n"
                    print(allot,end="")
                    allot=""
           #Course allotment will be done here if minimum no of employees registered          
           else:         
                allot=""
                self.course_registration.sort()
                for i in self.course_registration:
                    if cod.split('-')[1] in i: allot= allot+i+" "+" "+cod+" "+str([x for x in self.reg_emp_details.get(cod.split('-')[1]) if i.split('-')[2].lower() in x][0].upper())+" "+cod.split('-')[1]+" "+cod.split('-')[2]+" "+self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['date']+" "+"ACCEPTED"+"\n"
                    print(allot,end="")
                    allot="" 
    #Function to cancel registration course                                  
    def cancel_course(self,cri): 
            if cri.split('-')[3] in self.course_allot: #If allotment of course is done then can't cancel registration
                    print(cri+" "+"CANCEL_REJECTED")   
            else:
                    (self.reg_emp_details.get(cri.split('-')[3])).remove([x for x in self.reg_emp_details.get(cri.split('-')[3]) if x.split('@')[0].upper()==cri.split('-')[2].upper()][0]) 
                    self.course_registration.remove(cri.upper())
                    print(cri+" "+"CANCEL_ACCEPTED") #If allotment of course is not yet done then they can cancel registration
def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    #Created Object for LMS class    
    obj=LMS()
    #Read input commands from input txt file     
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    #Added validations for input commands
    for line in Lines:
        query=line.strip().split(' ')
        if query[0]=='ADD-COURSE-OFFERING': 
                   if len(query[1:])==5:
                       obj.add_couse(query[1],query[2],query[3],query[4],query[5])
                       print("OFFERING"+"-"+query[1].upper()+"-"+query[2].upper())
                   else:
                       print("INPUT_DATA_ERROR")     
        if query[0]=='REGISTER':
                   if len(query[1:])==2:
                       print(obj.register_couse(query[2].split('-')[1],query[1]))
                   else:
                       print("INPUT_DATA_ERROR")     
        if query[0]=='ALLOT-COURSE':
                   if len(query)==2:
                       obj.allot_course(query[1])
                   else:
                       print("INPUT_DATA_ERROR")          
        if query[0]=='CANCEL':
                   if len(query)==2: 
                       obj.cancel_course(query[1])
                   else:
                       print("INPUT_DATA_ERROR")               
if __name__ == "__main__":
    main()

