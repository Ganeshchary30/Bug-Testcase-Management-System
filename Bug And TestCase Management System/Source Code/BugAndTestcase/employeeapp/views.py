from django.shortcuts import render, redirect
from adminsapp.models import Employee, Project, News
from adminsapp.forms import EmployeeForm, ProjectForm
from employeeapp.models import Testcase, Bug, Requirements
from employeeapp.forms import TestcaseForm, BugForm, RequirementsForm
from django.db.models import Count
from managementapp.models import Task
from django.http import JsonResponse

# Create your views here.
def employee(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "employee_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "employee_login.html", {"msg": msg})
    return render(request, "employee_login.html", {})

def employee_home(request):
    return render(request, "employee_home.html", {})




from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Employee

def employee_change_pwd(request):
    email = request.session.get("email")

    if not email:
        return redirect('/employee')  # Redirect if no username in session

    if not islogin(request):
        return redirect('/employee')

    msg = ""  # Initialize message variable

    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        # ✅ Check if old and new passwords are the same
        if password == new_password:
            msg = "Your Old Password And New Password Are The Same."
            return render(request, "employee_chpwd.html", {"email": email, "msg": msg})

        try:
            # ✅ Verify the old password
            user = Employee.objects.get(email=email, password=password)
            user.password = new_password
            user.save()

            msg = "Successfully Password Changed."
            return render(request, "employee_login.html", {"email": email, "msg": msg})

        except Employee.DoesNotExist:
            msg = "Invalid Old Password."
            return render(request, "employee_chpwd.html", {"email": email, "msg": msg})

    return render(request, "employee_chpwd.html", {"email": email, "msg": msg})


def employee_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "employee_login.html", {})


def islogin(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def employee_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "employee_edit_profile.html", {"employ": employ, "role":role})


def employee_update_profile(request):
    email = request.session['email']
    role = request.session["role"]
    data = Employee.objects.get(email=email, role=role)
    if request.method == "POST":
        print("hi1")
        email = request.session["email"]
        print(email)
        emp = Employee.objects.get(email=email, role=role)
        print("hi3")
        employee = EmployeeForm(request.POST, instance=emp)
        print("hi4")
        try:
            if employee.is_valid():
                print("hi6")
                employee.save()
                print("hi")
                return render(request, "employee_home.html", {"msg": "Successfully Update", "role": role})
        except Exception as e:
            print(e)
            return render(request, "employee_home.html", {"msg": "your details not updated", "role":role})
    return render(request, "employee_edit_profile.html", {"employee":data, "role":role})



def add_testcase(request):
    if request.method == "POST":
        testcase = TestcaseForm(request.POST)
        print(testcase.errors)

        if testcase.is_valid():
            print("hi2")
            try:
                testcase.save()
                print("h3")
                return redirect("view_testcase")  # ✅ Redirect after successful save
            except Exception as e:
                print(e)
                # Optional: Add an error message here
                return render(request, "add_testcase.html", {
                    "msg": "Something went wrong!",
                    "tester_emails": request.session.get("email"),
                    "details_project": Project.objects.all(),
                    "requirements": Requirements.objects.all()
                })
        else:
            print("Form is not valid!")
            # Optional: Add validation error message
            return render(request, "add_testcase.html", {
                "msg": "Please correct the errors below.",
                "tester_emails": request.session.get("email"),
                "details_project": Project.objects.all(),
                "requirements": Requirements.objects.all(),
                "form": testcase  # To show validation errors in the template
            })

    # GET request fallback
    tester_emails = request.session.get("email")
    details_project = Project.objects.all()
    requirements = Requirements.objects.all()
    return render(request, "add_testcase.html", {
        "tester_emails": tester_emails,
        "details_project": details_project,
        "requirements": requirements
    })


def view_testcase(request):
    email = request.session["email"]
    if request.method == "GET":
        testcases = Testcase.objects.filter(tester_email=email)
        role=request.session["role"]
        return render(request, "view_testcase.html", {"testcases": testcases,"role": role})


def delete_testcase(request, id):
    testcase = Testcase.objects.get(id=id)
    testcase.delete()
    return redirect("/view_testcase")

def edit_testcase(request, id):
    testcases = Testcase.objects.get(id=id)
    tester_emails = request.session["email"]
    details_project = Project.objects.all()
    requirements = Requirements.objects.all()
    return render(request, "edit_testcase.html",
                  {"testcases": testcases, "tester_emails": tester_emails, "details_project": details_project,"requirements":requirements})



