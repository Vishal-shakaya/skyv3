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
