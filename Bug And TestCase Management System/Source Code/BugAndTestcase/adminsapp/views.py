from django.shortcuts import render, redirect
from adminsapp.models import Admins
from adminsapp.models import Employee
from adminsapp.forms import EmployeeForm
from adminsapp.models import Project
from adminsapp.forms import ProjectForm
from employeeapp.models import Bug, Testcase, Requirements
from employeeapp.forms import BugForm, TestcaseForm
from adminsapp.models import News
from adminsapp.forms import NewsForm
from django.db.models import Count


# Create your views here.

def admins(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        request.session["username"] = username
        try:
            admin = Admins.objects.get(username=username, password=password)

            msg = "Data Found"
            print("msg")
            return render(request, "admins_home.html", {"admin": admin, "msg": msg})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "admins.html", {"msg": msg})
    return render(request, "admins.html", {})


def admins_home(request):
    return render(request, "admins_home.html", {})


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Admins

def admins_change_pwd(request):
    username = request.session.get("username")

    if not username:
        return redirect('/admins')  # Redirect if no username in session

    if islogin(request):
        if request.method == 'POST':
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')

            # ✅ Check if old and new passwords are the same
            if password == new_password:
                msg = "Your Old Password And New Password Are The Same."
                messages.error(request, msg)
                return render(request, "admins_chpwd.html", {"username": username, "msg": msg})

            try:
                # ✅ Verify the old password
                user = Admins.objects.get(username=username, password=password)
                user.password = new_password
                user.save()

                msg = "Successfully Password Changed."
                messages.success(request, msg)
                return redirect('/admins')

            except Admins.DoesNotExist:
                msg = "Invalid Old Password."
                messages.error(request, msg)
                return render(request, "admins_chpwd.html", {"username": username, "msg": msg})

        return render(request, "admins_chpwd.html", {"username": username})

    return redirect('/admins')



def admins_logout(request):
    request.session["username"] = ""
    del request.session["username"]
    return render(request, "admins.html", {})


def islogin(request):
    if request.session.__contains__("username"):
        return True
    else:
        return False



from django.contrib import messages
from django.db import IntegrityError


# def add_employee(request):
#     if request.method == "POST":
#         print("hi")
#         employee_form = EmployeeForm(request.POST)
#         print("hi1")
#
#         try:
#             if employee_form.is_valid():
#                 print("hi2")
#
#                 # 🔥 Get the cleaned data
#                 empid = employee_form.cleaned_data.get("empid")
#                 email = employee_form.cleaned_data.get("email")
#
#                 # 🔥 Check if Employee ID exists
#                 if Employee.objects.filter(empid=empid).exists():
#                     messages.error(request, "Employee ID already exists! Please use a different ID.")
#
#                 # 🔥 Check if Email exists
#                 elif Employee.objects.filter(email=email).exists():
#                     messages.error(request, "Email already exists! Please use a different email.")
#
#                 # 🔥 If no duplicates, add the employee
#                 else:
#                     employee_form.save()
#                     messages.success(request, "Employee added successfully!")
#                     return redirect("/view_employee")
#
#         except IntegrityError as e:
#             messages.error(request, "A database error occurred. Please try again!")
#             print("Integrity Error:", e)
#
#         except Exception as e:
#             messages.error(request, "An error occurred. Please try again!")
#             print("Exception:", e)
#
#     return render(request, "add_employee.html", {"form": EmployeeForm()})
#
#
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .forms import EmployeeForm
from .models import Employee


