from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Avg
from patient.models import HealthVital, Patient  

User = get_user_model()


def blankpage(request):
    context={
        "title": "Blank Page",
        "subTitle": "Blank Page",
    }
    return render(request,"blankpage.html", context)
    
def calendar(request):
    context={
        "title": "Calendar",
        "subTitle": "Components / Calendar",
    }
    return render(request,"calendar.html", context)
    
def chat(request):
    context={
        "title": "Chat",
        "subTitle": "Chat",
    }
    return render(request,"chat.html", context)
    
def chatProfile(request):
    context={
        "title": "Chat",
        "subTitle": "Chat",
    }
    return render(request,"chatProfile.html", context)
    
def comingsoon(request):
    context={
        "title": "",
        "subTitle": "",
    }
    return render(request,"comingsoon.html", context)
    
def email(request):
    context={
        "title": "Email",
        "subTitle": "Components / Email",
    }
    return render(request,"email.html", context)
    
def faqs(request):
    context={
        "title": "Faq",
        "subTitle": "Faq",
    }
    return render(request,"faqs.html", context)
    
def gallery(request):
    context={
        "title": "Gallery",
        "subTitle": "Gallery",
    }
    return render(request,"gallery.html", context)
    
def index(request):
    context={
        "title": "Dashboard",
        "subTitle": "AI",
    }
    return render(request,"index.html", context)
    
def kanban(request):
    context={
        "title": "Kanban",
        "subTitle": "Kanban",
    }
    return render(request,"kanban.html", context)
    
def maintenance(request):
    context={
        "title": "",
        "subTitle": "",
    }
    return render(request,"maintenance.html", context)
    
def notFound(request):
    context={
        "title": "404",
        "subTitle": "404",
    }
    return render(request,"notFound.html", context)
    
def pricing(request):
    context={
        "title": "Pricing",
        "subTitle": "Pricing",
    }
    return render(request,"pricing.html", context)
    
def stared(request):
    context={
        "title": "Email",
        "subTitle": "Components / Email",
    }
    return render(request,"stared.html", context)
    
def termsAndConditions(request):
    context={
        "title": "Terms & Condition",
        "subTitle": "Terms & Condition",
    }
    return render(request,"termsAndConditions.html", context)
    
def testimonials(request):
    context={
        "title": "Testimonials",
        "subTitle": "Testimonials",
    }
    return render(request,"testimonials.html", context)
    
def viewDetails(request):
    context={
        "title": "Email",
        "subTitle": "Components / Email",
    }
    return render(request,"viewDetails.html", context)
    
def widgets(request):
    context={
        "title": "Widgets",
        "subTitle": "Widgets",
    }
    return render(request,"widgets.html", context)


@login_required(login_url="/users/login/")
def index8(request):
    # Get system statistics
    total_users = User.objects.count()
    total_patients = Patient.objects.count()  # Number of patients in the system

    # Get the average risk scores for each patient
    patient_risk_averages = (
        HealthVital.objects.values("patient")
        .annotate(
            avg_high_risk=Avg("high_risk_probability"),
            avg_low_risk=Avg("low_risk_probability")
        )
    )

    # Count patients based on their average risk scores
    high_risk_users = sum(1 for p in patient_risk_averages if p["avg_high_risk"] >= 0.5)
    low_risk_users = sum(1 for p in patient_risk_averages if p["avg_low_risk"] >= 0.5)

    # Assuming doctors are stored in the User model 
    total_doctors = User.objects.all().count()  
    context = {
        "title": "Dashboard",
        "subTitle": "Medical",
        "user": request.user,
        "total_users": total_users,
        "total_patients": total_patients,
        "high_risk_users": high_risk_users,
        "low_risk_users": low_risk_users,
        "total_doctors": total_doctors,
    }
    return render(request, "dashboard/index8.html", context)


def addNew(request):
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render(request, "invoice/addNew.html", context)
    
def edit(request):
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render(request, "invoice/edit.html", context)
    
def list(request):
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render(request, "invoice/list.html", context)
    
def preview(request):
    context={
        "title": "Invoice List",
        "subTitle": "Invoice List",
    }
    return render(request, "invoice/preview.html", context)

def codeGenerator(request):
    context={
        "title": "Code Generator",
        "subTitle": "Code Generator",
    }
    return render(request,"ai/codeGenerator.html", context)

