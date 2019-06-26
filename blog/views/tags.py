from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages

from ..utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from ..forms import TagForm
from ..models import *


# tags
def tags(request):
    return render(request, 'tags.html', context={})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'tag_update.html'


class TagDeleteView(View):
    def get(self, request, tag_id):
        Tag.objects.filter(id=tag_id).delete()
        messages.success(request, 'Selected tag has been deleted!')
        return HttpResponseRedirect(reverse('tags'))
