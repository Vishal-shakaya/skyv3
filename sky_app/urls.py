
from django.urls import path
from sky_app import views
from django.conf.urls.static import static
from django.conf import settings
from SkyProject import settings as sett

urlpatterns = [
    path('', views.HomvView, name='home_view'),
    path('create-card/<pk>/', views.CreateCardView, name='create_card'),
    path('card-detail/<pk>/', views.CardDetailView, name='card_detail'),
    path('card-list/', views.CardListView, name='card_list'),
    path('feedback/', views.FeedbackView, name='feedback'),
    path('our-word/', views.OurWorkView, name='our_work'),
    path('our-story/', views.OurStoryView, name='our_story'),
    path('on-demnad/', views.OnDemandView, name='on_demand'),
    path('about/', views.AboutView, name='about'),
    path('campaign/', views.CampaignView, name='campaing'),
    path('authview/', views.AuthView, name='auth'),
    path('signup/', views.SignupHandler, name='signup'),
    path('login/', views.LoginHandler, name='login'),
    path('delete-card/<pk>', views.DeleteCardManager, name='delete_card'),
    path('logout/', views.LogoutUser, name='logout_user'),
    path('create-card-handler/', views.CreateCardHandler,
         name='create_card_handler'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if sett.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