def update_testcase(request):
    if request.method == "POST":
        userid = request.POST.get("id")
        testcase_instance = Testcase.objects.get(id=userid)

        # Bind form data to the instance
        testcase_form = TestcaseForm(request.POST, instance=testcase_instance)
        print("hi1")

        try:
            if testcase_form.is_valid():
                print("hi2")
                testcase_form.save()
                print("hi3")
                # Redirect to view_testcase page after successful update
                return redirect("view_testcase")  # Assuming you have a named URL 'view_testcase'
            else:
                print(testcase_form.errors)  # Debug: See why the form is not valid
        except Exception as e:
            print("Error:", e)

        # If something goes wrong, re-render edit page with the form and error message
        tester_emails = request.session.get("email")
        details_project = Project.objects.all()
        requirements = Requirements.objects.all()

        return render(
            request,
            "edit_testcase.html",
            {
                "testcases": testcase_instance,
                "tester_emails": tester_emails,
                "details_project": details_project,
                "requirements": requirements,
                "msg": "There was an error updating the test case. Please try again."
            }
        )


def add_bug(request):
    if request.method == "POST":
        print("hi")
        bugs = BugForm(request.POST,request.FILES)
        print(bugs.errors)
        print("hi1")
        try:
            if bugs.is_valid():
                print("hi2")
                bugs.save()
                print("h3")
        except Exception as e:
            print(e)
        return redirect("view_bug")
        # return render(request, "add_bug.html", {"msg": "success"})
    tested_by = request.session["email"]
    testcaseids = Testcase.objects.filter(status='Fail')
    developersids = Employee.objects.filter(role='devloper')
    return render(request, "add_bug.html",
                          {"tested_by": tested_by, "testcaseids": testcaseids,"developersids":developersids})

def view_bug(request):
    if request.method=="GET":
        bugs=Bug.objects.all()
        role=request.session["role"]
        return render(request,"view_bug.html",{"bugs":bugs,"role":role})

def delete_bug(request, id):
    bugs = Bug.objects.get(id=id)
    bugs.delete()
    return redirect("/view_bug")

def edit_bug(request, id):
    bugs = Bug.objects.get(id=id)
    tested_by = request.session["email"]
    testcaseids = Testcase.objects.filter(status='Fail')
    developersids = Employee.objects.filter(role='devloper')
    return render(request, "edit_bug.html",
                  {"tested_by": tested_by, "testcaseids": testcaseids,"bugs":bugs,"developersids":developersids})


def update_bug(request):
    if request.method == "POST":
        userid = request.POST["id"]
        bugs = Bug.objects.get(id=userid)
        print("hi")
        bugs = BugForm(request.POST,request.FILES,instance=bugs)
        print(bugs.errors)
        print("hi1")
        try:
            if bugs.is_valid():
                print("hi2")
                bugs.save()
                print("h3")
        except Exception as e:
            print(e)
        return redirect("/view_bug", {"msg": "success"})
    return render(request, "edit_bug.html", {})

def developer_view_bugs(request):
    email = request.session["email"]
    if request.method=="GET":
        role=request.session["role"]
        print(role)
        bugs=Bug.objects.filter(developer_email=email)
        return render(request,"developer_view_bugs.html",{"bugs":bugs,"role":role})

def developer_view_testcases(request):
    if request.method == "GET":
        role=request.session["role"]
        testcases = Testcase.objects.all()
        return render(request, "developer_view_testcases.html", {"testcases": testcases,"role":role})




def developer_update_status(request, id):
    # This view shows the form to update status
    try:
        bug = get_object_or_404(Bug, id=id)  # safer than get()
        email = request.session.get("email")

        context = {
            "bugs": bug,
            "email": email,
            "id": id
        }

        return render(request, "developer_status_update.html", context)

    except Exception as e:
        print(e)
        messages.error(request, "Bug not found!")
        return redirect("/developer_view_bugs")  # Redirect to list if something wrong


