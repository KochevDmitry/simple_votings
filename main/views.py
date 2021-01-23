import datetime

from django.shortcuts import render
from main.models import Votings, InformationAboutVoting
import sqlite3


def get_menu_context():
    return [
        {'url_name': 'index', 'name': 'Главная'},
        {'url_name': 'time', 'name': 'Текущее время'},
    ]


def index_page(request):
    context = {
        'pagename': 'Главная',
        'author': 'Andrew',
        'pages': 4,
        'menu': get_menu_context()
    }
    if request.user.is_authenticated:
        vot = Votings.objects.filter(user_create=request.user)
        context['votings_user'] = vot
    return render(request, 'pages/index.html', context)


def time_page(request):
    context = {
        'pagename': 'Текущее время',
        'time': datetime.datetime.now().time(),
        'menu': get_menu_context()
    }
    return render(request, 'pages/time.html', context)


def votings_page(request):
    vot = Votings.objects.all()
    context = {'votings': vot}
    print(vot)
    return render(request, 'pages/votings.html', context)


def add_voting(request):
    name = request.GET.get('name', '')
    info = request.GET.get('info', '')
    label1 = request.GET.get('label1', None)
    label2 = request.GET.get('label2', None)
    label3 = request.GET.get('label3', None)
    if name != '' and label3 != None and label2 != None and label1 != None and info != '':
        labels = str(label1) + '$' + str(label2) + '$' + str(label3)
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = '0' + '$' + '0' + '$' + '0'
        c = Votings(voting_name=name, user_create=request.user)
        c.save()
        result = cur.execute("""SELECT id FROM main_votings WHERE voting_name='{}'""".format
                             (name)).fetchall()
        id = result[0][0]
        b = InformationAboutVoting(information=info, labels=labels, voting_id=id, result=res)
        b.save()
        context = {'message': 'Вы создали голосование'}
    else:
        context = {'message': ''}
    return render(request, 'pages/add_voting.html', context)


def voting_info_page(request):
    global context, labels, result, id
    context = {}
    if request.GET.get('id', None):
        id = request.GET.get('id', None)
    vot_info = InformationAboutVoting.objects.filter(voting=id)
    for i in vot_info:
        label = i.labels
        res = i.result
        labels = label.split('$')
        result = res.split('$')
        context = {'id_voting': i.voting, 'labels': labels, 'result': result, 'info': i.information}
    context['Letter'] = 'Вы проголосовали'
    print(context['id_voting'])
    for i in range(len(labels)):
        label = request.GET.get(labels[i], None)
        if label is not None:
            result[i] = str(int(result[i]) + 1)
            context['result'] = result
            res = '$'.join(result)
            print('res: ', res)
            con = sqlite3.connect("db.sqlite3")
            cur = con.cursor()
            cur.execute("""UPDATE main_informationaboutvoting SET result='{}' WHERE voting_id = {}""".format
                        (res, id))
            con.commit()
            con.close()
            context['Letter'] += ' ' + labels[i] + ','
    if context['Letter'] == 'Вы проголосовали':
        context['Letter'] = 'Вы не проголосовали'
    else:
        context['Letter'] = context['Letter'][:-1]
    return render(request, 'pages/voting_info.html', context)


def result_voting(request):
    global id
    vot_info = InformationAboutVoting.objects.filter(voting=id)
    for i in vot_info:
        label = str(i.labels)
        res = str(i.result)
        labels = label.split('$')
        result = res.split('$')
        res = []
        print(type(labels), type(result), labels, result, type(labels[0]))
        for j in range(len(labels)):
            res.append([labels[j], result[j]])
        context = {'res': res}
        print(res, 112)
    return render(request, 'pages/result_voting.html', context)

def edit_profile(request):
    new_name = request.GET.get('name', '')
    context = {'message': ''}
    if new_name != '':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("""SELECT username FROM auth_user""").fetchall()
        if new_name in res[0]:
            context['message'] = 'Такой логин уже существует'
        else:
            cur.execute("""UPDATE auth_user SET username = '{}' WHERE username = '{}'""".format(new_name, request.user))
            con.commit()
            cur.execute("""UPDATE main_votings SET user_create = '{}' WHERE user_create = '{}'""".format(new_name, request.user))
            con.commit()
            con.close()
    return render(request, 'pages/edit_profile.html', context)
