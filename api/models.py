from django.db import models


class Product(models.Model):
    pdu_ustr = models.CharField(max_length=200)
    pdu_name = models.CharField(max_length=200)
    pdu_type = models.CharField(max_length=200)
    pdu_country = models.CharField(max_length=200)
    pdu_city = models.CharField(max_length=200)
    pdu_language = models.CharField(max_length=200)
    pdu_brief_description = models.TextField(blank=True, null=True)
    pdu_detailed_description = models.TextField(blank=True, null=True)
    pdu_hashtag = models.CharField(max_length=600)
    pdu_meeting_time = models.CharField(max_length=100)
    pdu_duration = models.CharField(max_length=100)
    pdu_location = models.CharField(max_length=600)
    pdu_meeting_point_lat = models.CharField(max_length=200)
    pdu_meeting_point_lng = models.CharField(max_length=200)
    pdu_hottoget = models.TextField(blank=True, null=True)
    pdu_price = models.IntegerField(default=0)
    pdu_price_include = models.CharField(max_length=600)
    pdu_min_guest = models.IntegerField(default=0)
    pdu_max_guest = models.IntegerField(default=0)
    pdu_season_from = models.DateField(blank=True, null=True)
    pdu_season_to = models.DateField(blank=True, null=True)
    pdu_unavailable_date = models.CharField(max_length=200)
    pdu_additional_info = models.TextField(blank=True, null=True)
    pdu_created_time =  models.DateTimeField(blank=True, null=True)
    pdu_created_by = models.CharField(max_length=200)
    pdu_show_tourpage = models.IntegerField(null=True)
    pdu_recommended = models.IntegerField(null=True)



class ProductImage(models.Model):
    pdu_ustr = models.CharField(max_length=200)
    pdu_name = models.CharField(max_length=200)
    pdu_img_name = models.CharField(max_length=200)
    pdu_img_url = models.URLField(max_length=600)
    main_img = models.BooleanField(null=True)


class City(models.Model):
    city_name = models.CharField(max_length=200)
    city_img_bar_url = models.URLField(max_length=600)
    city_video_url = models.URLField(max_length=600)
    city_description = models.CharField(max_length=600)


class Profile(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    kakaoid = models.CharField(max_length=200)
    image = models.URLField(max_length=600)
    introself = models.TextField(blank=True, null=True)
    videoId = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=100)
    interest = models.CharField(max_length=600)
    language = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    major = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    cellnumber = models.CharField(max_length=200)
    emergency = models.CharField(max_length=200)
    afilliation = models.CharField(max_length=200)
    visited_country = models.CharField(max_length=200)
    next_country = models.CharField(max_length=200)


class Booker(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    ages = models.CharField(max_length=50)
    nationality = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    language = models.CharField(max_length=600)
    email = models.EmailField(max_length=200)
    bookingDate = models.DateField(blank=True, null=True)
    cellNumber = models.CharField(max_length=200)
    mainSNS = models.CharField(max_length=200, null=True)
    snsId = models.CharField(max_length=200, null=True)
    numberPeople = models.IntegerField(default=0)
    someNote = models.TextField(null=True)


class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    tourname = models.CharField(max_length=200)
    tourdate = models.DateField(blank=True, null=True)
    starttime = models.CharField(max_length=200)
    language = models.CharField(max_length=600)
    numberPeople = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    

class Travel(models.Model):
    key = models.IntegerField(default=0)
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    lastUpdated = models.DateField(blank=True, null=True)
    view = models.IntegerField(default=0)


class TravelComment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True)
    lastUpdated = models.DateTimeField(blank=True)
    articleId = models.IntegerField(default=0)
    parentId = models.IntegerField(default=0)


class Event(models.Model):
    key = models.IntegerField(default=0)
    area = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    period_from = models.DateField(blank=True, null=True)
    period_to = models.DateField(blank=True, null=True)
    content = models.TextField(null=True)
    view = models.IntegerField(default=0)
    lastUpdated = models.DateField(blank=True, null=True)


class EventComment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True)
    lastUpdated = models.DateTimeField(blank=True)
    articleId = models.IntegerField(default=0)
    parentId = models.IntegerField(default=0)


class LocalCommunity(models.Model):
    key = models.IntegerField(default=0)
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=600)
    area = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    lastUpdated = models.DateField(blank=True, null=True)
    view = models.IntegerField(default=0)


class LocalComment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True)
    lastUpdated = models.DateTimeField(blank=True)
    articleId = models.IntegerField(default=0)
    parentId = models.IntegerField(default=0)


class SocialUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    socialId = models.CharField(max_length=200)
    socialName = models.CharField(max_length=200)
    joinTime = models.DateTimeField(blank=True, null=True)