def developer_status_insert(request):
    # This view handles the POST submission and redirects
    if request.method == "POST":
        try:
            tested_by_email = request.session.get("email")
            status = request.POST.get('status')
            id = request.POST.get('id')

            print("hi1", tested_by_email)
            print("hi2", status, id)

            bug = get_object_or_404(Bug, id=id)  # safer than get()

            bug.status = status
            bug.tested_by_email = tested_by_email

            print("hi3")
            bug.save()
            print("hi4 - Saved Successfully")

            messages.success(request, "Bug status updated successfully!")  # ✅ Success message
            return redirect("/developer_view_bugs")  # ✅ After POST-Redirect-GET (best practice)

        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong during update.")
            return redirect("/developer_view_bugs")  # Redirect in case of error

    else:
        # If someone directly accesses POST handler without submitting
        messages.warning(request, "Invalid request.")
        return redirect("/developer_view_bugs")


def tester_update_status(request, id):
    try:
        bugs = Bug.objects.get(id=id)
        email = request.session.get("email")

        # Render the update form page with bug data
        return render(request, "tester_update_status.html", {"bugs": bugs, "email": email, "id": id})

    except Bug.DoesNotExist:
        # Optional: handle case where bug is not found
        return redirect("/view_bug")  # Or show an error page


def tester_status_insert(request):
    if request.method == "POST":
        try:
            tested_by_email = request.session.get("email")
            status = request.POST.get('status')
            bug_id = request.POST.get('id')

            print("hi1")

            bug = Bug.objects.get(id=bug_id)

            print("hi2")

            bug.status = status
            bug.tested_by_email = tested_by_email

            print("hi3")

            bug.save()

            print("Bug updated successfully!")

            # Redirect to view_bug page after updating
            return redirect("/view_bug")

        except Bug.DoesNotExist:
            print("Bug not found!")
            return redirect("/view_bug")

        except Exception as e:
            print("Error:", e)
            return render(request, "tester_update_status.html", {"error": str(e)})

    # If not POST, just redirect (or handle GET if you want)
    return redirect("/view_bug")


def analyst_view_bugs(request):
    if request.method=="GET":
        bugs=Bug.objects.all()
        return render(request,"analyst_view_bugs.html",{"bugs":bugs})

def analyst_view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
        return render(request, "analyst_view_testcases.html", {"testcases": testcases})

def developer(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "developer_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "developer.html", {"msg": msg})
    return render(request, "developer.html", {})

def developer_home(request):
    return render(request, "developer_home.html", {})





def developer_change_pwd(request):
    email = request.session.get("email")

    if not email:
        return redirect('/developer')  # Redirect if no email in session

    msg = ""  # Initialize message variable

    if islogin(request):
        if request.method == 'POST':
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')

            # ✅ Check if old and new passwords are the same
            if password == new_password:
                msg = "Your Old Password And New Password Are The Same."
                return render(request, "developer_change_pwd.html", {"email": email, "msg": msg})

            try:
                # ✅ Verify the old password
                user = Employee.objects.get(email=email, password=password)
                user.password = new_password
                user.save()

                msg = "Successfully Password Changed."
                return render(request, "developer.html", {"email": email, "msg": msg})

            except Employee.DoesNotExist:
                msg = "Invalid Old Password."
                return render(request, "developer_change_pwd.html", {"email": email, "msg": msg})

        return render(request, "developer_change_pwd.html", {"email": email, "msg": msg})

    else:
        return redirect('/developer')





def developer_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "developer.html", {})

def developer_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "developer_edit_profile.html", {"employ": employ, "role":role})


def developer_update_profile(request):
    email = request.session['email']
    role = request.session["role"]
    data = Employee.objects.get(email=email, role=role)
    if request.method == "POST":
        print("hi1")
        email = request.session["email"]
        print(email)
        emp = Employee.objects.get(email=email, role=role)
        print("hi3")
        employee = EmployeeForm(request.POST, instance=emp)
        print("hi4")
        try:
            if employee.is_valid():
                print("hi6")
                employee.save()
                print("hi")
                return render(request, "developer_home.html", {"msg": "Successfully Update ", "role": role})
        except Exception as e:
            print(e)
            return render(request, "developer_edit_profile.html", {"msg": "Your Details Not Updated", "role":role})
    return render(request, "developer_edit_profile.html", {"employee":data, "role":role})


def analyst_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "analyst_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "analyst_login.html", {"msg": msg})
    return render(request, "analyst_login.html", {})

def analyst_home(request):
    return render(request, "analyst_home.html", {})



#


from django.shortcuts import render, redirect
from .models import Employee

