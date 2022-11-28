from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test, name='index'),
    path('signup', views.signup),
    path('signin', views.signin),
    path('social_login', views.social_login),

    path('register_product', views.register_product),
    path('upload_tour_img', views.upload_tour_img),
    path('remove_uploaded_img', views.remove_uploaded_img),
    path('upload_testtour_img', views.upload_testtour_img),
    path('test_register_product', views.test_register_product),

    path('get_modify_product', views.get_modify_product),
    path('upload_modify_tour_img', views.upload_modify_tour_img),
    path('modify_product', views.modify_product),
    
    path('profile', views.profile),
    path('upload_profile_img', views.upload_profile_img),

    path('booking_register', views.booking_register),
    path('booking_summary', views.booking_summary),

    path('ask', views.ask),

    path('mypage_profile_products', views.mypage_profile_products),
    path('get_profile_for_modify', views.get_profile_for_modify),
    path('save_modified_profile', views.save_modified_profile),
    path('get_product_detail', views.get_product_detail),

    path('show_tourpage_products', views.show_tourpage_products),

    path('city_products', views.city_products),

    path('save_travel_article', views.save_travel_article),
    path('get_travelArticle_byId', views.get_travelArticle_byId),
    path('modify_travel_article', views.modify_travel_article),
    path('save_travel_article_comment', views.save_travel_article_comment),

    path('save_event_article', views.save_event_article),
    path('get_eventArticle_byId', views.get_eventArticle_byId),
    path('modify_event_article', views.modify_event_article),
    path('save_event_article_comment', views.save_event_article_comment),

    path('save_local_article', views.save_local_article),
    path('get_localArticle', views.get_localArticle),
    path('get_localArticle_byId', views.get_localArticle_byId),
    path('save_local_article_comment', views.save_local_article_comment),
    
    # Admin api
    path('get_travelArticle', views.get_travelArticle),
    path('del_travelArticle', views.del_travelArticle),

    path('get_eventArticle', views.get_eventArticle),
    path('del_eventArticle', views.del_eventArticle),

    path('del_localArticle', views.del_localArticle),
    path('modify_local_article', views.modify_local_article),
    
    path('get_admin_product', views.get_admin_product),
    path('get_admin_user', views.get_admin_user),
    path('get_admin_foreignUser', views.get_admin_foreignUser),
    path('get_admin_bookinglist', views.get_admin_bookinglist),
    
    path('show_tour_program_page', views.show_tour_program_page),
]