def codeGeneratorNew(request):
    context={
        "title": "Code  Generator",
        "subTitle": "Code  Generator",
    }
    return render(request, "ai/codeGeneratorNew.html", context)

def imageGenerator(request):
    context={
        "title": "Image  Generator",
        "subTitle": "Image  Generator",
    }
    return render(request, "ai/imageGenerator.html", context)

def textGenerator(request):
    context={
        "title": "Text Generator",
        "subTitle": "Text Generator",
    }
    return render(request, "ai/textGenerator.html", context)

def textGeneratorNew(request):
    context={
        "title": "Text Generator",
        "subTitle": "Text Generator",
    }
    return render(request, "ai/textGeneratorNew.html", context)

def videoGenerator(request):
    context={
        "title": "Video Generator",
        "subTitle": "Video Generator",
    }
    return render(request, "ai/videoGenerator.html", context)

def voiceGenerator(request):
    context={
        "title": "Voice Generator",
        "subTitle": "Voice Generator",
    }
    return render(request, "ai/voiceGenerator.html", context)

def forgotPassword(request):
    return render(request, "authentication/forgotPassword.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signup(request):
    return render(request, "authentication/signup.html")

def addBlog(request):
    context={
        "title": "Add Blog",
        "subTitle": "Add Blog",
    }
    return render(request, "blog/addBlog.html", context)

def blog(request):
    context={
        "title": "Blog",
        "subTitle": "Blog",
    }
    return render(request, "blog/blog.html", context)

def blogDetails(request):
    context={
        "title": "Blog Details",
        "subTitle": "Blog Details",
    }
    return render(request, "blog/blogDetails.html", context)

def columnChart(request):
    context={
        "title": "Column Chart",
        "subTitle": "Components / Column Chart",
    }
    return render(request, "chart/columnChart.html", context)
    
def lineChart(request):
    context={
        "title": "Line Chart",
        "subTitle": "Components / Line Chart",
    }
    return render(request, "chart/lineChart.html", context)
    
def pieChart(request):
    context={
        "title": "Pie Chart",
        "subTitle": "Components / Pie Chart",
    }
    return render(request, "chart/pieChart.html", context)

def alerts(request):
    context={
        "title": "Alerts",
        "subTitle": "Components / Alerts",
    }
    return render(request, "components/alerts.html", context)
    
def avatars(request):
    context={
        "title": "Avatars",
        "subTitle": "Components / Avatars",
    }
    return render(request, "components/avatars.html", context)
    
def badges(request):
    context={
        "title": "Badges",
        "subTitle": "Components / Badges",
    }
    return render(request, "components/badges.html", context)
    
def button(request):
    context={
        "title": "Button",
        "subTitle": "Components / Button",
    }
    return render(request, "components/button.html", context)
    
def calendar(request):
    context={
        "title": "Calendar",
        "subTitle": "Components / Calendar",
    }
    return render(request, "components/calendar.html", context)
    
def card(request):
    context={
        "title": "Card",
        "subTitle": "Components / Card",
    }
    return render(request, "components/card.html", context)
    
def carousel(request):
    context={
        "title": "Carousel",
        "subTitle": "Components / Carousel",
    }
    return render(request, "components/carousel.html", context)
    
def colors(request):
    context={
        "title": "Colors",
        "subTitle": "Components / Colors",
    }
    return render(request, "components/colors.html", context)
    
def dropdown(request):
    context={
        "title": "Dropdown",
        "subTitle": "Components / Dropdown",
    }
    return render(request, "components/dropdown.html", context)
    
def list(request):
    context={
        "title": "List",
        "subTitle": "Components / List",
    }
    return render(request, "components/list.html", context)
    
def pagination(request):
    context={
        "title": "Pagination",
        "subTitle": "Components / Pagination",
    }
    return render(request, "components/pagination.html", context)
    
def progressbar(request):
    context={
        "title": "Progressbar",
        "subTitle": "Components / Progressbar",
    }
    return render(request, "components/progressbar.html", context)
    
def radio(request):
    context={
        "title": "Radio",
        "subTitle": "Components / Radio",
    }
    return render(request, "components/radio.html", context)
    
def starRatings(request):
    context={
        "title": "Star Ratings",
        "subTitle": "Components / Star Ratings",
    }
    return render(request, "components/starRatings.html", context)
    
def switch(request):
    context={
        "title": "Switch",
        "subTitle": "Components / Switch",
    }
    return render(request, "components/switch.html", context)
    
def tabAndAccordion(request):
    context={
        "title": "Tab & Accordion",
        "subTitle": "Components / Tab & Accordion",
    }
    return render(request, "components/tabAndAccordion.html", context)
    
def tags(request):
    context={
        "title": "Tags",
        "subTitle": "Components / Tags",
    }
    return render(request, "components/tags.html", context)
    
def tooltip(request):
    context={
        "title": "Tooltip & Popover",
        "subTitle": "Components / Tooltip & Popover",
    }
    return render(request, "components/tooltip.html", context)
    
def typography(request):
    context={
        "title": "Typography",
        "subTitle": "Components / Typography",
    }
    return render(request, "components/typography.html", context)
    
def upload(request):
    context={
        "title": "File Upload",
        "subTitle": "Components / File Upload",
    }
    return render(request, "components/upload.html", context)
    
def videos(request):
    context={
        "title": "Videos",
        "subTitle": "Components / Videos",
    }
    return render(request, "components/videos.html", context)

def marketplace(request):
    context={
        "title": "Market Place",
        "subTitle": "Market Place",
    }
    return render(request,"crypto_currency/marketplace.html", context)

def marketplaceDetails(request):
    context={
        "title": "Market Place Details",
        "subTitle": "Market Place Details",
    }
    return render(request,"crypto_currency/marketplaceDetails.html", context)

def portfolio(request):
    context={
        "title": "Portfolio",
        "subTitle": "Portfolio",
    }
    return render(request,"crypto_currency/portfolio.html", context)

def wallet(request):
    context={
        "title": "Wallet",
        "subTitle": "Wallet",
    }

def formValidation(request):
    context={
        "title": "Form Validation",
        "subTitle": "Form Validation",
    }
    return render(request,"forms/formValidation.html", context)

def formWizard(request):
    context={
        "title": "Wizard",
        "subTitle": "Wizard",
    }
    return render(request,"forms/formWizard.html", context)

def inputForms(request):
    context={
        "title": "Input Forms",
        "subTitle": "Input Forms",
    }
    return render(request,"forms/inputForms.html", context)

def inputLayout(request):
    context={
        "title": "Input Layout",
        "subTitle": "Input Layout",
    }
    return render(request,"forms/inputLayout.html", context)


def assignRole(request):
    context={
        "title": "Role & Access",
        "subTitle": "Role & Access",
    }
    return render(request, "roles_and_access/assignRole.html", context)

def roleAccess(request):
    context={
        "title": "Role & Access",
        "subTitle": "Role & Access",
    }
    return render(request, "roles_and_access/roleAccess.html", context)

def company(request):
    context={
        "title": "Company",
        "subTitle": "Settings - Company",
    }
    return render(request,"settings/company.html", context)

def currencies(request):
    context={
        "title": "Currrencies",
        "subTitle": "Settings - Currencies",
    }
    return render(request,"settings/currencies.html", context)

def languages(request):
    context={
        "title": "Languages",
        "subTitle": "Settings - Languages",
    }
    return render(request,"settings/languages.html", context)

def notification(request):
    context={
        "title": "Notification",
        "subTitle": "Settings - Notification",
    }
    return render(request,"settings/notification.html", context)

def notificationAlert(request):
    context={
        "title": "Notification Alert",
        "subTitle": "Settings - Notification Alert",
    }
    return render(request,"settings/notificationAlert.html", context)

def paymentGetway(request):
    context={
        "title": "Payment Getway",
        "subTitle": "Settings - Payment Getway",
    }
    return render(request,"settings/paymentGetway.html", context)

def theme(request):
    context={
        "title": "Theme",
        "subTitle": "Settings - Theme",
    }
    return render(request,"settings/theme.html", context)

def basicTable(request):
    context={
        "title": "Basic Table",
        "subTitle": "Basic Table",
    }
    return render(request, "table/basicTable.html", context)

def dataTable(request):
    context={
        "title": "Data Table",
        "subTitle": "Data Table",
    }
    return render(request, "table/dataTable.html", context)