def analyst_change_pwd(request):
    email = request.session.get("email")

    if not email:
        return redirect('/analyst_login')  # Redirect if no username in session

    if not islogin(request):
        return redirect('/analyst_login')

    msg = ""  # Initialize message variable

    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        # ✅ Check if old and new passwords are the same
        if password == new_password:
            msg = "Your Old Password And New Password Are The Same."
            return render(request, "analyst_change_pwd.html", {"email": email, "msg": msg})

        try:
            # ✅ Verify the old password
            user = Employee.objects.get(email=email, password=password)
            user.password = new_password
            user.save()

            msg = "Successfully Password Changed."
            return render(request, "analyst_login.html", {"email": email, "msg": msg})

        except Employee.DoesNotExist:
            msg = "Invalid Old Password."
            return render(request, "analyst_change_pwd.html", {"email": email, "msg": msg})

    return render(request, "analyst_change_pwd.html", {"email": email, "msg": msg})

def analyst_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "analyst_login.html", {})

def analyst_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "analyst_edit_profile.html", {"employ": employ, "role":role})


def analyst_update_profile(request):
    email = request.session['email']
    role = request.session["role"]
    data = Employee.objects.get(email=email, role=role)
    if request.method == "POST":
        print("hi1")
        email = request.session["email"]
        print(email)
        emp = Employee.objects.get(email=email, role=role)
        print("hi3")
        employee = EmployeeForm(request.POST, instance=emp)
        print("hi4")
        try:
            if employee.is_valid():
                print("hi6")
                employee.save()
                print("hi")
                return render(request, "analyst_home.html", {"msg": "Successfully Update ", "role": role})
        except Exception as e:
            print(e)
            return render(request, "analyst_edit_profile.html", {"msg": "Your Details Not Updated", "role":role})
    return render(request, "analyst_edit_profile.html", {"employee":data, "role":role})

def developer_view_projects(request):
    projects = Project.objects.all()
    return render(request, "developer_view_projects.html", {"projects": projects})



def employee_view_projects(request):
    projects = Project.objects.all()
    return render(request, "employee_view_projects.html", {"projects": projects})


def analyst_view_projects(request):
    projects = Project.objects.all()
    return render(request, "analyst_view_projects.html", {"projects": projects})



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import RequirementsForm

def add_requirements(request):
    email = request.session.get('email')  # Use .get() to avoid errors
    projects = Project.objects.all()

    if request.method == "POST":
        requirements = RequirementsForm(request.POST)
        if requirements.is_valid():
            requirements.save()
            messages.success(request, "Thanks For Adding The Requirement")
            return redirect("add_requirements")  # Redirect to prevent form resubmission

    return render(request, "add_requirements.html", {"projects": projects, "email": email})


def analyst_view_requirements(request,id):
    projects = Project.objects.get(id=id)
    requirements = Requirements.objects.filter(projects_id=projects)
    return render(request, "analyst_view_requirements.html", {"requirements": requirements})

def developer_view_requirements(request,id):
    projects = Project.objects.get(id=id)
    requirements = Requirements.objects.filter(projects_id=projects)
    return render(request, "developer_view_requirements.html", {"requirements": requirements})


def employee_view_requirements(request,id):
    projects = Project.objects.get(id=id)
    requirements = Requirements.objects.filter(projects_id=projects)
    return render(request, "employee_view_requirements.html", {"requirements": requirements})

def testcase_bug_piechart(request, id):
    # Get the project object based on ID
    projects = Project.objects.get(pk=id)

    # Count Requirements for the project
    requirements_count = Requirements.objects.filter(projects=projects).count()

    # Filter Testcases with status count
    project_testcases = Testcase.objects.filter(project_name=projects.title)  # Assign the queryset to a variable
    testcases_count = project_testcases.count()

    testcases_by_status = project_testcases.values('status').annotate(count=Count('id'))

    # Initialize test case counts
    testcases_pass_count = 0
    testcases_fail_count = 0
    testcases_new_count = 0

    # Extract counts from queryset
    for testcase in testcases_by_status:
        if testcase['status'] == 'Pass':
            testcases_pass_count = testcase['count']
        elif testcase['status'] == 'Fail':
            testcases_fail_count = testcase['count']
        elif testcase['status'] == 'new':
            testcases_new_count = testcase['count']

    # Filter Bugs using the assigned variable
    bugs = Bug.objects.filter(testcase_id__in=project_testcases.values_list('id', flat=True))
    bugs_count = bugs.count()

    context = {
        'projects': projects,
        'requirements_count': requirements_count,
        'testcases_count':testcases_count,
        'testcases_pass_count': testcases_pass_count,
        'testcases_fail_count': testcases_fail_count,
        'testcases_new_count': testcases_new_count,
        'bugs_count': bugs_count,
    }

    return render(request, "testcase_bug_piechart.html", context)



