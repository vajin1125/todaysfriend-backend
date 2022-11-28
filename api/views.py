from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductImageSerializer, ProfileSerializer, TravelSerializer, EventSerializer, LocalSerializer, UserSerializer, BookingSerializer, BookerSerializer, TravelCommentSerializer, EventCommentSerializer, LocalCommentSerializer
from .models import Product, ProductImage, Profile, Booker, Booking, Travel, Event, LocalCommunity, TravelComment, EventComment, LocalComment, SocialUser
import datetime
import os
import shutil
import string
import random
import json


# for test
def test(request):
    return render(request, 'test.html')

# for login
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        print(request.data)
        data = request.data['values']
        username = data['username']
        email = data['email']
        name_count = User.objects.filter(username=username).count()
        email_count = User.objects.filter(email = email).count()

        if name_count > 0 and email_count > 0:
            response_data = {'type':'error', 'message':'already existed user'}
        elif name_count > 0 and email_count == 0:
            response_data = {'type':'error', 'message':'already registered username'}
        elif name_count == 0 and email_count > 0:
            response_data = {'type':'error', 'message':'already registered email'}
        else:
            user = User()
            user.username = data['username']
            user.email = data['email']
            user.password = data['password']
            user.save()
            response_data = {'type':'success', 'name': username}
        return Response(response_data)



@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        print(request.data)
        try:
            data = request.data['values']
            email = data['email']
            password = data['password']
            match_user = User.objects.get(email=email)
            if match_user.password == password:
                match_user.last_login = datetime.datetime.now()
                match_user.save()
                username = match_user.username
                response_data = {'type':'success', 'name': username}
                return Response(response_data)
            else:
                response_data = {'type':'error', 'message': 'wrong password'}
                return Response(response_data)
        except User.DoesNotExist:
            response_data = {'type':'error', 'message': 'not exist'}
            return Response(response_data)


@api_view(['POST'])
def social_login(request):
    if request.method == 'POST':
        print(request.data)
        data = request.data
        socialId = data['socialId']
        socialName = data['socialName']
        match_user = SocialUser.objects.filter(socialId=socialId, socialName=socialName)
        if len(match_user) != 0:
            response_data = {'type':'exist', 'name': socialName}
        else: 
            socialuser = SocialUser()
            socialuser.name = data['name']
            socialuser.email = data['email']
            socialuser.socialId = data['socialId']
            socialuser.socialName = data['socialName']
            socialuser.joinTime = datetime.datetime.now()
            socialuser.save()
            response_data = {'type':'new', 'name': socialName}
        return Response(response_data)


@api_view(['POST'])
def logout(request):
    pass

            
# for create product
@api_view(['POST'])
def register_product(request):
    if request.method == 'POST':
        # print(request.data)
        product = Product()
        data = request.data['values']
        ran_str = random_str_generator()
        product.pdu_ustr = ran_str
        product.pdu_name = data['tourname']
        product.pdu_type = data['tourtype']
        product.pdu_country = data['country']
        product.pdu_city = data['city']
        product.pdu_language = data['language']
        product.pdu_brief_description = data['briefDesc']
        product.pdu_detailed_description = data['detailedDesc']
        product.pdu_hashtag = data['hashtag']
        product.pdu_meeting_time = request.data['meetingtime']
        product.pdu_duration = request.data['durationhours']
        product.pdu_location = data['meetingLocation']
        product.pdu_hottoget = data['howgetthere']
        product.pdu_price = data['price']
        product.pdu_price_include = data['priceIncluded']
        product.pdu_min_guest = data['minNumGuest']
        product.pdu_max_guest = data['maxNumGuest']
        product.pdu_season_from = request.data['seasondate'][0]
        product.pdu_season_to = request.data['seasondate'][1]
        notdays = ','.join(data['notAllowed'])
        product.pdu_unavailable_date = notdays
        product.pdu_additional_info = data['addNote']
        product.pdu_created_time = datetime.datetime.now()

        # for product image
        uploaddirpath = 'static/uploads/images/products/' + ran_str    
        os.makedirs(uploaddirpath)
        uploadedFiles = request.data['uploadedFiles']

        # move available tourimages in own directory
        for imgfile in uploadedFiles:
            print(imgfile['name'])
            source = 'static/uploads/images/temp/' + imgfile['name']
            destination = uploaddirpath
            shutil.move(source, destination)

            # product images save to table
            product_img = ProductImage()
            product_img.pdu_name = data['tourname']
            product_img.pdu_ustr = ran_str
            product_img.pdu_img_name = imgfile['name']
            product_img.pdu_img_url = destination
            product_img.save()

        # # delete all files in temp directory
        # dirPath = 'static/uploads/images/temp/'
        # fileList = os.listdir(dirPath)
        # for fileName in fileList:
        #     os.remove(dirPath+"/"+fileName)

        # Save Product table
        product.save()
        response_data = {'type':'success'}
    else:
        response_data = {'type':'failed'}
    return Response(response_data)


