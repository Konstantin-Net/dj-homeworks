from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    # В form.cleaned_data будет словарь с данными
    # каждой отдельной формы, которые вы можете проверить
    # form.cleaned_data
    # вызовом исключения ValidationError можно указать админке о наличие ошибки
    # таким образом объект не будет сохранен,
    # а пользователю выведется соответствующее сообщение об ошибке
    # raise ValidationError('Тут всегда ошибка')
    def clean(self):
        count_is_main = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count_is_main += 1
        if count_is_main == 0:
            raise ValidationError('Укажите один основной раздел')
        elif count_is_main > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    pass


@admin.register(Tag)
class TagsArticle(admin.ModelAdmin):
    pass
