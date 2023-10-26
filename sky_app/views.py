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
from .models import PartnerUs, SureveyQuest, NewsletterSubscription, QueryForm
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
            print(username, password)
            user_exist = UserObj.objects.filter(
                username=username,)

            if not user_exist:
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
    return render(
        request,
        template_name='SurveyView.html',
        context={"fields": surveyFields})

@csrf_exempt
def SurveyForm(request):
    data=request.body
    jsonData=json.loads(data)
    print(jsonData)
    
    email=jsonData['email']
    yes_1=jsonData['yes_1']
    no_1=jsonData['no_1']
    
    yes_2=jsonData['yes_2']
    no_2=jsonData['no_2']
    
    yes_3=jsonData['yes_3']
    no_3=jsonData['no_3']
    
    yes_4=jsonData['yes_4']
    no_4=jsonData['no_4']
    
    yes_5=jsonData['yes_5']
    no_5=jsonData['no_5']
    
    yes_6=jsonData['yes_6']
    no_6=jsonData['no_6']
    
    yes_7=jsonData['yes_7']
    no_7=jsonData['no_7']
    
    yes_8=jsonData['yes_8']
    no_8=jsonData['no_8']
    
    yes_9=jsonData['yes_9']
    no_9=jsonData['no_9']
    
    yes_10=jsonData['yes_10']
    no_10=jsonData['no_10']
    
    yes_11=jsonData['yes_11']
    no_11=jsonData['no_11']
    
    yes_12=jsonData['yes_12']
    no_12=jsonData['no_12']
    
    yes_13=jsonData['yes_13']
    no_13=jsonData['no_13']
    
    yes_14=jsonData['yes_14']
    no_14=jsonData['no_14']
    
    yes_15=jsonData['yes_15']
    no_15=jsonData['no_15']
    
    yes_16=jsonData['yes_16']
    no_16=jsonData['no_16']
    
    print(type(yes_1))
    print(no_2)
    if request.method =='POST':
        try:
            surveyData=SureveyQuest(
                email=email,
                yes_1=yes_1,
                no_1=no_1,
                
                yes_2=yes_2,
                no_2=no_2,
                
                yes_3=yes_3,
                no_3=no_3,
                
                yes_4=yes_4,
                no_4=no_4,
                
                yes_5=yes_5,
                no_5=no_5,
                
                yes_6=yes_6,
                no_6=no_6,
                
                yes_7=yes_7,
                no_7=no_7,
                
                yes_8=yes_8,
                no_8=no_8,
                
                yes_9=yes_9,
                no_9=no_9,
                
                yes_10=yes_10,
                no_10=no_10,
                
                yes_11=yes_11,
                no_11=no_12,
                
                yes_12=yes_12,
                no_12=no_12,
                
                yes_13=yes_13,
                no_13=no_13,
                
                yes_14=yes_14,
                no_14=no_14,
                
                yes_15=yes_15,
                no_15=no_15,
                
                yes_16=yes_16,
                no_16=no_16,
            )
            surveyData.save()
            return ResponseBack(message='Data submitted', data='', response='success')
        except print(0):
            return ResponseBack(message='Unable to submit data', data='', response='fail')

    
    
    
    



def PartnerView(request):
    return render(request, template_name='PartnerWithUs.html')


@csrf_exempt
def CreatePartner(request):
    data = request.body
    jsonData = json.loads(data)
    name = jsonData['name']
    email = jsonData['email']
    phone = jsonData['phone']
    catigory = jsonData['catigory']
    website = jsonData['website']

    print(name)
    print(email)
    print(phone)
    print(catigory)
    print(website)

    if request.method == 'POST':
        try:
            partnerIns = PartnerUs(
                name=name,
                email=email,
                phone=phone,
                category=catigory,
                website=website,
            )
            partnerIns.save()
            return ResponseBack(message='Partner Registered', data='', response='success')
        except print(0):
            return ResponseBack(message='Unable To Register Partner', data='', response='fail')

@csrf_exempt
def NewsletterSubs(request):
    data=request.body
    jsonData=json.loads(data)
    email=jsonData["email"]
    
    if request.method == 'POST':
        try:
            mailSub = NewsletterSubscription(
                email=email,
            )
            mailSub.save()
            return ResponseBack(message='Email registered', data='', response='success')
        except print(0):
            return ResponseBack(message='Unable To Register Email', data='', response='fail')
    
    
    
@csrf_exempt
def QueryFormReg(request):
    data=request.body
    jsonData=json.loads(data)
    print(jsonData)
    
    name=jsonData["name"]
    phone=jsonData["phone"]
    email=jsonData["email"]
    services=json.dumps(jsonData["services"])
    message=jsonData["message"]
    
    if request.method=="POST":
        try:
            queryRegister = QueryForm(
                name=name,
                phone=phone,
                email=email,
                services=services,
                message=message
            )
            queryRegister.save()
            return ResponseBack(message='Query registered', data='', response='success')
        except print(0):
            return ResponseBack(message='Unable To Register Query', data='', response='fail')
    