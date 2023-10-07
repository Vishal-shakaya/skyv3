from django.http import JsonResponse
from .models import SkyCard


def ResponseBack(message, data, response):
    temp = {
        'message': message,
        'data': data,
        'response': response
    }
    return JsonResponse(temp)


def PyResponseBack(message, data, response):
    temp = {
        'message': message,
        'data': data,
        'response': response
    }
    return temp


def ValidateField(field):
    if (field == '' or field == None):
        return PyResponseBack(
            message=f'required field cant be empty check ',
            data='',
            response='fail')
    else:
        return PyResponseBack(
            message=f'required field cant be empty check ',
            data='',
            response='success')


def ValidateCardData(request):
    try:
        data = request.POST

        userName = data['userName']
        resp = ValidateField(field=userName)
        if (resp['response'] == 'fail'):
            return resp

        position = data['position']
        resp = ValidateField(field=position)
        if (resp['response'] == 'fail'):
            return resp

        userNumber = data['userNumber']
        resp = ValidateField(field=userNumber)
        if (resp['response'] == 'fail'):
            return resp

        userwhatsappNumber = data['userwhatsappNumber']
        resp = ValidateField(field=userwhatsappNumber)
        if (resp['response'] == 'fail'):
            return resp

        userEmail = data['userEmail']
        resp = ValidateField(field=userEmail)
        if (resp['response'] == 'fail'):
            return resp

        instaLink = data['instaLink']
        resp = ValidateField(field=instaLink)
        if (resp['response'] == 'fail'):
            return resp

        faceLink = data['faceLink']
        resp = ValidateField(field=faceLink)
        if (resp['response'] == 'fail'):
            return resp

        twitterLink = data['twitterLink']
        resp = ValidateField(field=twitterLink)
        if (resp['response'] == 'fail'):
            return resp

        youtubeLink = data['youtubeLink']
        resp = ValidateField(field=youtubeLink)
        if (resp['response'] == 'fail'):
            return resp

        businessName = data['businessName']
        resp = ValidateField(field=businessName)
        if (resp['response'] == 'fail'):
            return resp

        gstNumber = data['gstNumber']
        resp = ValidateField(field=gstNumber)
        if (resp['response'] == 'fail'):
            return resp

        stablishedYear = data['stablishedYear']
        resp = ValidateField(field=stablishedYear)
        if (resp['response'] == 'fail'):
            return resp

        webUrl = data['webUrl']
        resp = ValidateField(field=webUrl)
        if (resp['response'] == 'fail'):
            return resp

        tagline = data['tagline']
        resp = ValidateField(field=tagline)
        if (resp['response'] == 'fail'):
            return resp

        businessTag = data['businessTag']
        resp = ValidateField(field=businessTag)
        if (resp['response'] == 'fail'):
            return resp

        businessDesc = data['businessDesc']
        resp = ValidateField(field=businessDesc)
        if (resp['response'] == 'fail'):
            return resp

        state = data['state']
        resp = ValidateField(field=state)
        if (resp['response'] == 'fail'):
            return resp

        city = data['city']
        resp = ValidateField(field=city)
        if (resp['response'] == 'fail'):
            return resp

        country = data['country']
        resp = ValidateField(field=country)
        if (resp['response'] == 'fail'):
            return resp

        pincode = data['pincode']
        resp = ValidateField(field=pincode)
        if (resp['response'] == 'fail'):
            return resp

        address = data['address']
        resp = ValidateField(field=address)
        if (resp['response'] == 'fail'):
            return resp

        businessHead = data['businessHeading']
        resp = ValidateField(field=businessHead)
        if (resp['response'] == 'fail'):
            return resp

        if (request.FILES):
            try:
                profileImage = request.FILES['profile_image']
                resp = ValidateField(field=profileImage)
                if (resp['response'] == 'fail'):
                    return resp
            except Exception as e:
                print(e)
                print('no profile image')

                try:
                    businessLogo = request.FILES['business_logo']
                    resp = ValidateField(field=businessLogo)
                    if (resp['response'] == 'fail'):
                        return resp
                except Exception as e:
                    print('no business logo ')
        else:
            print('file not exist')

        return PyResponseBack(message='validate data', data='', response='success')
    except Exception as e:
        print(e)
        return PyResponseBack(message=' error found', data='', response='fail')