# random string generator
def random_str_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def handle_uploaded_file(f):
    filename = f.name
    url = 'static/uploads/images/temp/'
    with open(url + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            

@api_view(['POST'])
def upload_tour_img(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'])
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['POST'])
def remove_uploaded_img(request):
    if request.method == 'POST':
        url = 'static/uploads/images/temp/'
        filename = request.data['file']['name']
        os.remove(url + '/' + filename)
        response_data = {'type': 'success'}
        return Response(response_data)



###################################################################################
# test register products
@api_view(['POST'])
def test_register_product(request):
    if request.method == 'POST':
        # print(request.data)
        product = Product()
        data = request.data['values']
        ran_str = random_str_generator()
        product.pdu_ustr = ran_str
        product.pdu_name = data['tourname']
        product.pdu_type = data['tourtype']
        product.pdu_country = data['country']
        product.pdu_city = data['city']
        language = ','.join(data['language'])
        product.pdu_language = language
        product.pdu_brief_description = data['briefDesc']
        product.pdu_detailed_description = data['detailedDesc']
        product.pdu_hashtag = data['hashtag']
        product.pdu_meeting_time = data['meetingTime']
        product.pdu_duration = data['duration']
        product.pdu_location = data['meetingLocation']
        product.pdu_hottoget = data['howgetthere']
        product.pdu_price = data['price']
        product.pdu_price_include = data['priceIncluded']
        product.pdu_min_guest = data['minNumGuest']
        product.pdu_max_guest = data['maxNumGuest']
        product.pdu_season_from = request.data['seasondate'][0]
        product.pdu_season_to = request.data['seasondate'][1]
        notdays = ','.join(request.data['notAllowedDate'])
        product.pdu_unavailable_date = notdays
        product.pdu_additional_info = data['addNote']
        product.pdu_created_time = datetime.datetime.now()
        product.pdu_created_by = request.data['username']
        # latlng = request.data['meetingpoint'].split(",")
        # product.pdu_meeting_point_lat = latlng[0]
        # product.pdu_meeting_point_lng = latlng[1]
        product.pdu_meeting_point_lat = request.data['meetingpoint']['lat']
        product.pdu_meeting_point_lng = request.data['meetingpoint']['lng']

        # for product image
        uploaddirpath = 'static/uploads/images/products/' + ran_str    
        os.makedirs(uploaddirpath)
        uploadedFiles = request.data['uploadedFiles']

        # move to file real directory
        source = 'static/uploads/images/temp/'
        destination = uploaddirpath
        files = os.listdir(source)
        for f in files:
            shutil.move(source + f, destination)
        #
        # Save ProductImg table 
        for imgfile in uploadedFiles:
            # print(imgfile['name'])
            # product images save to table
            product_img = ProductImage()
            product_img.pdu_name = data['tourname']
            product_img.pdu_ustr = ran_str
            product_img.pdu_img_name = imgfile['name']
            product_img.pdu_img_url = destination
            product_img.save()

        # Save Product table
        product.save()
        response_data = {'type':'success'}
    else:
        response_data = {'type':'failed'}
    return Response(response_data)
# end test register products

# Upload image
@api_view(['POST'])
def upload_testtour_img(request):
    if request.method == 'POST':
        # print("request.data", request.data)
        # print("request.FILES", request.FILES)
        files = request.FILES.getlist('uploaded_file')
        # print("files :", files)
        for file in files:
            # print("====file===")
            handle_test_uploaded_file(file)
        response_data = {'type':'success'}
        return Response(response_data)

def handle_test_uploaded_file(f):
    filename = f.name
    url = 'static/uploads/images/temp/'
    with open(url + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
# end
###################################################################################

@api_view(['POST'])
def get_modify_product(request):
    if request.method == 'POST':
        print(request.data)
        productId = request.data['productId']
        product = Product.objects.get(id=productId)
        ustr = product.pdu_ustr
        productImg = ProductImage.objects.filter(pdu_ustr=ustr)
        product_serializer = ProductSerializer(product)
        productimg_serializer = ProductImageSerializer(productImg, many=True)
        serializerData = []
        serializerData.append(product_serializer.data)
        serializerData.append(productimg_serializer.data)
        return Response(serializerData, status=200)

@api_view(['POST'])
def modify_product(request):
    if request.method == 'POST':
        print(request.data['values'])
        print(request.data['for_modify_id'])
        print(request.data['ustr'])
        print(request.data['meetingpoint'])
        productId = request.data['for_modify_id']
        productUstr = request.data['ustr']
        data = request.data['values']

        product = Product.objects.get(id=productId)

        product.pdu_name = data['tourname']
        product.pdu_type = data['tourtype']
        product.pdu_country = data['country']
        product.pdu_city = data['city']

        language = ','.join(data['language'])
        product.pdu_language = language

        product.pdu_brief_description = data['briefDesc']
        product.pdu_detailed_description = data['detailedDesc']
        product.pdu_hashtag = data['hashtag']

        product.pdu_meeting_time = data['meetingTime']
        product.pdu_duration = data['duration']
        product.pdu_location = data['meetingLocation']
        product.pdu_hottoget = data['howgetthere']
        product.pdu_price = data['price']
        product.pdu_price_include = data['priceIncluded']
        product.pdu_min_guest = data['minNumGuest']
        product.pdu_max_guest = data['maxNumGuest']
        product.pdu_season_from = request.data['seasondate_from']
        product.pdu_season_to = request.data['seasondate_to']

        notdays = ','.join(request.data['notAllowedDate'])
        product.pdu_unavailable_date = notdays

        product.pdu_additional_info = data['addNote']
        product.pdu_created_time = datetime.datetime.now()
        product.pdu_created_by = request.data['username']
        product.pdu_meeting_point_lat = request.data['meetingpoint']['lat']
        product.pdu_meeting_point_lng = request.data['meetingpoint']['lng']

        # uploadedFiles = request.data['uploadedFiles']
        # ProductImage.objects.filter(pdu_ustr=productUstr).delete()
        # for imgfile in uploadedFiles:
        #     # print(imgfile['name'])
        #     # product images save to table
        #     product_img = ProductImage()
        #     product_img.pdu_name = data['tourname']
        #     product_img.pdu_ustr = productUstr
        #     product_img.pdu_img_name = imgfile['name']
        #     product_img.pdu_img_url = 'static/uploads/images/products/' + productUstr
        #     product_img.save()

        product.save()
        response_data = {'type':'success'}
    else:
        response_data = {'type':'failed'}
    return Response(response_data)



@api_view(['POST'])
def upload_modify_tour_img(request):
    if request.method == 'POST':
        print("request.data", request.data)
        foldername = request.data['ustr']
        # print("request.FILES", request.FILES)
        files = request.FILES.getlist('uploaded_file')
        # print("files :", files)
        source = 'static/uploads/images/products/' + foldername + '/'
        rmfiles = os.listdir(source)
        for f in rmfiles:
            os.remove(source + f)

        for file in files:
            # print("====file===")
            modify_handle_test_uploaded_file(file, foldername)
        response_data = {'type':'success'}
        return Response(response_data)

def modify_handle_test_uploaded_file(f, foldername):
    filename = f.name
    url = 'static/uploads/images/products/' + foldername + '/'
    with open(url + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@api_view(['GET', 'POST'])
def mypage_profile_products(request):
    if request.method == 'POST':
        username = request.data['username']
        try:
            profile = Profile.objects.get(username=username)
            profile_serializers = ProfileSerializer(profile)
            products = Product.objects.filter(pdu_created_by=username)
            products_img_data = []
            serializered_data = []
            count_products = len(products)
            if count_products != 0 :
                for product in products:
                    ustr = product.pdu_ustr
                    front_img = ProductImage.objects.filter(pdu_ustr=ustr)[0]
                    # print(front_img)
                    products_img_data.append(front_img)
                    # print(products_img_data)
                product_serializers = ProductSerializer(products, many=True)
                product_img_serializers = ProductImageSerializer(products_img_data, many=True)
                # print("------: ", product_serializers.data)
                # print("======: ", product_img_serializers.data)
                serializered_data.append(product_serializers.data)
                serializered_data.append(product_img_serializers.data)
                serializered_data.append(profile_serializers.data)
                # return Response(product_serializers.data, product_img_serializers.data, status=200)
                return Response(serializered_data, status=200)
            else:
                response_data = "Nothing"
                serializered_data.append(response_data)
                serializered_data.append(profile_serializers.data)
                return Response(serializered_data, status=200)
        except Profile.DoesNotExist:
            response_data = "No profile"
            return Response(response_data, status=200)


@api_view(['POST'])
def get_profile_for_modify(request):
    if request.method == 'POST':
        username = request.data['username']
        profile = Profile.objects.get(username=username)
        profile_serializers = ProfileSerializer(profile)
        serializered_data = []
        serializered_data.append(profile_serializers.data)
        return Response(serializered_data, status=200)


@api_view(['POST'])
def save_modified_profile(request):
    if request.method == 'POST':
        username = request.data['username']
        data = request.data['values']
        profile = Profile.objects.get(username=username)
        language = ','.join(data['language'])
        visitCountry = ','.join(data['visitCountry'])
        nextCountry = ','.join(data['nextCountry'])
        profile.username = request.data['username']
        profile.name = data['name']
        profile.kakaoid = data['kakaoId']
        profile.introself = data['introSelf']
        profile.videoId = data['introvideo']
        profile.gender = data['gender']
        profile.interest = data['interest']
        profile.language = language
        profile.birthday = request.data['birthday']
        profile.major = data['major']
        profile.email = data['email']
        profile.cellnumber = data['phone']
        profile.emergency = data['emergency']
        profile.visited_country = visitCountry
        profile.afilliation = data['afilliation']
        profile.next_country = nextCountry
        profile.save()
        response_data = {'type':'success'}
        return Response(response_data)
        

@api_view(['GET'])
def show_tourpage_products(request):
    if request.method == 'GET':
        # seoul_products = Product.objects.filter(pdu_city='seoul')[:2]
        # busan_products = Product.objects.filter(pdu_city='busan')[:2]
        # jeju_products = Product.objects.filter(pdu_city='jeju')[:2]
        # gyeongju_products = Product.objects.filter(pdu_city='gyeongju')[:2]
        # jeonju_products = Product.objects.filter(pdu_city='jeonju')[:2]
        # daegu_products = Product.objects.filter(pdu_city='daegu')[:2]
        # other_products = Product.objects.filter(pdu_city='other')[:2]
        products = Product.objects.filter(pdu_show_tourpage=1)
        products_img_data = []
        serializered_data = []
        count_products = len(products)
        if count_products != 0:
            for product in products:
                ustr = product.pdu_ustr
                front_img = ProductImage.objects.filter(pdu_ustr=ustr)[0]
                products_img_data.append(front_img)
            product_serializers = ProductSerializer(products, many=True)
            product_img_serializers = ProductImageSerializer(products_img_data, many=True)
            serializered_data.append(product_serializers.data)
            serializered_data.append(product_img_serializers.data)
            return Response(serializered_data, status=200)
        else:
            response_data="nothing"
            return Response(response_data)


@api_view(['POST'])
def get_product_detail(request):
    if request.method == 'POST':
        product_id = request.data['product_id']
        products = Product.objects.get(id=product_id)
        ustr = products.pdu_ustr
        # get username profile 
        username = products.pdu_created_by
        profile = Profile.objects.get(username=username)
        profile_serializers = ProfileSerializer(profile)
        # get productImage
        ProductsImg = ProductImage.objects.filter(pdu_ustr=ustr)
        product_serializers = ProductSerializer(products)
        product_img_serializers = ProductImageSerializer(ProductsImg, many=True)
        serializered_data = []
        serializered_data.append(product_serializers.data)
        serializered_data.append(product_img_serializers.data)
        serializered_data.append(profile_serializers.data)
        return Response(serializered_data, status=200)



@api_view(['POST'])
def profile(request):
    if request.method == 'POST':
        print(request.data['values'])
        profile = Profile()
        data = request.data['values']
        language = ','.join(data['language'])
        visitCountry = ','.join(data['visitCountry'])
        nextCountry = ','.join(data['nextCountry'])
        profile.username = request.data['username']
        profile.name = data['name']
        profile.kakaoid = data['kakaoId']
        profile.introself = data['introSelf']
        if 'introvideo' in data:
            profile.videoId = data['introvideo']
        profile.gender = data['gender']
        profile.interest = data['interest']
        profile.language = language
        profile.birthday = request.data['birthday']
        profile.major = data['major']
        profile.email = data['email']
        profile.cellnumber = data['phone']
        profile.emergency = data['emergency']
        profile.visited_country = visitCountry
        profile.afilliation = data['afilliation']
        profile.next_country = nextCountry
        # profile.image
        uploaddirpath = 'static/uploads/images/profiles/' + request.data['username']
        os.makedirs(uploaddirpath)
        uploadedFiles = request.data['uploadedFiles']
        # move to file real directory
        source = 'static/uploads/images/temp/'
        destination = uploaddirpath
        files = os.listdir(source)
        for f in files:
            shutil.move(source + f, destination)
        for imgfile in uploadedFiles:
            profile.image = destination + "/" + imgfile['name']
        profile.save()
        response_data = {'type':'success'}
        return Response(response_data)


# Upload profile image
@api_view(['POST'])
def upload_profile_img(request):
    if request.method == 'POST':
        # print("request.data", request.data)
        # print("request.FILES", request.FILES)
        files = request.FILES.getlist('uploaded_file')
        # print("files :", files)
        for file in files:
            # print("====file===")
            handle_upload_profile_img(file)
        response_data = {'type':'success'}
        return Response(response_data)


def handle_upload_profile_img(f):
    filename = f.name
    url = 'static/uploads/images/temp/'
    with open(url + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



@api_view(['POST'])
def city_products(request):
    if request.method == 'POST':
        cityname = request.data['cityname']
        products = Product.objects.filter(pdu_city=cityname)
        products_img_data = []
        serializered_data = []
        count_products = len(products)
        if count_products != 0:
            for product in products:
                ustr = product.pdu_ustr
                front_img = ProductImage.objects.filter(pdu_ustr=ustr)[0]
                products_img_data.append(front_img)
            product_serializers = ProductSerializer(products, many=True)
            product_img_serializers = ProductImageSerializer(products_img_data, many=True)
            serializered_data.append(product_serializers.data)
            serializered_data.append(product_img_serializers.data)
            return Response(serializered_data, status=200)
        else:
            response_data = "Nothing"
            return Response(response_data, status=200)



@api_view(['POST'])
def booking_register(request):
    if request.method == 'POST':
        print(request.data)
        data = request.data['values']
        booker = Booker()
        booker.firstname = data['firstname']
        booker.lastname = data['lastname']
        booker.ages = data['agerange']
        booker.nationality = data['nationality']
        booker.gender = data['gender']
        language = ','.join(data['language'])
        booker.language = language
        booker.email = data['emailConfirm']
        booker.bookingDate = request.data['bookingdate']
        booker.cellNumber = data['phone']
        booker.mainSNS = data['mainSNS']
        booker.snsId = data['snsId']
        booker.numberPeople = data['numberOfPeople']
        booker.someNote = data['note']
        booker.save()
        response_data = {'type':'success'}
        return Response(response_data)

    
@api_view(['POST'])
def booking_summary(request):
    if request.method == 'POST':
        print(request.data)
        data = request.data['values']
        booking = Booking()
        booking.name = data['bookername']
        booking.email = data['email']
        booking.tourname = data['tourname']
        booking.tourdate = request.data['tourdate']
        booking.starttime = data['starttime']
        language = ','.join(data['language'])
        booking.language = language
        booking.numberPeople = data['numberOfPeople']
        booking.price = data['price']
        booking.save()
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['POST'])
def ask(request):
    if request.method == 'POST':
        print(request.data)
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['POST'])
def save_travel_article(request):
    if request.method == 'POST':
        # print(request.data)
        data = request.data['values']
        travel = Travel()
        travel.category = data['category']
        travel.name = data['name']
        travel.area = data['area']
        travel.writer = data['writer']
        travel.content = request.data['content']
        travel.lastUpdated = datetime.datetime.now()
        travel.save()
        key = travel.id
        travelforId = Travel.objects.get(id=key)
        travelforId.key = key
        travelforId.save()
        response_data = {'type':'success'}
        return Response(response_data)

@api_view(['POST'])
def modify_travel_article(request):
    if request.method == 'POST':
        data = request.data['values']
        content = request.data['content']
        articleId = request.data['articleId']
        travel = Travel.objects.get(id=articleId)
        travel.category = data['category']
        travel.name = data['name']
        travel.area = data['area']
        travel.writer = data['writer']
        travel.content = content
        travel.lastUpdated = datetime.datetime.now()
        travel.save()
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['GET'])
def get_travelArticle(request):
    if request.method == 'GET':
        travel = Travel.objects.all().order_by('-id')
        travel_serializer = TravelSerializer(travel, many=True)
        return Response(travel_serializer.data, status=200)


@api_view(['POST'])
def del_travelArticle(request):
    if request.method == 'POST':
        print(request.data['key'])
        Travel.objects.filter(key=request.data['key']).delete()
        response_data = "del success"
        return Response(response_data, status=200)


@api_view(['POST'])
def get_travelArticle_byId(request):
    if request.method == 'POST':
        print(request.data['id'])
        travelarticle = Travel.objects.get(key=request.data['id'])
        travelarticle.view += 1
        travelarticle.save()
        travelarticle_serializer = TravelSerializer(travelarticle)
        travelcomment = TravelComment.objects.filter(articleId=request.data['id']).order_by('id')
        travelcomment_serializer = TravelCommentSerializer(travelcomment, many=True)
        serializerData = []
        serializerData.append(travelarticle_serializer.data)
        serializerData.append(travelcomment_serializer.data)
        return Response(serializerData, status=200)


@api_view(['POST'])
def save_travel_article_comment(request):
    if request.method == 'POST':
        print(request.data)
        name = request.data['values']['name']
        password = request.data['values']['password']
        comment = request.data['values']['comment']
        articleId = request.data['articleId']
        user = User.objects.filter(username=name,password=password)
        if len(user) != 0:
            travelcomment = TravelComment()
            travelcomment.name = name
            travelcomment.comment = comment
            travelcomment.lastUpdated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            travelcomment.articleId = articleId
            travelcomment.save()
            travelcomment = TravelComment.objects.filter().order_by('-id')[0]
            travelcomment_serializer = TravelCommentSerializer(travelcomment)
            return Response(travelcomment_serializer.data, status=200)
        else:
            return Response("no permission")


@api_view(['POST'])
def save_event_article(request):
    if request.method == 'POST':
        # print(request.data)
        data = request.data['values']
        event = Event()
        event.area = data['area']
        event.name = data['name']
        event.content = request.data['content']
        event.lastUpdated = datetime.datetime.now()
        # period = request.data['period'][0] + '~' + request.data['period'][1]
        event.period_from = request.data['period'][0]
        event.period_to = request.data['period'][1]
        event.save()
        key = event.id
        eventforId = Event.objects.get(id=key)
        eventforId.key = key
        eventforId.save()
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['POST'])
def modify_event_article(request):
    if request.method == 'POST':
        print(request.data['values'])
        data = request.data['values']
        content = request.data['content']
        articleId = request.data['articleId']
        event = Event.objects.get(id=articleId)
        event.area = data['area']
        event.name = data['name']
        if len(request.data['period']) != 0:
            period_from = request.data['period'][0]
            period_to = request.data['period'][1]
            event.period_from = period_from
            event.period_to = period_to
        event.content = request.data['content']
        event.lastUpdated = datetime.datetime.now()
        event.save()
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['GET'])
def get_eventArticle(request):
    if request.method == 'GET':
        event = Event.objects.all().order_by('-id')
        event_serializer = EventSerializer(event, many=True)
        return Response(event_serializer.data, status=200)

