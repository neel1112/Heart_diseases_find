from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
import datetime

from sklearn.ensemble import GradientBoostingClassifier

from .forms import DoctorForm
from .models import *
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, time as dt_time
from django.contrib.auth import authenticate, login, logout
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'carousel.html')

def Admin_Home(request):
    dis = Search_Data.objects.all()
    pat = Patient.objects.all()
    doc = Doctor.objects.all()
    feed = Feedback.objects.all()

    d = {'dis':dis.count(),'pat':pat.count(),'doc':doc.count(),'feed':feed.count()}
    return render(request,'admin_home.html',d)

@login_required(login_url="login")
def assign_status(request,pid):
    doctor = Doctor.objects.get(id=pid)
    if doctor.status == 1:
        doctor.status = 2
        messages.success(request, 'Selected doctor are successfully withdraw his approval.')
    else:
        doctor.status = 1
        messages.success(request, 'Selected doctor are successfully approved.')
    doctor.save()
    return redirect('view_doctor')

@login_required(login_url="login")
def User_Home(request):
    return render(request,'patient_home.html')

@login_required(login_url="login")
def Doctor_Home(request):
    return render(request,'doctor_home.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')


def Gallery(request):
    return render(request,'gallery.html')


def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        sign = ""
        if user:
            try:
                sign = Patient.objects.get(user=user)
            except:
                pass
            if sign:
                login(request, user)
                error = "pat1"
            else:
                pure=False
                try:
                    pure = Doctor.objects.get(status=1,user=user)
                except:
                    pass
                if pure:
                    login(request, user)
                    error = "pat2"
                else:
                    login(request, user)
                    error="notmember"
        else:
            error="not"
    d = {'error': error}
    return render(request, 'login.html', d)

