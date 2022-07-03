from sys import argv

class Ins():
    def __init__(self):
            self.courses=[] #List of couses 
            self.reg_emp_details={}  # Registerd employees Dict
            self.c_id=(i for i in range(1001,1999)) # course id 
            self.course_id={} # dict for cid and list index of course 
            self.course_registration=[] #Course registration
            self.course_allot=[] #Alloted courses list

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
    def allot_course(self,cod):
           self.course_allot.append(cod.split('-')[1])
           allot=""
           if len([x for x in self.reg_emp_details.get(cod.split('-')[1])])<int(self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['min_emp']):
                self.course_registration.sort()
                for i in self.course_registration:
                    if cod.split('-')[1] in i: allot= allot+i+" "+str([x for x in self.reg_emp_details.get(cod.split('-')[1]) if i.split('-')[2].lower() in x][0].upper())+" "+"COURSE_CANCELED"+" "+cod.split('-')[1]+" "+cod.split('-')[2]+" "+self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['date']+"\n"
                    print(allot,end="")
                    allot=""
           else:         
                allot=""
                self.course_registration.sort()
                for i in self.course_registration:
                    if cod.split('-')[1] in i: allot= allot+i+" "+" "+cod+" "+str([x for x in self.reg_emp_details.get(cod.split('-')[1]) if i.split('-')[2].lower() in x][0].upper())+" "+cod.split('-')[1]+" "+cod.split('-')[2]+" "+self.courses[(self.course_id.get(cod.split('-')[1]))-1001]['date']+" "+"ACCEPTED"+"\n"
                    print(allot,end="")
                    allot=""                   
    def cancel_course(self,cri): 
            if cri.split('-')[3] in self.course_allot:
                    print(cri+" "+"CANCEL_REJECTED")   
            else:
                    (self.reg_emp_details.get(cri.split('-')[3])).remove([x for x in self.reg_emp_details.get(cri.split('-')[3]) if x.split('@')[0].upper()==cri.split('-')[2].upper()][0]) 
                    self.course_registration.remove(cri.upper())
                    print(cri+" "+"CANCEL_ACCEPTED")
                    

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    a1=Ins()    
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    for line in Lines:
        query=line.strip().split(' ')
        if query[0]=='ADD-COURSE-OFFERING': 
                   if len(query[1:])==5:
                       a1.add_couse(query[1],query[2],query[3],query[4],query[5])
                       print("OFFERING"+"-"+query[1].upper()+"-"+query[2].upper())
                   else:
                       print("INPUT_DATA_ERROR")     
        if query[0]=='REGISTER':
                   if len(query[1:])==2:
                       print(a1.register_couse(query[2].split('-')[1],query[1]))
                   else:
                       print("INPUT_DATA_ERROR")     
        if query[0]=='ALLOT-COURSE':
                   if len(query)==2:
                       a1.allot_course(query[1])
                   else:
                       print("INPUT_DATA_ERROR")          
        if query[0]=='CANCEL':
                   if len(query)==2: 
                       a1.cancel_course(query[1])
                   else:
                       print("INPUT_DATA_ERROR")               
if __name__ == "__main__":
    main()