@api_view(['POST'])
def del_eventArticle(request):
    if request.method == 'POST':
        print(request.data['key'])
        Event.objects.filter(key=request.data['key']).delete()
        response_data = "del success"
        return Response(response_data, status=200)


@api_view(['POST'])
def get_eventArticle_byId(request):
    if request.method == 'POST':
        print(request.data['id'])
        eventarticle = Event.objects.get(key=request.data['id'])
        eventarticle.view += 1
        eventarticle.save()
        eventarticle_serializer = EventSerializer(eventarticle)
        eventcomment = EventComment.objects.filter(articleId=request.data['id']).order_by('id')
        eventcomment_serializer = EventCommentSerializer(eventcomment, many=True)
        serializerData = []
        serializerData.append(eventarticle_serializer.data)
        serializerData.append(eventcomment_serializer.data)
        return Response(serializerData, status=200)


@api_view(['POST'])
def save_event_article_comment(request):
    if request.method == 'POST':
        print(request.data)
        name = request.data['values']['name']
        password = request.data['values']['password']
        comment = request.data['values']['comment']
        articleId = request.data['articleId']
        user = User.objects.filter(username=name,password=password)
        if len(user) != 0:
            eventcomment = EventComment()
            eventcomment.name = name
            eventcomment.comment = comment
            eventcomment.lastUpdated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            eventcomment.articleId = articleId
            eventcomment.save()
            eventcomment = EventComment.objects.filter().order_by('-id')[0]
            eventcomment_serializer = EventCommentSerializer(eventcomment)
            return Response(eventcomment_serializer.data, status=200)
        else:
            return Response("no permission")


