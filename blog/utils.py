from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            messages.success(request, f'{new_obj} has been created!')
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            messages.success(request, f'{obj} has been updated!')
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

#
# class ObjectDeleteMixin:
#     model = None
#     redirect_url = None
#     template = None
#
#     def get(self, request, slug):
#         obj = self.model.objects.get(slug__iexact=slug)
#         return render(request, self.template, context={self.model.__name__.lower(): obj})
#
#     def post(self, request, slug):
#         obj = self.model.objects.get(slug__iexact=slug)
#         obj.delete()
#         messages.success(request, f'{obj} has been deleted!')
#         return redirect(reverse(self.redirect_url))
#
