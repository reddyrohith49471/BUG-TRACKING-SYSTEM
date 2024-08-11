import mysql.connector
def get_db_connection():
    return mysql.connector.connect(host = "localhost",user = "Your_username",password="Your_password",database = "bds",charset="utf8")
def main_menu():
    print("*******MAIN MENU********")
    print("1.ADMIN MODULE")
    print("2.MANAGER PANEL")
    print("3.EMPLOYEE PANEL")
    choice = int(input("Enter number to open module:-"))
    if(choice == 1):
        Admin_module()
    elif(choice == 2):
        Manager_panel()
    elif(choice == 3):
        Employee_panel()
    else:
        print("INVALID")

def Admin_module():
    while True:
        print("******ADMIN MODULE*******")
        print("1.MANAGER")
        print("2.EMPLOYEE")
        print("3.View All Project")
        print("4.View Bug's Reports")
        print("5.Exit")
        choice1 = int(input("Enter which one You need to go:-"))
        if(choice1 == 1):
            Admin_module_manager()
        elif(choice1 == 2):
            Admin_module_employee()
        elif(choice1 == 3):
            Admin_module_view_all_projects()
        elif(choice1 == 4):
            View_all_bugs()
        elif(choice1 == 5):
            print("Exiting....")
            break
        else:
            print("Invalid Choice")


def Admin_module_manager():
    print("*******MANAGER*******")
    print("1.Add Manager Account")
    print("2.View Manager Account")
    print("3.Delete Manager")
    print("4.Update Manager Detail's")
    choice2 = int(input("Enter which you need to do:-"))
    if(choice2 == 1):
        Add_manager_account()
    elif(choice2 == 2):
        View_manager_account()
    elif(choice2 == 3):
        Delete_manager()
    elif(choice2 == 4):
        update_manager_details()
    else:
        print("Invalid Choice")
        