def Login_admin(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get('uname', '')
        p = request.POST.get('pwd', '')
        user = authenticate(username=u, password=p)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home')  # Redirect to admin home on success
            else:
                error = "You don't have admin privileges."
        else:
            error = "Invalid username or password."
            
        messages.error(request, error)  # Add error message to display to user
        
    return render(request, 'admin_login.html', {'error': error})

def Signup_User(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        d = request.POST['dob']
        con = request.POST['contact']
        add = request.POST['add']
        type = request.POST['type']
        im = request.FILES['image']
        dat = datetime.date.today()
        user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
        if type == "Patient":
            Patient.objects.create(user=user,contact=con,address=add,image=im,dob=d)
        else:
            Doctor.objects.create(dob=d,image=im,user=user,contact=con,address=add,status=2)
        error = "create"
    d = {'error':error}
    return render(request,'register.html',d)

def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
def Change_Password(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    if not request.user.is_staff:
        try:
            sign = Patient.objects.get(user=user)
            if sign:
                error = "pat"
        except:
            sign = Doctor.objects.get(user=user)
    terror = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            terror = "yes"
        else:
            terror = "not"
    d = {'error':error,'terror':terror,'data':sign}
    return render(request,'change_password.html',d)


def preprocess_inputs(df, scaler):
    df = df.copy()
    # Split df into X and y
    y = df['target'].copy()
    X = df.drop('target', axis=1).copy()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    return X, y


def prdict_heart_disease(list_data):
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)

    X = df[['age','sex','cp',  'trestbps',  'chol',  'fbs',  'restecg',  'thalach',  'exang',  'oldpeak',  'slope',  'ca',  'thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    nn_model = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1, random_state=0)
    nn_model.fit(X_train, y_train)
    pred = nn_model.predict([list_data])
    print("Neural Network Accuracy: {:.2f}%".format(nn_model.score(X_test, y_test) * 100))
    print("Prdicted Value is : ", format(pred))
    dataframe = str(df.head())
    return (nn_model.score(X_test, y_test) * 100),(pred)

@login_required(login_url="login")
def add_doctor(request,pid=None):
    doctor = None
    if pid:
        doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance = doctor)
        if form.is_valid():
            new_doc = form.save()
            new_doc.status = 1
            if not pid:
                user = User.objects.create_user(password=request.POST['password'], username=request.POST['username'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                new_doc.user = user
            new_doc.save()
            return redirect('view_doctor')
    d = {"doctor": doctor}
    return render(request, 'add_doctor.html', d)

@login_required(login_url="login")
def add_heartdetail(request):
    if request.method == "POST":
        try:
            # Get form data and convert to appropriate types
            age = int(request.POST.get('age', 0))
            sex = int(request.POST.get('sex', 0))
            cp = int(request.POST.get('cp', 0))
            trestbps = int(request.POST.get('trestbps', 0))
            chol = int(request.POST.get('chole', 0))  # Note: form field is 'chole' but model expects 'chol'
            fbs = int(request.POST.get('fbs', 0))
            restecg = int(request.POST.get('restecg', 0))
            thalach = int(request.POST.get('thalach', 0))
            exang = int(request.POST.get('exang', 0))
            oldpeak = float(request.POST.get('old_peak', 0.0))
            slope = int(request.POST.get('slope', 0))
            ca = int(request.POST.get('ca', 0))
            thal = int(request.POST.get('thal', 0))
            
            # Create list in the exact order expected by the model
            list_data = [
                age, sex, cp, trestbps, chol, fbs, restecg, 
                thalach, exang, oldpeak, slope, ca, thal
            ]
            
            # Make prediction
            accuracy, pred = prdict_heart_disease(list_data)
            
            # Save prediction
            patient = Patient.objects.get(user=request.user)
            Search_Data.objects.create(
                patient=patient, 
                prediction_accuracy=accuracy, 
                result=pred[0], 
                values_list=list_data
            )
            
            # Prepare result message
            if pred[0] == 0:
                pred_msg = "<span style='color:green'>You are healthy</span>"
            else:
                pred_msg = "<span style='color:red'>You are Unhealthy, Need to Checkup.</span>"
            
            # Redirect to prediction result page
            return redirect('predict_desease', str(pred[0]), str(accuracy))
            
        except Exception as e:
            print(f"Error in add_heartdetail: {str(e)}")
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('add_heartdetail')
            
    return render(request, 'add_heartdetail.html')

@login_required(login_url="login")
def predict_desease(request, pred, accuracy):
    # Ensure pred is a string for template comparison
    pred = str(pred)
    
    # Get all active doctors by default
    doctor = Doctor.objects.filter(status=1)
    
    try:
        # Try to get the patient's address for location-based matching
        patient = Patient.objects.get(user=request.user)
        if patient.address:
            # Use the first part of the address for matching if available
            address_part = patient.address.split(',')[0].strip()
            if address_part:
                doctor = doctor.filter(address__icontains=address_part)
    except (Patient.DoesNotExist, Exception) as e:
        # If any error occurs, just use all active doctors
        print(f"Note in predict_desease: {str(e)}")
    
    # Convert pred to string for template comparison
    prediction_result = pred != "0"
    
    d = {
        'pred': pred, 
        'accuracy': accuracy, 
        'doctor': doctor,
        'show_doctors': prediction_result  # Explicit flag for template
    }
    return render(request, 'predict_disease.html', d)

@login_required(login_url="login")
def view_search_pat(request):
    doc = None
    try:
        doc = Doctor.objects.get(user=request.user)
        data = Search_Data.objects.filter(patient__address__icontains=doc.address).order_by('-id')
    except:
        try:
            doc = Patient.objects.get(user=request.user)
            data = Search_Data.objects.filter(patient=doc).order_by('-id')
        except:
            data = Search_Data.objects.all().order_by('-id')
    return render(request,'view_search_pat.html',{'data':data})

@login_required(login_url="login")
def delete_doctor(request,pid):
    doc = Doctor.objects.get(id=pid)
    doc.delete()
    return redirect('view_doctor')

@login_required(login_url="login")
def delete_feedback(request,pid):
    doc = Feedback.objects.get(id=pid)
    doc.delete()
    return redirect('view_feedback')

@login_required(login_url="login")
def delete_patient(request,pid):
    doc = Patient.objects.get(id=pid)
    doc.delete()
    return redirect('view_patient')

@login_required(login_url="login")
def delete_searched(request,pid):
    doc = Search_Data.objects.get(id=pid)
    doc.delete()
    return redirect('view_search_pat')

@login_required(login_url="login")
def View_Doctor(request):
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

@login_required(login_url="login")
def View_Patient(request):
    patient = Patient.objects.all()
    d = {'patient':patient}
    return render(request,'view_patient.html',d)

@login_required(login_url="login")
def View_Feedback(request):
    dis = Feedback.objects.all()
    d = {'dis':dis}
    return render(request,'view_feedback.html',d)

@login_required(login_url="login")
def View_My_Detail(request):
    terror = ""
    user = User.objects.get(id=request.user.id)
    error = ""
    try:
        sign = Patient.objects.get(user=user)
        error = "pat"
    except:
        sign = Doctor.objects.get(user=user)
    d = {'error': error,'pro':sign}
    return render(request,'profile_doctor.html',d)

@login_required(login_url="login")
def Edit_Doctor(request,pid):
    doc = Doctor.objects.get(id=pid)
    error = ""
    # type = Type.objects.all()
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        add = request.POST['add']
        cat = request.POST['type']
        try:
            im = request.FILES['image']
            doc.image=im
            doc.save()
        except:
            pass
        dat = datetime.date.today()
        doc.user.first_name = f
        doc.user.last_name = l
        doc.user.email = e
        doc.contact = con
        doc.category = cat
        doc.address = add
        doc.user.save()
        doc.save()
        error = "create"
    d = {'error':error,'doc':doc,'type':type}
    return render(request,'edit_doctor.html',d)

@login_required(login_url="login")
def Edit_My_deatail(request):
    terror = ""
    error = None
    user = request.user
    
    # Determine if the user is a doctor or patient
    try:
        profile = Doctor.objects.get(user=user)
        error = "doc"  # Not a patient
    except Doctor.DoesNotExist:
        try:
            profile = Patient.objects.get(user=user)
            error = "pat"  # Is a patient
        except Patient.DoesNotExist:
            # Handle case where user has no profile
            messages.error(request, "Profile not found.")
            return redirect('profile_doctor')
    
    if request.method == 'POST':
        f = request.POST.get('fname', user.first_name)
        l = request.POST.get('lname', user.last_name)
        e = request.POST.get('email', user.email)
        con = request.POST.get('contact', profile.contact)
        add = request.POST.get('add', profile.address)
        
        # Handle file upload
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
        
        # Update user fields
        user.first_name = f
        user.last_name = l
        user.email = e
        
        # Update profile fields
        profile.contact = con
        profile.address = add
        
        # Update doctor-specific fields if user is a doctor
        if error == "doc":
            cat = request.POST.get('type', getattr(profile, 'category', ''))
            profile.category = cat
        
        # Save changes
        user.save()
        profile.save()
        terror = "create"
        
        if terror == "create":
            return redirect('profile_doctor')
    
    d = {'error': error, 'terror': terror, 'pro': profile}
    return render(request, 'edit_profile.html', d)

@login_required(login_url='login')
def sent_feedback(request):
    terror = None
    if request.method == 'POST':
        try:
            message = request.POST.get('msg', '').strip()
            if not message:
                messages.error(request, 'Please enter your feedback message.')
            else:
                Feedback.objects.create(user=request.user, messages=message)
                messages.success(request, 'Thank you for your feedback!')
                return redirect('sent_feedback')
        except Exception as e:
            messages.error(request, f'Error submitting feedback: {str(e)}')
    
    return render(request, 'sent_feedback.html', {'terror': terror})

@login_required(login_url='login')
def cancel_appointment(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id, patient=request.user)
        if appointment.status == 'pending':
            appointment.status = 'cancelled'
            appointment.save()
            messages.success(request, 'Appointment has been cancelled successfully.')
        else:
            messages.warning(request, 'Only pending appointments can be cancelled.')
    except Appointment.DoesNotExist:
        messages.error(request, 'Appointment not found or you do not have permission to cancel it.')
    
    return HttpResponseRedirect(reverse('view_appointments'))

@login_required(login_url='login')
def view_appointments(request):
    # Get all appointments for the logged-in patient, ordered by date and time
    appointments = Appointment.objects.filter(patient=request.user).order_by('appointment_date', 'appointment_time')
    return render(request, 'view_appointments.html', {'appointments': appointments})

@login_required(login_url="login")
def book_appointment(request):
    doctors = Doctor.objects.all()
    
    if request.method == 'POST':
        try:
            # Get form data
            doctor_id = request.POST.get('doctor')
            appointment_date = request.POST.get('date')
            appointment_time = request.POST.get('time')
            symptoms = request.POST.get('symptoms')
            
            # Validate data
            if not all([doctor_id, appointment_date, appointment_time, symptoms]):
                messages.error(request, 'All fields are required.')
                return render(request, 'book_appointment.html', {'doctors': doctors})
            
            # Convert date and time strings to proper format
            try:
                appointment_datetime = datetime.strptime(
                    f"{appointment_date} {appointment_time}", 
                    "%Y-%m-%d %H:%M"
                )
            except ValueError:
                messages.error(request, 'Invalid date or time format.')
                return render(request, 'book_appointment.html', {'doctors': doctors})
            
            # Check if the selected time is in the future
            if appointment_datetime < timezone.now():
                messages.error(request, 'Appointment date and time must be in the future.')
                return render(request, 'book_appointment.html', {'doctors': doctors})
            
            # Get doctor instance
            try:
                doctor = Doctor.objects.get(id=doctor_id)
            except Doctor.DoesNotExist:
                messages.error(request, 'Selected doctor does not exist.')
                return render(request, 'book_appointment.html', {'doctors': doctors})
            
            # Check for existing appointment at the same time
            existing_appointment = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                status__in=['pending', 'confirmed']
            ).exists()
            
            if existing_appointment:
                messages.warning(request, 'The selected time slot is already booked. Please choose another time.')
                return render(request, 'book_appointment.html', {'doctors': doctors})
            
            # Create the appointment
            appointment = Appointment.objects.create(
                patient=request.user,
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                symptoms=symptoms,
                status='pending'
            )
            
            # Send confirmation email (to be implemented)
            # send_appointment_confirmation_email(request.user, appointment)
            
            messages.success(request, 'Your appointment has been booked successfully!')
            return redirect('patient_home')
            
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'book_appointment.html', {'doctors': doctors})
    
    # GET request - show the form
    return render(request, 'book_appointment.html', {'doctors': doctors})