@api_view(['POST'])
def save_local_article(request):
    if request.method == 'POST':
        print(request.data)
        data = request.data['values']
        local = LocalCommunity()
        local.category = data['category']
        local.title = data['title']
        local.area = data['area']
        local.writer = request.data['writer']
        local.content = request.data['content']
        local.lastUpdated = datetime.datetime.now()
        local.save()
        key = local.id
        localforId = LocalCommunity.objects.get(id=key)
        localforId.key = key
        localforId.save()
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['GET'])
def get_localArticle(request):
    if request.method == 'GET':
        local = LocalCommunity.objects.all().order_by('-id')
        local_serializer = LocalSerializer(local, many=True)
        return Response(local_serializer.data, status=200)


@api_view(['POST'])
def get_localArticle_byId(request):
    if request.method == 'POST':
        print(request.data['id'])
        localarticle = LocalCommunity.objects.get(key=request.data['id'])
        localarticle.view += 1
        localarticle.save()
        localarticle_serializer = LocalSerializer(localarticle)
        localcomment = LocalComment.objects.filter(articleId=request.data['id']).order_by('id')
        localcomment_serializer = LocalCommentSerializer(localcomment, many=True)
        serializerData = []
        serializerData.append(localarticle_serializer.data)
        serializerData.append(localcomment_serializer.data)
        return Response(serializerData, status=200)

