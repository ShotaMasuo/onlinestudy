from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import User, Subject
from .models import WorkModel, ReserveModel
from datetime import date, timedelta, datetime
from django.core.mail import send_mail

# Create your views here.
today = date.today()
yesterday = today - timedelta(days=1)

@login_required
def listfunc(request):
    teacher_list = []
    reserveinfo = ReserveModel.objects.filter(reservedate=today)
    delete_data = WorkModel.objects.filter(workdate__lte=yesterday)
    delete_data.delete()
    user = request.user
    username = request.user.get_full_name()
    stuortea = request.user.role
    newtoday = today
    teachers = User.objects.filter(role=1)
    students = User.objects.filter(role=2)
    teachers = teachers.filter(workmodel__workdate=today)
    reserveinfoteacher = reserveinfo.filter(teacher=request.user)
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    r5 = ''
    r6 = ''
    r7 = ''
    r8 = ''
    for teacher in teachers:
        if teacher not in teacher_list:
            teacher_list.append(teacher)
    for r in reserveinfo:
        if r.reservetime == 'c1':
            r1 += str(r.teacher.email) + ','
        elif r.reservetime == 'c2':
            r2 += str(r.teacher.email) + ','
        elif r.reservetime == 'c3':
            r3 += str(r.teacher.email) + ','
        elif r.reservetime == 'c4':
            r4 += str(r.teacher.email) + ','
        elif r.reservetime == 'c5':
            r5 += str(r.teacher.email) + ','
        elif r.reservetime == 'c6':
            r6 += str(r.teacher.email) + ','
        elif r.reservetime == 'c7':
            r7 += str(r.teacher.email) + ','
        elif r.reservetime == 'c8':
            r8 += str(r.teacher.email) + ','
    counter = 0
    print(user.id)
    # 教師
    if stuortea == 1:
        return render(request, 'list_teacher.html', {
            'username': username, 
            'teachers': teachers,
            'students': students,
            'newtoday': newtoday,
            'today': today,
            'counter': counter,
            'teacher_list': teacher_list,
            'reserveinfoteacher': reserveinfoteacher,
            'user': user,
            'reserveinfo': reserveinfo,
            })
    # 生徒
    else:
        return render(request, 'list_student.html', {
            'username': username, 
            'teachers': teachers,
            'students': students,
            'newtoday': newtoday,
            'today': today,
            'counter': counter,
            'teacher_list': teacher_list,
            'r1':r1, 'r2':r2,'r3':r3,'r4':r4,'r5':r5,'r6':r6,'r7':r7,'r8':r8,
            'user': user,
            'reserveinfo': reserveinfo,
            })

def prevlistfunc(request, counter):
    stuortea = request.user.role
    teacher_list = []
    username = request.user.get_full_name()
    teachers = User.objects.filter(role=1)
    counter -= 1
    todaycalc = timedelta(days=counter)
    newtoday = today + todaycalc
    teachers = teachers.filter(workmodel__workdate=newtoday)
    reserveinfo = ReserveModel.objects.filter(reservedate=newtoday)
    reserveinfoteacher = reserveinfo.filter(teacher=request.user)
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    r5 = ''
    r6 = ''
    r7 = ''
    r8 = ''
    for teacher in teachers:
        if teacher not in teacher_list:
            teacher_list.append(teacher)
    for r in reserveinfo:
        if r.reservetime == 'c1':
            r1 += str(r.teacher.email) + ','
        elif r.reservetime == 'c2':
            r2 += str(r.teacher.email) + ','
        elif r.reservetime == 'c3':
            r3 += str(r.teacher.email) + ','
        elif r.reservetime == 'c4':
            r4 += str(r.teacher.email) + ','
        elif r.reservetime == 'c5':
            r5 += str(r.teacher.email) + ','
        elif r.reservetime == 'c6':
            r6 += str(r.teacher.email) + ','
        elif r.reservetime == 'c7':
            r7 += str(r.teacher.email) + ','
        elif r.reservetime == 'c8':
            r8 += str(r.teacher.email) + ','
    # 教師
    if stuortea == 1:
        return render(request, 'list_teacher.html', {
                'username': username, 
                'teachers': teachers,
                'newtoday': newtoday,
                'today': today,
                'counter': counter,
                'teacher_list': teacher_list,
                'r1':r1, 'r2':r2,'r3':r3,'r4':r4,'r5':r5,'r6':r6,'r7':r7,'r8':r8,
                'reserveinfoteacher': reserveinfoteacher,
                })
    # 生徒
    else:
        return render(request, 'list_student.html', {
                'username': username, 
                'teachers': teachers,
                'newtoday': newtoday,
                'today': today,
                'counter': counter,
                'teacher_list': teacher_list,
                'r1':r1, 'r2':r2,'r3':r3,'r4':r4,'r5':r5,'r6':r6,'r7':r7,'r8':r8,
                'reserveinfoteacher': reserveinfoteacher,
                })


