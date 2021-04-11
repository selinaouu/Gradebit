from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

#Selina Ou
#Brings user to the splashpage
def home(request):
    return render(request, 'index.html')

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#Filters for the id of the student object and then displays the tasks, units, and final grade/comments of the specific student on the evidence record
@login_required(login_url='signup')
def gradebook(request,pk_test):
    studentgrades=Studentgrades.objects.get(id=pk_test)
    evidencerec=studentgrades.evidencerec_set.all()
    category=studentgrades.category_set.all()
    additional=studentgrades.additional_set.all()

    context={'studentgrades':studentgrades,'evidencerecs':evidencerec,'categories':category,'additionals':additional}
    return render(request, 'gradebook.html', context)

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function gets the data from the student form and if the form is valid it will save the data to the user that is currently logged in
@login_required(login_url='signup')
def student_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form= StudentForm()
        else:
            student=Student.objects.get(pk=id)
            form= StudentForm(instance=student)
        return render(request, 'student_form.html',{'form':form})
    else:
        if id ==0:
            form= StudentForm(request.POST)
        else:
            student=Student.objects.get(pk=id)
            form=StudentForm(request.POST,instance=student)

        if form.is_valid():
            u=form.save()
            users = Student.objects.filter(user= request.user)
            request.user.new_spending.add(u) 

        return render(request, 'student_list.html', {'users': users})

#Selina Ou
#this function will only be avaliable to the user if they are logged in
@login_required(login_url='signup')
def student_list(request):
    users = Student.objects.filter(user= request.user)# This function first filters for the user that is currently logged in and it displays the students that the user has entered on the students page
    return render(request, 'student_list.html',{'users': users})

#Selina Ou
#this function will only be avaliable to the user if they are logged in
@login_required(login_url='signup')
def student_delete(request,id):
    student=Student.objects.filter(pk=id)#This function will first filter for the id of the student(when the user creates a student, the student has an id connected to the student) and then delete the row of the student data that has the id
    student.delete()
    return redirect('student_list')

#Selina Ou
#This function is the signin function that will allow the users to signin
#This function displays the signin page with the signin form 
def signin(request):
    # From the signin form, it will take the data entered in the username and password fields
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)#and then authenticate them,

        if user is not None:
            auth.login(request,user)
            redirect_url=request.GET.get('next','task_list')#if the user exists, it will redirect them to their 'task_list' which is also their dashboard
            return redirect(redirect_url)
        else:
            #However, if any of the credentials are invalid or if the user doesnt yet have an account, it wont let the user signin and will actually refresh the page for the user and give the user an error message
            messages.info(request, 'invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

#Selina Ou
#This function is the signin function that will allow the users to signin
#This function displays the signup page with the signup form 
def signup(request):
    # From the signin form, it will take the data entered in the email, username, password1, and password2 fields and error check these fields.
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        # if the first password matches the 2nd password entered it will filter through the users objects and check whether the username already exists, if so the user will receive and error message; the same conecept applies to the email
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is unavaliable')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already taken ')
                return redirect('signup')
            else:
                user=User.objects.create_user(email=email, username=username,password=password1)# However, if it passes it will create an user object with the email, username, and password
                user.save();
                print('user created')
        else:
            messages.info(request,"Passwords do not match")
            return redirect('signup')
        return redirect('/')

    else:
        return render(request, 'signup.html')

#Ally Tan
#this function will only be avaliable to the user if they are logged in
@login_required(login_url='signup')
def task_list(request):
    users = Task.objects.filter(user= request.user)# This function first filters for the user that is currently logged in and it displays the tasks that the user has entered on the dashboard page
    return render(request,"task_list.html", {'users': users})

#Ally Tan
#this function will only be avaliable to the user if they are logged in
#this function gets the data from the task form and if the form is valid it will save the data to the user that is currently logged in(insert it)
@login_required(login_url='signup')
def task_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form = TaskForm()
        else:
            task = Task.objects.get(pk=id)
            form = TaskForm(instance=task)
        return  render(request,"task_form.html", {'form':form})
    else: 
        if id == 0:
            form = TaskForm(request.POST)
        else:
             task = Task.objects.get(pk=id)
             form = TaskForm(request.POST,instance=task)
        if form.is_valid():
             t=form.save()
             users = Task.objects.filter(user= request.user)
             request.user.new_task.add(t) 

        return  render(request,"task_list.html", {'users': users})

#Ally Tan
#this function will only be avaliable to the user if they are logged in
@login_required(login_url='signup')
def task_delete(request,id):
    task = Task.objects.get(pk=id)#This function will first filter for the id of the task(when the user creates a task, the task has an id connected to it) and then delete the row of the task data that has the id
    task.delete()
    return redirect('task_list')

