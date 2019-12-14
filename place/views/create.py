from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView
from place.forms import PlaceForm, PlaceFormset
from place.models import Place


class PlaceCreateView(CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'place/create.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


def add_post(request):
    form = PlaceForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        formset = PlaceFormset(request.POST, files=request.FILES, instance=post)  # 今回はファイルなのでrequest.FILESが必要
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('user:list')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['formset'] = PlaceFormset()

    return render(request, 'place/create.html', context)