def UpdateCard(request):
    try:
        cardIns = SkyCard.objects.get(user=request.user)
        data = request.POST
        userName = data['userName']
        businessHeading = data['businessHeading']
        position = data['position']
        userNumber = data['userNumber']
        userwhatsappNumber = data['userwhatsappNumber']
        userEmail = data['userEmail']
        instaLink = data['instaLink']
        faceLink = data['faceLink']
        twitterLink = data['twitterLink']
        youtubeLink = data['youtubeLink']
        businessName = data['businessName']
        gstNumber = data['gstNumber']
        stablishedYear = data['stablishedYear']
        webUrl = data['webUrl']
        tagline = data['tagline']
        businessTag = data['businessTag']
        businessDesc = data['businessDesc']
        state = data['state']
        city = data['city']
        country = data['country']
        pincode = data['pincode']
        address = data['address']

        if (request.FILES):
            try:
                profileImage = request.FILES['profile_image']
                if (cardIns.profile_image != '' or cardIns.profile_image != None):
                    cardIns.profile_image = profileImage
            except:
                print('No Profile Image')

            try:
                businessLogo = request.FILES['business_logo']
                if (cardIns.business_logo == '' or cardIns.business_logo == None):
                    cardIns.business_logo = businessLogo
            except:
                print('No Business Logo')

        else:
            print('file not exist')

        cardIns.name = userName
        cardIns.position = position
        cardIns.number = userNumber
        cardIns.whats_app_number = userwhatsappNumber
        cardIns.email = userEmail
        cardIns.insta = instaLink
        cardIns.facebook = faceLink
        cardIns.twitter = twitterLink
        cardIns.youtube = youtubeLink
        cardIns.business_name = businessName
        cardIns.gst_number = gstNumber
        cardIns.stablish_year = stablishedYear
        cardIns.website = webUrl
        cardIns.tagline = tagline
        cardIns.business_description = businessDesc
        cardIns.tag = businessTag
        cardIns.state = state
        cardIns.city = city
        cardIns.country = country
        cardIns.pincode = pincode
        cardIns.address = address
        cardIns.business_heading = businessHeading
        cardIns.user = request.user
        cardIns.save()

        return PyResponseBack(message='card updated', response='success', data='')
    except Exception as e:
        print(e)
        return PyResponseBack(message='unable to update card',
                              response='fail', data='')


def CreateCard(request):
    try:
        cardIns = SkyCard()
        data = request.POST
        userName = data['userName']
        businessHeading = data['businessHeading']
        position = data['position']
        userNumber = data['userNumber']
        userwhatsappNumber = data['userwhatsappNumber']
        userEmail = data['userEmail']
        instaLink = data['instaLink']
        faceLink = data['faceLink']
        twitterLink = data['twitterLink']
        youtubeLink = data['youtubeLink']
        businessName = data['businessName']
        gstNumber = data['gstNumber']
        stablishedYear = data['stablishedYear']
        webUrl = data['webUrl']
        tagline = data['tagline']
        businessTag = data['businessTag']
        businessDesc = data['businessDesc']
        state = data['state']
        city = data['city']
        country = data['country']
        pincode = data['pincode']
        address = data['address']
        profileImage = request.FILES['profile_image']
        businessLogo = request.FILES['business_logo']

        cardIns.profile_image = profileImage
        cardIns.business_logo = businessLogo
        cardIns.name = userName
        cardIns.position = position
        cardIns.number = userNumber
        cardIns.whats_app_number = userwhatsappNumber
        cardIns.email = userEmail
        cardIns.insta = instaLink
        cardIns.facebook = faceLink
        cardIns.twitter = twitterLink
        cardIns.youtube = youtubeLink
        cardIns.business_name = businessName
        cardIns.gst_number = gstNumber
        cardIns.stablish_year = stablishedYear
        cardIns.website = webUrl
        cardIns.tagline = tagline
        cardIns.business_description = businessDesc
        cardIns.tag = businessTag
        cardIns.state = state
        cardIns.city = city
        cardIns.country = country
        cardIns.pincode = pincode
        cardIns.address = address
        cardIns.business_heading = businessHeading
        cardIns.user = request.user
        cardIns.save()

        return PyResponseBack(message='card creaded', response='success', data='')
    except Exception as e:
        return PyResponseBack(message='unable to create card', response='fail', data='')


