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
            course_offering_id=f'OFFERING-{cn}-{ins}'
            return course_offering_id
    @staticmethod        
    def get_dict_values(dict_var,var):
            dict_var=dict_var
            return dict_var[var]        
    @staticmethod
    def get_name_from_email(email):
            return email.split('@')[0].upper() 
    @staticmethod
    def get_list_value(list_var,var):
            var1=[x for x in list_var if var.lower() in x]
            return var1[0].upper()
    @staticmethod
    def get_command_value(command,index):
            return command.split('-')[index]              
    #Function for course registration        
    def register_couse(self,cn,email):
            if cn in self.reg_emp_details.keys():
                self.reg_emp_details[cn].append(email)
            else:
                self.reg_emp_details[cn]=[email]
            index_of_the_course=self.get_dict_values(self.course_id,cn)-1001
            comp1="max_emp"
            comp1_val=self.get_dict_values(self.courses[index_of_the_course],comp1)
            reg_emp_for_the_course=self.get_dict_values(self.reg_emp_details,cn)
            if int(comp1_val)>=len(reg_emp_for_the_course):
                course_registration_id=f'REG-COURSE-{self.get_name_from_email(email)}-{cn.upper()}'
                self.course_registration.append(course_registration_id)
                return f'{course_registration_id} ACCEPTED'
            else:
                self.reg_emp_details.get(cn).pop()
                return "COURSE_FULL_ERROR"
    #Function to allot course                     
    def allot_course(self,cod):
           self.course_allot.append(self.get_command_value(cod,1))
           allot=""
           cn=self.get_command_value(cod,1)
           index_of_the_course=self.get_dict_values(self.course_id,cn)-1001
           comp2="min_emp"
           comp2_val=self.get_dict_values(self.courses[index_of_the_course],comp2)
           reg_emp_for_the_course=self.get_dict_values(self.reg_emp_details,cn)
           if len(reg_emp_for_the_course)<int(comp2_val):
                self.course_registration.sort()
                for i in self.course_registration:
                    if cn in i: 
                       emp_name=self.get_command_value(i,2)
                       emp_email=self.get_list_value(reg_emp_for_the_course,emp_name)
                       date=self.get_dict_values(self.courses[index_of_the_course],'date')
                       instructor_name=self.get_dict_values(self.courses[index_of_the_course],'instructor')
                       allot=f'{i} {emp_email} COURSE_CANCELED {cn} {instructor_name} {date}'
                       print(allot) 
           #Course allotment will be done here if minimum no of employees registered          
           else:         
                allot=""
                self.course_registration.sort()
                for i in self.course_registration:
                    if cn in i: 
                       emp_name=self.get_command_value(i,2)
                       emp_email=self.get_list_value(reg_emp_for_the_course,emp_name)
                       date=self.get_dict_values(self.courses[index_of_the_course],'date')
                       instructor_name=self.get_dict_values(self.courses[index_of_the_course],'instructor')
                       allot=f'{i} {emp_email} {cod} {cn} {instructor_name} {date} CONFIRMED'
                       print(allot)  
    #Function to cancel registration course                                  
    def cancel_course(self,cri):
            cn=self.get_command_value(cri,3)  
            if cn in self.course_allot: #If allotment of course is done then can't cancel registration
                    status=f"{cri} CANCEL_REJECTED"
                    return status   
            else:
                    reg_emp_for_the_course=self.get_dict_values(self.reg_emp_details,cn)
                    emp_name=self.get_command_value(cri,2)
                    emp_email=self.get_list_value(reg_emp_for_the_course,emp_name)
                    reg_emp_for_the_course.remove(emp_email.lower())
                    self.course_registration.remove(cri.upper())
                    status=f"{cri} CANCEL_ACCEPTED"
                    return status #If allotment of course is not yet done then they can cancel registration
def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    #Created Object for LMS class    
    obj=LMS()
    max_args=5 #Input Validation for create course command
    min_args=2 #Input Validation for all the commands apart from create course 
    #Read input commands from input txt file     
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    #Added validations for input commands
    for line in Lines:
        query=line.strip().split(' ')
        if query[0]=='ADD-COURSE-OFFERING': 
                   if len(query[1:])==max_args:
                       print(obj.add_couse(query[1],query[2],query[3],query[4],query[5]))
                   else:
                       print("INPUT_DATA_ERROR")     
        if query[0]=='REGISTER':
                   if len(query[1:])==min_args:
                       print(obj.register_couse(query[2].split('-')[1],query[1]))
                   else:
                       print("INPUT_DATA_ERROR")     
        if query[0]=='ALLOT':
                   if len(query)==min_args:
                       obj.allot_course(query[1])
                   else:
                       print("INPUT_DATA_ERROR")          
        if query[0]=='CANCEL':
                   if len(query)==min_args: 
                       print(obj.cancel_course(query[1]))
                   else:
                       print("INPUT_DATA_ERROR")               
if __name__ == "__main__":
    main()