def developer_view_notifications(request):
    notifications = News.objects.all()
    return render(request, "developer_view_notifications.html", {"notifications": notifications})




def analyst_view_notifications(request):
    notifications = News.objects.all()
    return render(request, "analyst_view_notifications.html", {"notifications": notifications})


def employee_view_notifications(request):
    notifications = News.objects.all()
    return render(request, "employee_view_notifications.html", {"notifications": notifications})


def analyst_bug_piechart(request, id):
    # Get the project object based on ID
    projects = Project.objects.get(pk=id)

    # Count Requirements for the project
    requirements_count = Requirements.objects.filter(projects=projects).count()

    # Filter Testcases with status count
    project_testcases = Testcase.objects.filter(project_name=projects.title)  # Assign the queryset to a variable
    testcases_count = project_testcases.count()

    testcases_by_status = project_testcases.values('status').annotate(count=Count('id'))

    # Initialize test case counts
    testcases_pass_count = 0
    testcases_fail_count = 0
    testcases_new_count = 0

    # Extract counts from queryset
    for testcase in testcases_by_status:
        if testcase['status'] == 'Pass':
            testcases_pass_count = testcase['count']
        elif testcase['status'] == 'Fail':
            testcases_fail_count = testcase['count']
        elif testcase['status'] == 'new':
            testcases_new_count = testcase['count']

    # Filter Bugs using the assigned variable
    bugs = Bug.objects.filter(testcase_id__in=project_testcases.values_list('id', flat=True))
    bugs_count = bugs.count()

    context = {
        'projects': projects,
        'requirements_count': requirements_count,
        'testcases_count':testcases_count,
        'testcases_pass_count': testcases_pass_count,
        'testcases_fail_count': testcases_fail_count,
        'testcases_new_count': testcases_new_count,
        'bugs_count': bugs_count,
    }

    return render(request, "analyst_bug_piechart.html", context)


from django.shortcuts import redirect, render
from django.contrib import messages  # Optional for feedback messages

def employee_update_testcases_status(request, id):
    try:
        testcases = Testcase.objects.get(id=id)
        email = request.session["email"]
        return render(request, "employee_update_testcases_status.html", {
            "testcases": testcases,
            "email": email,
            "id": id
        })
    except Testcase.DoesNotExist:
        messages.error(request, "Testcase not found!")
        return redirect("/view_testcase")


def employee_update_testcases_status_insert(request):
    if request.method == "POST":
        try:
            tested_by_email = request.session.get("email")
            status = request.POST.get('status')
            comments = request.POST.get('comments')
            testcase_id = request.POST.get('id')

            print("Updating testcase with ID:", testcase_id)

            testcases = Testcase.objects.get(id=testcase_id)

            testcases.status = status
            testcases.comments = comments
            testcases.tested_by_email = tested_by_email

            testcases.save()

            print("Update successful for testcase ID:", testcase_id)

            # Optional success message
            messages.success(request, "Testcase status updated successfully!")

            # ✅ Redirect after successful update
            return redirect("/view_testcase")

        except Testcase.DoesNotExist:
            print("Testcase not found!")
            messages.error(request, "Testcase not found!")
            return redirect("/view_testcase")

        except Exception as e:
            print("An error occurred:", e)
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect("/view_testcase")

    # If it's not POST, you can redirect or return an error
    return redirect("/view_testcase")

