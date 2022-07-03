from sys import argv

class Ins():
    def __init__(self):
            self.courses=[] #List of couses List[0]--java list[1]--ROR 
            self.reg_emp_details={}  # dict for course--list of emps
            self.c_id=(i for i in range(1001,1999)) # course id 
            self.course_id={} # dict for cid and list index of course 
            self.course_registration=[] #Course registration
            self.course_allot=[]

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
            
    def reg_couse(self,cn,email):
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
    def allot_course(self,cod):
           self.course_allot.append(cod.split('-')[1])
           allot=""
           if len([x for x in self.reg_emp_details.get(cod.split('-')[1])])<int(self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['min_emp']):
                self.course_registration.sort()
                for i in self.course_registration:
                    if cod.split('-')[1] in i: allot= allot+i+" "+str([x for x in self.reg_emp_details.get(cod.split('-')[1]) if i.split('-')[2] in x ][0])+" "+cod+" "+cod.split('-')[1]+" "+cod.split('-')[2]+" "+self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['date']+" "+status+"\n"
                    print(allot,end="")
                    allot=""
           else:         
                allot=""
                self.course_registration.sort()
                for i in self.course_registration:
                    if cod.split('-')[1] in i: allot= allot+i+" "+str([x for x in self.reg_emp_details.get(cod.split('-')[1]) if i.split('-')[2] in x ][0])+" "+cod+" "+cod.split('-')[1]+" "+cod.split('-')[2]+" "+self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['date']+" "+"ACCEPTED"+"\n"
                    print(allot,end="")
                    allot=""                   
    def cancel_course(self,cri): 
            if cri.split('-')[3] in self.course_allot:
                    print(cri+" "+"CANCEL_REJECTED")   
            else:
                    (self.reg_emp_details.get(cri.split('-')[3])).remove([x for x in self.reg_emp_details.get(cri.split('-')[3]) if x.split('@')[0].upper()==cri.split('-')[2].upper()][0]) 
                    print(cri+" "+"CANCEL_ACCEPTED")                 
def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    a1=Ins()    
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    for line in Lines:
        process=line.strip().split(' ')
        if process[0]=='ADD-COURSE-OFFERING': 
                   a1.add_couse(process[1],process[2],process[3],process[4],process[5])
                   print("OFFERING"+"-"+process[1].upper()+"-"+process[2].upper())
        if process[0]=='REGISTER':
                   print(a1.reg_couse(process[2].split('-')[1],process[1]))
        if process[0]=='ALLOT-COURSE':
                   a1.allot_course(process[1])
        if process[0]=='CANCEL':
                   a1.cancel_course(process[1])           
if __name__ == "__main__":
    main()