def Add_manager_account():
    print("*******Adding Manager Details********")
    try:
        empcode = int(input("Enter Employee Code:-"))
        empname = input("Enter Name:-")
        if not empname:
            print("Name cannot be empty.")
            return
        empemail = input("Enter Email:-")
        if '@' not in empemail:
            print("Please enter a valid email address.")
            return
        emppassword = input("Enter password:-")
        if len(emppassword) < 8:
            print("Password must be at least 8 characters long.")
            return
        gender = input("Enter Gender('M' or 'F'):-").strip().upper()
        if gender not in ['M', 'F']:
            print("Invalid gender. Please enter M or F.")
            return
        dob = input("Enter Date of birth(YYYY-MM-DD):-").strip()
        
        mobileno = int(input("Enter Mobile Number:-"))

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO employee(empcode, empname, empemail, emppassword, gender, dob, mobileno, role) VALUES (%s, %s, %s, %s, %s, %s, %s, 'Manager')"""
        cursor.execute(query, (empcode, empname, empemail, emppassword, gender, dob, mobileno))
        conn.commit()
        cursor.close()
        conn.close()
        print("Manager added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def View_manager_account():
    print("******MANAGER'S*******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from employee where role='Manager'")

    managers = cursor.fetchall()
    if not managers:
        print("No managers found.")
    else:
        for row in managers:
            print(row)
    cursor.close()
    conn.close()


def Delete_manager():
    empcode = int(input("Enter Employee Code of the manager to delete:-"))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "delete from employee where empcode = %s AND role = 'Manager'"
    cursor.execute(query,(empcode,))
    conn.commit()
    if cursor.rowcount>0:
        print("Manager deleted Successfully!")
    else:
        print("Manager not found")
    cursor.close()
    conn.close()

def update_manager_details():
    print("******TO UPDATE MANAGER DETAILS******")
    empcode = int(input("Enter Employee code of the manager to update:-"))
    new_name = input("Enter new name:-")
    new_email = input("Enter New email:-")
    new_password = input("Enter New password:-")
    new_gender = input("Enter New Gender:-")
    new_dob = input("Enter New dob(YYYY-MM-DD):-")
    new_mobile_no = int(input("Enter New mobile no.:-"))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """update employee set empname = %s,empemail = %s,emppassword = %s,gender = %s,dob = %s,mobileno = %s where empcode = %s AND role = 'Manager'"""
    cursor.execute(query,(new_name,new_email,new_password,new_gender,new_dob,new_mobile_no,empcode))
    conn.commit()
    if cursor.rowcount>0:
        print("Manager details updated successfully!")
    else:
        print("manager not found.")
    cursor.close()
    conn.close()


def Admin_module_employee():
    print("******EMPLOYEE*******")
    print("1.Add Employee Account")
    print("2.View Employee's Account")
    print("3.Delete Employee Account")
    print("4.update Employee Detail's")
    choice3 = int(input("Enter Number to perform operation:"))
    if(choice3 == 1):
        Add_employee_account()
    elif(choice3 == 2):
        View_employee_account()
    elif(choice3 == 3):
        Delete_employee_account()
    elif(choice3 == 4):
        Update_employee_details()
    else:
        print("INVALID CHOICE")

def Add_employee_account():
    print("*********TO ADD EMPLOYEE ACCOUNT*********")
    try:
        empcode = int(input("Enter Employee Code:-"))
        empname = input("Enter Name:-")
        if not empname:
            print("Name cannot be empty.")
            return
        empemail = input("Enter Email:-")
        if '@' not in empemail:
            print("Please enter a valid email address.")
            return
        emppassword = input("Enter password:-")
        if len(emppassword) < 8:
            print("Password must be at least 8 characters long.")
            return
        gender = input("Enter Gender:-").strip().upper()
        if gender not in ['M', 'F']:
            print("Invalid gender. Please enter M or F.")
            return
        dob = input("Enter Date of birth(YYYY-MM-DD):-").strip()

        mobileno = int(input("Enter Mobile Number:-"))

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO employee(empcode, empname, empemail, emppassword, gender, dob, mobileno, role) VALUES (%s, %s, %s, %s, %s, %s, %s, 'Employee')"""
        cursor.execute(query, (empcode, empname, empemail, emppassword, gender, dob, mobileno))
        conn.commit()
        cursor.close()
        conn.close()
        print("Employee added successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

def View_employee_account():
    print("********TO VIEW EMPLOYEE ACCOUNT********")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from employee where role='Employee'")

    employees = cursor.fetchall()
    if not employees:
        print("No Employees found.")
    else:
        for row in employees:
            print(row)
    cursor.close()
    conn.close()

def Delete_employee_account():
    empcode = int(input("Enter Employee Code of the employee to delete:-"))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "delete from employee where empcode = %s AND role = 'Employee'"
    cursor.execute(query,(empcode,))
    conn.commit()
    if cursor.rowcount>0:
        print("Employee deleted Successfully!")
    else:
        print("Employee not found")
    cursor.close()
    conn.close()


def Update_employee_details():
    print("********TO UPDATE EMPLOYEE DETAILS*********")
    empcode = int(input("Enter Employee code of the Employee to update:-"))
    new_name = input("Enter new name:-")
    new_email = input("Enter New email:-")
    new_password = input("Enter New password:-")
    new_gender = input("Enter New Gender:-")
    new_dob = input("Enter New dob(YYYY-MM-DD):-")
    new_mobile_no = int(input("Enter New mobile no.:-"))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """update employee set empname = %s,empemail = %s,emppassword = %s,gender = %s,dob = %s,mobileno = %s where empcode = %s AND role = 'Employee'"""
    cursor.execute(query,(new_name,new_email,new_password,new_gender,new_dob,new_mobile_no,empcode))
    conn.commit()
    if cursor.rowcount>0:
        print("Employee details updated successfully!")
    else:
        print("Employee not found.")
    cursor.close()
    conn.close()

def Manager_panel():
    while True:
        print("*********MANAGER PANEL*********")
        print("1.Update Profile")
        print("2.Manage Project")
        print("3.Bug's")
        print("4.exit")
        choice4 = int(input("Enter your choice to do:-"))
        if(choice4 == 1):
            update_manager_details()
        elif(choice4 == 2):
            Manage_project()
        elif(choice4 == 3):
            Bugs()
        elif(choice4 == 4):
            print("Exiting....")
            break
        else:
            print("INVALID CHOICE")


def Manage_project():
    print("*******PROJECT*********")
    print("1.Add project")
    print("2.View all project")
    print("3.Delete project")
    print("4.Update project")
    choice5 = int(input("Enter Your Choice:-"))
    if(choice5 == 1):
        Add_project()
    elif(choice5 == 2):
        View_all_projects()
    elif(choice5 == 3):
        Delete_project()
    elif(choice5 == 4):
        Update_project()
    else:
        print("INVALID CHOICE")


def Add_project():
    print("******TO ADD PROJECT*******")
    projectid = int(input("Enter projectid:-"))
    projectname = input("Enter project name:-")
    sdate = input("Enter starting date of project:-")
    edate = input("Enter ending date of project:-")
    projectdec = input("Enter project description:-")
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """insert into project(projectid,projectname,sdate,edate,projectdec)values(%s,%s,%s,%s,%s)"""
    cursor.execute(query,(projectid,projectname,sdate,edate,projectdec))
    conn.commit()
    cursor.close()
    conn.close()
    print("Project Added Sucessfully")

def View_all_projects():
    print("******TO VIEW PROJECT******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from project")

    projects = cursor.fetchall()
    if not projects:
        print("No projects found.")
    else:
        for row in projects:
            print(row)
    cursor.close()
    conn.close()


def Delete_project():
    projectid = int(input("Enter projectid of the project to delete:"))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "delete from project where projectid = %s"
    cursor.execute(query,(projectid,))
    conn.commit()
    if cursor.rowcount>0:
        print("project deleted Successfully!")
    else:
        print("project not found")
    cursor.close()
    conn.close()


def Update_project():
    print("*********TO DELETE PROJECT********")
    projectid = int(input("Enter projectid of the project to update:"))
    new_project_name = input("Enter new projectname:-")
    new_sdate = input("Enter new Starting date:-")
    new_edate = input("Enter new Ending date:-")
    new_projectdec = input("Enter new project description:-")

    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE project SET projectname = %s, sdate = %s, edate = %s, projectdec = %s WHERE projectid = %s"""
    cursor.execute(query, (new_project_name, new_sdate, new_edate, new_projectdec, projectid))
    conn.commit()

    if cursor.rowcount > 0:
        print("Project details updated successfully!")
    else:
        print("Project not found.")
    
    cursor.close()
    conn.close()

    
def Admin_module_view_all_projects():
    print("********TO VIEW ALL PROJECTS*********")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from project")

    projects = cursor.fetchall()
    if not projects:
        print("No projects found.")
    else:
        for row in projects:
            print(row)
    cursor.close()
    conn.close()

def Bugs():
    print("*******BUG'S*******")
    print("1.Add new bug")
    print("2.View all bugs")
    print("3.Update bug")
    print("4.Delete bug")
    choice6 = int(input("Enter Your choice:-"))
    if(choice6 == 1):
        Add_new_bug()
    elif(choice6 == 2):
        View_all_bugs()
    elif(choice6 == 3):
        Update_bug()
    elif(choice6 == 4):
        Delete_bug()

def Add_new_bug():
    print("*******TO ADD NEW BUG*******")
    bugno = int(input("Enter bug number:-"))
    bugcode = int(input("Enter bug code:-"))
    projectid = int(input("Enter project id where you found bug:-"))
    tcode = int(input("Enter tester employee code:-"))  
    ecode = int(input("Enter executer employee code:-")) 
    status = input("Enter status of your bug:-")
    bugdes = input("Enter description of your bug:-")

    conn = get_db_connection()
    cursor = conn.cursor()

 
    check_query = "SELECT COUNT(*) FROM bugtype WHERE bugcode = %s"
    cursor.execute(check_query, (bugcode,))
    count = cursor.fetchone()[0]

    if count == 0:
        print("The entered bug code does not exist. Please enter a valid bug code.")
        cursor.close()
        conn.close()
        return  

    
    query = """INSERT INTO bugreport(bugno, bugcode, projectid, tcode, ecode, status, bugdes) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (bugno, bugcode, projectid, tcode, ecode, status, bugdes))
    conn.commit()
    cursor.close()
    conn.close()
    print("Bug report added successfully")




