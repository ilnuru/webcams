from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, FormView

from .models import Camera, House

class BaseTemplateView(TemplateView):
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(BaseTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['houses'] = House.objects.all().order_by('name')
        return ctx

#
# class BaseFormView(FormView):
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(BaseFormView, self).dispatch(request, *args, **kwargs)


class IndexView(BaseTemplateView):
    template_name = 'cams/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx

    def get(self, request, *args, **kwargs):
        house = House.objects.first()
        if house:
            return redirect(reverse('cams', kwargs={'house_id': house.pk}))
        return super(IndexView, self).get(request, *args, **kwargs)

class CamsView(BaseTemplateView):
    template_name = 'cams/index.html'

    def get_context_data(self, house_id=0, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['house'] = House.objects.filter(pk=house_id).first()
        order = self.request.GET.get('order', 'ask')
        cam_type = self.request.GET.get('type', 'all')

        cam_filter = {}
        if cam_type == 'in':
            cam_filter['cam_type'] = Camera.INSIDE
        elif cam_type == 'out':
            cam_filter['cam_type'] = Camera.OUTSIDE

        order_by = ('entrance', 'number') if order == 'ask' else ('-entrance', 'number')

        ctx['cams'] = Camera.objects.filter(house_id=house_id, **cam_filter).order_by(*order_by)
        return ctx