def nextlistfunc(request, counter):
    stuortea = request.user.role
    teacher_list = []
    username = request.user.get_full_name()
    teachers = User.objects.filter(role=1)
    counter += 1
    todaycalc = timedelta(days=counter)
    newtoday = today + todaycalc
    adddate = timedelta(days=1)
    subdate = timedelta(days=-1)
    teachers = teachers.filter(workmodel__workdate=newtoday)
    reserveinfo = ReserveModel.objects.filter(reservedate=newtoday)
    reserveinfoteacher = reserveinfo.filter(teacher=request.user)

    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    r5 = ''
    r6 = ''
    r7 = ''
    r8 = ''
    for teacher in teachers:
        if teacher not in teacher_list:
            teacher_list.append(teacher)
    for r in reserveinfo:
        if r.reservetime == 'c1':
            r1 += str(r.teacher.email) + ','
        elif r.reservetime == 'c2':
            r2 += str(r.teacher.email) + ','
        elif r.reservetime == 'c3':
            r3 += str(r.teacher.email) + ','
        elif r.reservetime == 'c4':
            r4 += str(r.teacher.email) + ','
        elif r.reservetime == 'c5':
            r5 += str(r.teacher.email) + ','
        elif r.reservetime == 'c6':
            r6 += str(r.teacher.email) + ','
        elif r.reservetime == 'c7':
            r7 += str(r.teacher.email) + ','
        elif r.reservetime == 'c8':
            r8 += str(r.teacher.email) + ','
    # 教師
    if stuortea == 1:
        return render(request, 'list_teacher.html', {
                'username': username, 
                'teachers': teachers,
                'newtoday': newtoday,
                'today': today,
                'counter': counter,
                'teacher_list': teacher_list,
                'r1':r1, 'r2':r2,'r3':r3,'r4':r4,'r5':r5,'r6':r6,'r7':r7,'r8':r8,
                'reserveinfoteacher': reserveinfoteacher,
                })
    # 生徒
    else:
        return render(request, 'list_student.html', {
                'username': username, 
                'teachers': teachers,
                'newtoday': newtoday,
                'today': today,
                'counter': counter,
                'teacher_list': teacher_list,
                'r1':r1, 'r2':r2,'r3':r3,'r4':r4,'r5':r5,'r6':r6,'r7':r7,'r8':r8,
                'reserveinfoteacher': reserveinfoteacher,
                })

def reservefunc(request, teacherid, newtoday, worktime):
    teacher = User.objects.filter(id=teacherid)
    subjects = Subject.objects.all()
    kamoku = Subject.Kamoku
    print(subjects)
    username = request.user.get_full_name()
    
    return render(request, 'reserve.html', {
        'username': username,
        'teacher': teacher,
        'newtoday': newtoday,
        'worktime': worktime,
        'subjects': subjects,
        'kamoku': kamoku,
    })

def completefunc(request, teacherid, newtoday, worktime):
    student = request.user.get_full_name()
    student_id = request.user.id
    teacher = User.objects.get(id=teacherid)
    teacher_name = teacher.last_name + teacher.first_name
    print(teacher)
    res_date = newtoday
    res_time = worktime
    subject = request.POST['subject']
    textname = request.POST['textname']
    question = request.POST['question']
    ReserveModel.objects.create(teacher=teacher, student=student, studentid=student_id, subject=subject, textbook=textname, content=question, reservedate=res_date, reservetime=res_time)
    if res_time =='c1':
        reservetime = "14:00"
    if res_time =='c2':
        reservetime = "15:00"
    if res_time =='c3':
        reservetime = "16:00"
    if res_time =='c4':
        reservetime = "17:00"
    if res_time =='c5':
        reservetime = "18:00"
    if res_time =='c6':
        reservetime = "19:00"
    if res_time =='c7':
        reservetime = "20:00"
    if res_time =='c8':
        reservetime = "21:00"
    print(res_time)
    send_mail('予約完了',
     student+'さん、' + res_date  + '  ' + reservetime + 'に' + teacher_name + '先生の予約が完了しました。',
      'ck.m8.r.o.m@gmail.com',
    ['shota.masuo@gmail.com'],
     fail_silently=False,)
    return redirect('list')