def View_all_bugs():
    print("*******TO VIEW BUG'S*******")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from bugreport")

    bugreports = cursor.fetchall()
    if not bugreports:
        print("No bugreports found.")
    else:
        for row in bugreports:
            print(row)
    cursor.close()
    conn.close()


def Update_bug():
    print("*******TO UPDATE BUG*******")
    bugno = int(input("Enter bug number to update:-"))
    new_bugcode = int(input("Enter new bug code to update:-"))
    new_projectid = int(input("Enter new project id to update:-"))
    new_tcode = int(input("Enter new tester employee code:-"))
    new_ecode = int(input("Enter new executer employee code:-"))
    new_status = input("Enter new status of bug:-")
    new_bugdes = input("Enter new description for bug:-")
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        
        query = """UPDATE bugreport SET bugno = %s,
                                  new_bugcode = %s,
                                  new_projectid = %s,
                                  new_tcode = %s,
                                  new_ecode = %s,
                                  new_status = %s,
                                  new_bugdes = %s
                             WHERE bugno = %s"""
        cursor.execute(query, (new_bugcode, new_projectid, new_tcode, new_ecode, new_status, new_bugdes, bugno))
        
        if cursor.rowcount > 0:
            print("Bug report details updated successfully!")
        else:
            print("Bug report not found.")
            
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()






