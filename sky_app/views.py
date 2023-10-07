from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as UserObj
from django.contrib.auth import authenticate, login, logout
from sky_app.forms import RegistorUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import ResponseBack, ValidateCardData, UpdateCard, CreateCard, surveyFields
from .models import SkyCard, Blog
from .forms import CreateCardForm, SurveyForm
from django.db.models import Q
from .models import PartnerUs
# Create your views here.


def HomvView(request):
    return render(request, template_name='index.html')


def CreateCardView(request, pk):
    # check update or create card :
    is_exist = SkyCard.objects.filter(user=request.user)
    if request.user.is_authenticated:
        if is_exist:
            obj = SkyCard.objects.get(user=request.user)
            return render(request, 'CreateCard.html', {"skyObj": obj, 'is_update': is_exist})
        else:
            return render(request, 'CreateCard.html')
    else:
        return redirect('auth')


def CardDetailView(request, pk):
    card = SkyCard.objects.get(pk=pk)
    if request.user.is_authenticated:
        return render(request, template_name='CardDetailView.html', context={'card': card})
    else:
        return redirect('auth')


def CardListView(request):
    print(request.POST)
    if request.user.is_authenticated:
        if request.POST:
            print(request.POST)

            search_value = request.POST['search_value']
            is_exist = SkyCard.objects.filter(Q(number__contains=search_value)
                                              | Q(business_name__contains=search_value)
                                              | Q(name__contains=search_value)
                                              )
            # print(is_exist)
            if is_exist:
                return render(request, template_name='CardSearchView.html', context={'cards': is_exist})
            else:
                cards = SkyCard.objects.all()
                return render(request, template_name='CardSearchView.html', context={'cards': cards})

        else:
            cards = SkyCard.objects.all()
            return render(request, template_name='CardSearchView.html', context={'cards': cards})
    else:
        return redirect('auth')


def FeedbackView(request):
    return render(request, template_name='Feedback.html', )


def OurWorkView(request):
    return render(request, template_name='OurWork.html', )


def OurStoryView(request):
    return render(request, template_name='OurStory.html', )


def OnDemandView(request):
    return render(request, template_name='OnDemand.html', )


def AboutView(request):
    return render(request, template_name='About.html', )


def CampaignView(request):
    return render(request, template_name='Campaing.html', )


def AuthView(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('create_card', pk=request.user.pk)
    else:
        return render(request, template_name='Auth.html', )


@csrf_exempt
def SignupHandler(request):
    try:
        if request.POST:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            print(username,password)
            user_exist = UserObj.objects.filter(
                username=username,)

            if not user_exist :
                print("user is not existing")
                
            # If user already exist
            if (user_exist):
                print(f'user exist ${user_exist}')
                return ResponseBack(message='username already exist', data='', response='fail')

            my_user = UserObj.objects.create_user(
                username=username, password=password)
            my_user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return ResponseBack(message='', data=my_user.pk, response='success')
    except Exception as e:
        print(f'error {e}')
        return ResponseBack(message='something went wrong', data='', response='fail')


@csrf_exempt
def LoginHandler(request):
    try:
        if request.POST:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            user_exist = authenticate(username=username, password=password)

            if user_exist == None:
                return ResponseBack(message='user not exist', response='fail', data='')

            if user_exist is not None:
                login(request, user_exist)
                return ResponseBack(data=user_exist.pk, response='success', message='')
            else:
                return ResponseBack(response='fail', message='something went wrong', data='')

        return ResponseBack(response='fail', message='something went wrong', data='')
    except Exception as e:
        return ResponseBack(response='fail', message='something went wrong', data='')


@csrf_exempt
def CreateCardHandler(request):
    data = request.POST

    # check update or create card :
    is_exist = SkyCard.objects.filter(user=request.user)

    # Update Card if user already created card :
    if is_exist:
        print('udpate card')
        # Validate Card Beform Update :
        resp = ValidateCardData(request=request)
        print(f'Validate Data {resp}')
        if resp['response'] == 'success':
            updateResp = UpdateCard(request)
            print(f'Update Resp {updateResp}')
            print(updateResp['response'])
            # Success Response
            if (updateResp['response'] == 'success'):
                return JsonResponse(updateResp)
            # Error Response
            if (updateResp['response'] == 'fail'):
                return JsonResponse(updateResp)

        if (resp['response'] == 'fail'):
            return JsonResponse(resp)

    # Creating New card :
    # Validate data before create new card :
    else:
        print('Create card')
        resp = ValidateCardData(request=request)

        # Validate Card Beform Update :
        if resp['response'] == 'success':
            createResp = CreateCard(request)
            print(f'update Resp {updateResp}')

            # Success Response
            if (createResp['response'] == 'success'):
                return JsonResponse(createResp)
            # Error Response
            if (createResp['response'] == 'fail'):
                return JsonResponse(createResp)

        if (resp['response'] == 'fail'):
            return JsonResponse(resp)


@csrf_exempt
def LogoutUser(request):
    try:
        logout(request)
        return ResponseBack(message='logout user', data='', response='success')
    except:
        return ResponseBack(message='unable to logout user', data='', response='fail')


@csrf_exempt
def DeleteCardManager(request, pk):
    try:
        obj = SkyCard.objects.get(pk=pk)
        obj.delete()
        return ResponseBack(message='Card Deleted', data='', response='success')
    except print(0):
        return ResponseBack(message='Unable to Delete Card', data='', response='fail')


def BlogView(request):
    blogs = Blog.objects.all()
    return render(request, template_name='BlogView.html', context={'blogs': blogs})


def BlogDetailView(request, pk):
    is_exist = Blog.objects.filter(pk=pk)
    if is_exist:
        blog = Blog.objects.get(pk=pk)
        return render(request, template_name='BlogDetail.html', context={'blog': blog})
    else:
        return JsonResponse({'soemthing Went Wrong': 'error'})


def SurveyView(request):
    if request.POST:
        form = SurveyForm(request.POST)
        form.save()
    return render(
        request,
        template_name='SurveyView.html',
        context={"fields": surveyFields})

def PartnerView(request):
    return render(request, template_name='PartnerWithUs.html')

@csrf_exempt
def CreatePartner(request):
    data = request.POST; 
    print(data['name']);
    if request.method=='POST':
        try:
            # data=PartnerUs(name=name,phone=phone,email=email,category=category,website=website)
            # data.save()
       
            return ResponseBack(message='Partner Registered', data='', response='success')
        except print(0):
            return ResponseBack(message='Unable To Register Partner', data='', response='fail')