#Selina Ou
#This function logs the user out 
def logout(request):
    auth.logout(request)
    return redirect('/')

#Selina Ou
#This function displays the studengrades_list on the website
@login_required(login_url='signup')
def studentgrades_list(request):
    users = Studentgrades.objects.filter(user= request.user)#Filters for the user and from the user it finds the studentgrades objects saved to that user and displays it
    return render(request, 'studentgrades_list.html', {'users': users})


#Selina Ou
#this function gets the data from the studentgrades form and if the form is valid it will save the data to the user that is currently logged in(insert it)
@login_required(login_url='signup')
def studentgrades_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Studentgradesform()
        else:
            studentgrades = Studentgrades.objects.get(pk=id)
            form = Studentgradesform(instance=studentgrades)
        return render(request, "studentgrades_form.html", {'form': form})
    else:
        if id == 0:
            form = Studentgradesform(request.POST)
        else:
            studentgrades = Studentgrades.objects.get(pk=id)
            form =Studentgradesform(request.POST,instance= studentgrades)
        if form.is_valid():
            sg=form.save()
            users = Studentgrades.objects.filter(user= request.user)
            request.user.new_studentgrades.add(sg) 
        return render(request, 'studentgrades_list.html', {'users': users})

#Selina Ou
#this function will only be avaliable to the user if they are logged in
@login_required(login_url='signup')
def studentgrades_delete(request,id):
    studentgrades = Studentgrades.objects.get(pk=id)#This function will first filter for the id of the task(when the user creates a task, the task has an id connected to it) and then delete the row of the task data that has the id
    studentgrades.delete()
    return redirect('studentgrades_list')

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function will create tasks in the evidence record and display the form to create tasks
@login_required(login_url='signup')
def create_evidencerecord(request,pk):
    studentgrades=Studentgrades.objects.get(id=pk)
    form= EviForm(initial={'studentgrades':studentgrades})
    if request.method =="POST":
        form= EviForm(request.POST,instance=studentgrades)
        if form.is_valid():
            form.save()
            return redirect('studentgrades_list')
    context={'form':form}
    return render(request,'evi_form.html',context)

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function updates the task in the evidence record and displays the form with the pre-entered data
@login_required(login_url='signup')
def update_evidencerecord(request,pk):
    evidencerec= EvidenceRec.objects.get(id=pk)
    form=EviForm(instance=evidencerec)
    if request.method=='POST':
        form=EviForm(request.POST,instance=evidencerec)
        if form.is_valid():
            form.save()
            return redirect ('studentgrades_list')

    context={'form':form}
    return render(request,'evi_form.html',context)

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function deletes the task in the evidence record
@login_required(login_url='signup')
def delete_evidencerecord(request,pk):
    evidencerec= EvidenceRec.objects.get(id=pk)
    if request.method == "POST":
        evidencerec.delete()
        return redirect ('studentgrades_list')

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function will create units in the evidence record and display the form to create units
@login_required(login_url='signup')
def create_category(request,pk):
    studentgrades=Studentgrades.objects.get(id=pk)
    form= CategoryForm(initial={'studentgrades':studentgrades})
    if request.method =="POST":
        form= CategoryForm(request.POST,instance=studentgrades)
        if form.is_valid():
            form.save()
            return redirect('studentgrades_list')
    context={'form':form}
    return render(request,'category_form.html',context)

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function deletes the unit in the evidence record
@login_required(login_url='signup')
def delete_category(request,pk):
    category= Category.objects.get(id=pk)
    if request.method == "POST":
        category.delete()
        return redirect ('studentgrades_list')

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function will create additional(comments+final mark) in the evidence record and display the form to create additional (final mark/comments)
@login_required(login_url='signup')
def create_additional(request,pk):
    studentgrades=Studentgrades.objects.get(id=pk)
    form= Additionalform(initial={'studentgrades':studentgrades})
    if request.method =="POST":
        form= Additionalform(initial={'studentgrades':studentgrades})
        if form.is_valid():
            form.save()
            return redirect('studentgrades_list')
    context={'form':form}
    return render(request,'additional_form.html',context)

#Selina Ou
#this function will only be avaliable to the user if they are logged in
#this function deletes the additional in the evidence record
@login_required(login_url='signup')
def delete_additional(request,pk):
    additional= Additional.objects.get(id=pk)
    if request.method == "POST":
        additional.delete()
        return redirect ('studentgrades_list')