def Delete_bug():
    bugno = int(input("Enter bugno of the bugreport to delete:"))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "delete from bugreport where bugno = %s"
    cursor.execute(query,(bugno,))
    conn.commit()
    if cursor.rowcount>0:
        print("bugreport deleted Successfully!")
    else:
        print("bugreport not found")
    cursor.close()
    conn.close()


def Employee_panel():
    while True:
        print("*********EMPLOYEE PANEL********")
        print("1.Update profile")
        print("2.Add Bug's Report")
        print("3.Update Bug status")
        print("4.View Bug's")
        print("5.Bug details")
        print("6.Exit")
        choice7 = int(input("Enter Your Choice:-"))
        if(choice7 == 1):
            Update_employee_details_employee_pannel()
        elif(choice7 == 2):
            Add_new_bug_employee_pannel()
        elif(choice7 == 3):
            update_bug_status_employee_pannel()
        elif(choice7 ==  4):
            View_all_bugs_employee_pannel()

        elif(choice7 == 5):
            View_all_bugs_employee_pannel()

        elif(choice7 == 6):
            print("Exiting.....")
            break
        else:
            print("INVALID CHOICE!!")

def Update_employee_details_employee_pannel():
    print("*******TO UPDATE EMPLOYEE DETAILS******")
    empcode = int(input("Enter Employee code of the Employee to update:"))
    new_name = input("Enter new name:-")
    new_email = input("Enter New email:-")
    new_password = input("Enter New password:-")
    new_gender = input("Enter New Gender:-")
    new_dob = input("Enter New dob(YYYY-MM-DD)")
    new_mobile_no = int(input("Enter New mobile no.:-"))
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """update employee set empname = %s,empemail = %s,emppassword = %s,gender = %s,dob = %s,mobileno = %s where empcode = %s AND role = 'Employee'"""
    cursor.execute(query,(new_name,new_email,new_password,new_gender,new_dob,new_mobile_no,empcode))
    conn.commit()
    if cursor.rowcount>0:
        print("Employee details updated successfully!")
    else:
        print("Employee not found.")
    cursor.close()
    conn.close()


def Add_new_bug_employee_pannel():
    print("*******TO ADD NEW BUG*******")
    bugno = int(input("Enter bug number:-"))
    bugcode = int(input("Enter bug code:-"))
    projectid = int(input("Enter project id where you found bug:-"))
    tcode = int(input("Enter tester employee code:-"))  
    ecode = int(input("Enter executer employee code:-")) 
    status = input("Enter status of your bug:-")
    bugdes = input("Enter description of your bug:-")

    conn = get_db_connection()
    cursor = conn.cursor()

 
    check_query = "SELECT COUNT(*) FROM bugtype WHERE bugcode = %s"
    cursor.execute(check_query, (bugcode,))
    count = cursor.fetchone()[0]

    if count == 0:
        print("The entered bug code does not exist. Please enter a valid bug code.")
        cursor.close()
        conn.close()
        return  

    
    query = """INSERT INTO bugreport(bugno, bugcode, projectid, tcode, ecode, status, bugdes) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (bugno, bugcode, projectid, tcode, ecode, status, bugdes))
    conn.commit()
    cursor.close()
    conn.close()
    print("Bug report added successfully")

def update_bug_status_employee_pannel():
    print("*******TO UPDATE BUG STATUS*******")
    bugno = int(input("Enter bug number to update:-"))
    new_status = input("Enter new status of bug:-")
    new_bugdes = input("Enter new description for bug:-")
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        
        query = """UPDATE bugreport SET bugno = %s,
                                  new_status = %s,
                                  new_bugdes = %s
                             WHERE bugno = %s"""
        cursor.execute(query, (new_status, new_bugdes, bugno))
        
        if cursor.rowcount > 0:
            print("Bug report details updated successfully!")
        else:
            print("Bug report not found.")
            
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def View_all_bugs_employee_pannel():
    print("*******TO VIEW ALL BUG'S********")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from bugreport")

    bugreports = cursor.fetchall()
    if not bugreports:
        print("No bugreports found.")
    else:
        for row in bugreports:
            print(row)
    cursor.close()
    conn.close()

 
    
if __name__ == "__main__":
    main_menu()
    print("ENDED")


    


        
    