@api_view(['POST'])
def del_localArticle(request):
    if request.method == 'POST':
        print(request.data['key'])
        LocalCommunity.objects.filter(key=request.data['key']).delete()
        response_data = "del success"
        return Response(response_data, status=200)


@api_view(['POST'])
def modify_local_article(request):
    if request.method == 'POST':
        data = request.data['values']
        content = request.data['content']
        articleId = request.data['articleId']
        localcommunity = LocalCommunity.objects.get(id=articleId)
        localcommunity.category = data['category']
        localcommunity.title = data['title']
        localcommunity.area = data['area']
        localcommunity.content = content
        localcommunity.lastUpdated = datetime.datetime.now()
        localcommunity.save()
        response_data = {'type':'success'}
        return Response(response_data)


@api_view(['POST'])
def save_local_article_comment(request):
    if request.method == 'POST':
        print(request.data)
        name = request.data['values']['name']
        password = request.data['values']['password']
        comment = request.data['values']['comment']
        articleId = request.data['articleId']
        user = User.objects.filter(username=name,password=password)
        if len(user) != 0:
            localcomment = LocalComment()
            localcomment.name = name
            localcomment.comment = comment
            localcomment.lastUpdated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            localcomment.articleId = articleId
            localcomment.save()
            localcomment = LocalComment.objects.filter().order_by('-id')[0]
            localcomment_serializer = LocalCommentSerializer(localcomment)
            return Response(localcomment_serializer.data, status=200)
        else:
            return Response("no permission")


@api_view(['GET'])
def get_admin_product(request):
    if request.method == 'GET':
        product = Product.objects.all()
        product_serializer = ProductSerializer(product, many=True)
        return Response(product_serializer.data, status=200)


@api_view(['GET'])
def get_admin_user(request):
    if request.method == 'GET':
        user = User.objects.filter(is_superuser=0)
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data, status=200)


@api_view(['GET'])
def get_admin_foreignUser(request):
    if request.method == 'GET':
        booker = Booker.objects.all()
        booker_serializer = BookerSerializer(booker, many=True)
        return Response(booker_serializer.data, status=200)


@api_view(['GET'])
def get_admin_bookinglist(request):
    if request.method == 'GET':
        booking = Booking.objects.all()
        booking_serializer = BookingSerializer(booking, many=True)
        return Response(booking_serializer.data, status=200)


@api_view(['POST'])
def show_tour_program_page(request):
    if request.method == 'POST':
        print(request.data)
        data = request.data['value']
        val, id = data.split(" ")
        print(val, id)
        product = Product.objects.get(id=id)
        product.pdu_show_tourpage = val
        product.save()
        response_data = "success"
        return Response(response_data, status=200)