def employee_bug_piechart(request, id):
    # Get the project object based on ID
    projects = Project.objects.get(pk=id)

    # Count Requirements for the project
    requirements_count = Requirements.objects.filter(projects=projects).count()

    # Filter Testcases with status count
    project_testcases = Testcase.objects.filter(project_name=projects.title)  # Assign the queryset to a variable
    testcases_count = project_testcases.count()

    testcases_by_status = project_testcases.values('status').annotate(count=Count('id'))

    # Initialize test case counts
    testcases_pass_count = 0
    testcases_fail_count = 0
    testcases_new_count = 0

    # Extract counts from queryset
    for testcase in testcases_by_status:
        if testcase['status'] == 'Pass':
            testcases_pass_count = testcase['count']
        elif testcase['status'] == 'Fail':
            testcases_fail_count = testcase['count']
        elif testcase['status'] == 'new':
            testcases_new_count = testcase['count']

    # Filter Bugs using the assigned variable
    bugs = Bug.objects.filter(testcase_id__in=project_testcases.values_list('id', flat=True))
    bugs_count = bugs.count()

    context = {
        'projects': projects,
        'requirements_count': requirements_count,
        'testcases_count':testcases_count,
        'testcases_pass_count': testcases_pass_count,
        'testcases_fail_count': testcases_fail_count,
        'testcases_new_count': testcases_new_count,
        'bugs_count': bugs_count,
    }

    return render(request, "employee_bug_piechart.html", context)



def developer_view_task(request):
    email= request.session["email"]
    if request.method == "GET":
        tasks = Task.objects.filter(employee_email=email)
        return render(request, "developer_view_task.html", {"tasks": tasks})

def employee_view_task(request):
    email= request.session["email"]
    if request.method == "GET":
        tasks = Task.objects.filter(employee_email=email)
        return render(request, "employee_view_task.html", {"tasks": tasks})

def analyst_view_task(request):
    email= request.session["email"]
    if request.method == "GET":
        tasks = Task.objects.filter(employee_email=email)
        return render(request, "analyst_view_task.html", {"tasks": tasks})

def project_view_requirements(request):
    title = request.GET["project_title"]
    print("project ",title)
    projects = Project.objects.filter(title=title)
    requirements = Requirements.objects.filter(projects_id=projects[0].id)
    req_list = []
    for req in requirements:
        req_list.append(req.title)
    print(req_list)
    return JsonResponse(req_list,safe=False)



def developer_task_update_status(request, id):
    if request.method == "GET":
        try:
            tasks = Task.objects.get(id=id)
            return render(request, "developer_task_update_status.html", {"tasks": tasks, "id": id})
        except Task.DoesNotExist:
            return redirect("/developer_view_task")
    else:
        return redirect("/developer_view_task")  # ✅ Redirect on wrong request method



from django.shortcuts import redirect  # make sure you import this

def developer_task_status_insert(request):
    if request.method == "POST":
        try:
            # tested_by_email = request.session["email"]
            status = request.POST['status']
            id = request.POST['id']

            print("hi1")
            print("hi2")

            task = Task.objects.get(id=id)

            print("hi3")

            task.status = status
            # task.tested_by_email = tested_by_email

            print("hi4")

            task.save()

            print("✅ Task updated successfully!")

            # ✅ Redirect after successful update
            return redirect("/developer_view_task")

        except Exception as e:
            print(f"❌ Error: {e}")

            # ✅ Redirect even if there’s an error (or you can pass error info)
            return redirect("/developer_view_task")

    # If not POST, redirect to view_task as a fallback
    return redirect("/developer_view_task")



def tester_task_update_status(request, id):
    if request.method == "GET":
        try:
            tasks = Task.objects.get(id=id)
            return render(request, "tester_task_update_status.html", {"tasks": tasks, "id": id})
        except Task.DoesNotExist:
            return redirect("/employee_view_task")
    else:
        return redirect("/employee_view_task")  # ✅ Redirect on wrong request method



from django.shortcuts import redirect  # make sure you import this

def tester_task_status_insert(request):
    if request.method == "POST":
        try:
            # tested_by_email = request.session["email"]
            status = request.POST['status']
            id = request.POST['id']

            print("hi1")
            print("hi2")

            task = Task.objects.get(id=id)

            print("hi3")

            task.status = status
            # task.tested_by_email = tested_by_email

            print("hi4")

            task.save()

            print("✅ Task updated successfully!")

            # ✅ Redirect after successful update
            return redirect("/employee_view_task")

        except Exception as e:
            print(f"❌ Error: {e}")

            # ✅ Redirect even if there’s an error (or you can pass error info)
            return redirect("/employee_view_task")

    # If not POST, redirect to view_task as a fallback
    return redirect("/employee_view_task")



from django.shortcuts import render, get_object_or_404
from .models import Testcase  # Replace with your actual model name

def view_testcase_details(request, testcase_id):
    testcase = get_object_or_404(Testcase, id=testcase_id)
    context = {'testcase': testcase}
    return render(request, 'view_testcase_details.html', context)


