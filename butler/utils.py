from butler.models import ButlerPage



def create_pages_clean():
    if not ButlerPage.objects.filter(slug='order'):
        ButlerPage.objects.create(title="Главная", slug="main", content="")
        ButlerPage.objects.create(title="Заказ онлайн", slug="order", content="")
        ButlerPage.objects.create(title="FAQ", slug="faq", content="")
        ButlerPage.objects.create(title="Цены", slug="price", content="")
        ButlerPage.objects.create(title="Контакты", slug="contact", content="")
    if not ButlerPage.objects.filter(slug__startswith="clean"):
        ButlerPage.objects.create(title="Уборка автосалонов", slug="clean-car", content="")
        ButlerPage.objects.create(title="Уборка фитнес клубов", slug="clean-fit", content="")
        ButlerPage.objects.create(title="Уборка офисов, ТЦ и БЦ", slug="clean-office", content="")
        ButlerPage.objects.create(title="Уборка ТСЖ", slug="clean-tcj", content="")
        ButlerPage.objects.create(title="Уборка прилегающей территории", slug="clean-area", content="")
        ButlerPage.objects.create(title="Мойка фасадов и остекления", slug="clean-facades", content="")
        ButlerPage.objects.create(title="Комплексная уборка квартир", slug="clean-apartments", content="")
        ButlerPage.objects.create(title="Комплексная уборка коттеджей", slug="clean-cottages", content="")
        ButlerPage.objects.create(title="Генеральная уборка", slug="clean-out", content="")
        ButlerPage.objects.create(title="Уборка после ремонта", slug="clean-renovation", content="")

def create_pages_clean_admin(modeladmin, request, queryset):
    create_pages_clean()

create_pages_clean_admin.short_description = "Созадть страницы по умолчанию"