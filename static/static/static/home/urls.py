from django.urls import path 
from . import views


urlpatterns = [
    
    # Home Views 
    path('', views.index),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name="index2"),
    path('index3/', views.index3, name="index3"),
    path('index4/', views.index4, name="index4"),
    path('index5/', views.index5, name="index5"),
    path('index6/', views.index6, name="index6"),
    path('index7/', views.index7, name="index7"),
    path('index8/', views.index8, name="index8"),
    path('index9/', views.index9, name="index9"),
    path('index10/', views.index10, name="index10"),
    path('blankpage/', views.blankpage, name='blankpage'),
    path('calendar/', views.calendar, name='calendar'),
    path('chat/', views.chat, name='chat'),
    path('chat-profile/', views.chatProfile, name='chatProfile'),
    path('comingsoon/', views.comingsoon, name='comingsoon'),
    path('email/', views.email, name='email'),
    path('faqs/', views.faqs, name='faqs'),
    path('gallery/', views.gallery, name='gallery'),
    path('kanban/', views.kanban, name='kanban'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('not-found/', views.notFound, name='notFound'),
    path('pricing/', views.pricing, name='pricing'),
    path('stared/', views.stared, name='stared'),
    path('terms-conditions/', views.termsAndConditions, name='termsAndConditions'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('view-details/', views.viewDetails, name='viewDetails'),
    path('widgets/', views.widgets, name='widgets'),
    
    
    # forms routes

    path('forms/form-validation', views.formValidation, name="formValidation"),
    path('forms/form-wizard', views.formWizard, name="formWizard"),
    path('forms/input-forms', views.inputForms, name="inputForms"),
    path('forms/input-layout', views.inputLayout, name="inputLayout"),

# invoices routes

    path('invoice/add-new', views.addNew, name='addNew'),
    path('invoice/edit', views.edit, name='edit'),
    path('invoice/list', views.list, name='invoiceList'),
    path('invoice/preview', views.preview, name='preview'),

# role and access routes

    path('role-access/assign-role', views.assignRole, name='assignRole'),
    path('role-access/role-access', views.roleAccess, name='roleAccess'),

#settings routes

    path('settings/company', views.company, name='company'),
    path('settings/currencies', views.currencies, name='currencies'),
    path('settings/languages', views.languages, name='languages'),
    path('settings/notification', views.notification, name='notification'),
    path('settings/notification-alert', views.notificationAlert, name='notificationAlert'),
    path('settings/payment-getway', views.paymentGetway, name='paymentGetway'),
    path('settings/theme', views.theme, name='theme'),

# tables routes

    path('tables/basic-table', views.basicTable, name='basicTable'),
    path('tables/data-table', views.dataTable, name='dataTable'),

#users routes

    path('users/add-user', views.addUser, name='addUser'),
    path('users/users-grid', views.usersGrid, name='usersGrid'),
    path('users/users-list', views.usersList, name='usersList'),
    path('users/view-profile', views.viewProfile, name='viewProfile'),
    
    
    # ai routes
    path('ai/code-generator', views.codeGenerator, name='codeGenerator'),
    path('ai/code-generatorNew', views.codeGeneratorNew, name='codeGeneratorNew'),
    path('ai/image-generator', views.imageGenerator, name='imageGenerator'),
    path('ai/text-generator', views.textGenerator, name='textGenerator'),
    path('ai/text-generator-new', views.textGeneratorNew, name='textGeneratorNew'),
    path('ai/video-generator', views.videoGenerator, name='videoGenerator'),
    path('ai/voice-generator', views.voiceGenerator, name='voiceGenerator'),


# authentication routes
    path('authentication/forgot-password', views.forgotPassword, name='forgotPassword'),
    path('authentication/signin', views.signin, name='signin'),
    path('authentication/signup', views.signup, name='signup'),

# blog routes
    path('blog/add-blog', views.addBlog, name='addBlog'),
    path('blog/blog', views.blog, name='blog'),
    path('blog/blog-details', views.blogDetails, name='blogDetails'),

# chart routes
    path('chart/column-chart', views.columnChart, name='columnChart'),
    path('chart/line-chart', views.lineChart, name='lineChart'),
    path('chart/pie-chart', views.pieChart, name='pieChart'),

# components routes
    path('components/alerts', views.alerts, name='alerts'),
    path('components/avatars', views.avatars, name='avatars'),
    path('components/badges', views.badges, name='badges'),
    path('components/button', views.button, name='button'),
    path('components/calendar', views.calendar, name='calendarMain'),
    path('components/card', views.card, name='card'),
    path('components/carousel', views.carousel, name='carousel'),
    path('components/colors', views.colors, name='colors'),
    path('components/dropdown', views.dropdown, name='dropdown'),
    path('components/list', views.list, name='list'),
    path('components/pagination', views.pagination, name='pagination'),
    path('components/progressbar', views.progressbar, name='progressbar'),
    path('components/radio', views.radio, name='radio'),
    path('components/star-ratings', views.starRatings, name='starRatings'),
    path('components/switch', views.switch, name='switch'),
    path('components/tab-accordion', views.tabAndAccordion, name='tabAndAccordion'),
    path('components/tags', views.tags, name='tags'),
    path('components/tooltip', views.tooltip, name='tooltip'),
    path('components/typography', views.typography, name='typography'),
    path('components/upload', views.upload, name='upload'),
    path('components/videos', views.videos, name='videos'),

# cryptoCurrency routes

    path('crypto-currency/marketplace', views.marketplace, name='marketplace'),
    path('crypto-currency/marketplace-details', views.marketplaceDetails, name='marketplaceDetails'),
    path('crypto-currency/portfolio', views.portfolio, name='portfolio'),
    path('crypto-currency/wallet', views.wallet, name='wallet'),
]