surveyFields = [
    {
        'field_name1': 'yes_1',
        'field_name2': 'no_1',
        'title': '''Does business have missed-call text-back in place?''',
        'subtitle': ''' Small and mid-sized businesses miss about 62% of calls! Automating a text message back to missed-call dialers prevents
                    prospects from calling competitors and recoups countless in would-be missed revenue!'''
    },
    {
        'field_name1': 'yes_2',
        'field_name2': 'no_2',
        'title': '''Does website have a text-enabled phone number?''',
        'subtitle': ''' 9 out of 10 people want to use messaging to interact with businesses, and the average open rate of an SMS is 99 % ! It’s critical
                    that businesses offer Text Messaging as a communication channel for their customers.'''
    },
    {
        'field_name1': 'yes_3',
        'field_name2': 'no_3',
        'title': '''Does website have an SMS chat widget?''',
        'subtitle': ''' SMS chat widgets allow website visitors to quickly initiate a text-message conversation but not be tethered to a website.'''
    },
    {
        'field_name1': 'yes_4',
        'field_name2': 'no_4',
        'title': '''Is Google Business Chat enabled?''',
        'subtitle': ''' The average business receives over 1,000 monthly visits to their Google Business Profile! Activating Google Chat immediately
                        converts more of these visitors into customers.'''
    },
    {
        'field_name1': 'yes_5',
        'field_name2': 'no_5',
        'title': '''Are popular listings in place and in order?''',
        'subtitle': ''' Top-ranking local businesses have approximately 81 citations from top-level domains on average and search engines love to
see consistent data.'''
    },
    {
        'field_name1': 'yes_6',
        'field_name2': 'no_6',
        'title': '''Does business have a consolidated conversation stream? Is it mobile-friendly?''',
        'subtitle': ''' Managing conversations across communications in one conversation stream increases response time and ensures conversa
tions don't go unanswered.'''
    },

    {
        'field_name1': 'yes_7',
        'field_name2': 'no_7',
        'title': '''Is business leveraging Text Snippets or auto-replies for FAQs?''',
        'subtitle': ''' Response time is the # 1 factor when it comes to turning conversations into sales.'''
    },
    {
        'field_name1': 'yes_8',
        'field_name2': 'no_8',
        'title': '''Is the business set up to send personalized video messages to leads?''',
        'subtitle': '''93% of companies who send personalized videos see an increase in conversion rate.'''
    },
    {
        'field_name1': 'yes_9',
        'field_name2': 'no_9',
        'title': '''Does the business have Tap-2-Pay?''',
        'subtitle': '''Tap to pay turns smartphones into credit card readers, enabling payment anywhere. '''
    },
    {
        'field_name1': 'yes_10',
        'field_name2': 'no_10',
        'title': '''Does business have an acceptable amount of Google reviews?''',
        'subtitle': '''60% of consumers feel that the number of reviews a business has is critical and 8 8 % of consumers make the effort to consult
                    reviews before purchase. '''
    },
    {
        'field_name1': 'yes_11',
        'field_name2': 'no_11',
        'title': '''Does business have an acceptable rating?''',
        'subtitle': '''3.3 Stars is the minimum rating customers expect. '''
    },
    {
        'field_name1': 'yes_12',
        'field_name2': 'no_12',
        'title': '''Are reviews being generated frequently and consistently?''',
        'subtitle': '''A steady increase in reviews has been shown to correlate with an increase in phone calls from Google Business Profiles. '''
    },
    {
        'field_name1': 'yes_13',
        'field_name2': 'no_13',
        'title': '''Are reviews being replied to?''',
        'subtitle': '''89% of consumers say they,re likely to choose a local business that responds to reviews. '''
    },
    {
        'field_name1': 'yes_14',
        'field_name2': 'no_14',
        'title': '''Does business have a database of emails and phone numbers?''',
        'subtitle': '''Businesses who aren't consistently growing a database of potential and existing customer information generate significantly
less repeat-buyers than businesses who have healthy database.'''
    },

    {
        'field_name1': 'yes_15',
        'field_name2': 'no_15',
        'title': '''Does business have a way to send bulk email/sms?''',
        'subtitle': '''Businesses that can send news, promotions, updates, and stories to contacts in bulk are able to generate new sales on-demand.'''
    },
    {
        'field_name1': 'yes_16',
        'field_name2': 'no_16',
        'title': '''Does business have a Newsletter Builder?''',
        'subtitle': '''Visual emails create brand awareness and increase brand loyalty.'''
    },
]
