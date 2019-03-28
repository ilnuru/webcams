import requests
from django.contrib import admin

# Register your models here.

from .models import Address, House, Camera
from .utils import get_camera_link, get_rtsp_link



class CameraAdmin(admin.ModelAdmin):
	actions = ['update_rtsp']
	def update_rtsp(self, request, queryset):
		for camera in queryset:
			link = get_camera_link(camera)
			rtsp_link = get_rtsp_link(link)
			camera.rtsp_link = rtsp_link
			camera.save()
		self.message_user(request, 'Ссылки обновлены')
			
	update_rtsp.short_description = 'Обновить RTSP ссылки'

admin.site.register(Address)
admin.site.register(House)
admin.site.register(Camera, CameraAdmin)