def add_employee(request):
    msg = ""
    if request.method == "POST":
        print("hi")
        employee_form = EmployeeForm(request.POST)
        print("hi1")

        try:
            if employee_form.is_valid():
                print("hi2")

                empid = employee_form.cleaned_data.get("empid")
                email = employee_form.cleaned_data.get("email")

                if Employee.objects.filter(empid=empid).exists():
                    msg = "Employee ID already exists! Please use a different ID."
                    messages.error(request, msg)
                elif Employee.objects.filter(email=email).exists():
                    msg = "Email already exists! Please use a different email."
                    messages.error(request, msg)
                else:
                    employee_form.save()
                    msg = "Employee added successfully!"
                    messages.success(request, msg)
                    return redirect("/view_employee")

        except IntegrityError as e:
            msg = "A database error occurred. Please try again!"
            messages.error(request, msg)
            print("Integrity Error:", e)

        except Exception as e:
            msg = "An error occurred. Please try again!"
            messages.error(request, msg)
            print("Exception:", e)

    return render(request, "add_employee.html", {"form": EmployeeForm(), "msg": msg})


def view_employee(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
    return render(request, "view_employee.html", {"employee": employee})


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/view_employee")


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit_employee.html", {"employee": employee})


def update_employee(request):
    if request.method == "POST":
        print("h")
        userid = request.POST["id"]
        print("hi")
        employee = Employee.objects.get(id=userid)
        print("HI")
        employee = EmployeeForm(request.POST, instance=employee)
        print("hii")
        if employee.is_valid():
            print("hiii")
            employee.save()
            print("hiiiii")
        return redirect("/view_employee")
    return redirect("/view_employee")


def add_project(request):
    managers = Employee.objects.filter(role="manager")
    return render(request, "add_project.html", {"managers": managers})


def add_new_project(request):
    if request.method == "POST":
        project = ProjectForm(request.POST)
        try:
            if project.is_valid():
                print("hi2")
                project.save()
                print("h3")
                return redirect("/view_project")
                # return render(request, "admins_home.html", {})
        except Exception as e:
            print(e)
            return render(request, "add_project.html", {})
    return render(request, "add_project.html", {})


def view_project(request):
    if request.method == 'GET':
        projects = Project.objects.all()
    return render(request, "view_project.html", {"projects": projects})


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("/view_project")


def edit_project(request, id):
    project = Project.objects.get(id=id)
    managers = Employee.objects.filter(role="manager")
    return render(request, "edit_project.html", {"project": project, "managers": managers})

from django.contrib import messages

def update_project(request):
    if request.method == "POST":
        userid = request.POST["id"]

        try:
            project = Project.objects.get(id=userid)
        except Project.DoesNotExist:
            messages.error(request, "Project not found!")
            return redirect("/view_project")

        project.title = request.POST.get("title")
        project.code = request.POST.get("code")
        project.technology = request.POST.get("technology")
        project.domain = request.POST.get("domain")
        project.description = request.POST.get("description")
        project.fromdate = request.POST.get("fromdate")
        project.todate = request.POST.get("todate")
        project.manager = request.POST.get("manager")

        project.save()
        return redirect("/view_project")
        # messages.success(request, "Project updated successfully")





def view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
    return render(request, "view_testcases.html", {"testcases": testcases})


def view_bugs(request):
    if request.method == "GET":
        bugs = Bug.objects.all()
    return render(request, "view_bugs.html", {"bugs": bugs})


def add_news(request):
    if request.method == "POST":
        news = NewsForm(request.POST)
        if news.is_valid():
            news.save()
            return redirect("/view_news")
        # return render(request, "add_news.html", {"msg": "Success"})
    return render(request, "add_news.html", {})


def view_news(request):
    if request.method == "GET":
        news = News.objects.all()
    return render(request, "view_news.html", {"news": news})

def delete_news(request,id):
    news=News.objects.get(id=id)
    news.delete()
    return redirect("/view_news")

def edit_news(request, id):
    news = News.objects.get(id=id)
    return render(request, "edit_news.html", {"news": news})


def update_news(request):
    if request.method == "POST":
        userid = request.POST["id"]
        news = News.objects.get(id=userid)
        news = NewsForm(request.POST, instance=news)
        if news.is_valid():
            news.save()
        return redirect("/view_news")
    return redirect("/view_news")


def admin_bug_piechart(request, id):
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

    return render(request, "admin_bug_piechart.html", context)

