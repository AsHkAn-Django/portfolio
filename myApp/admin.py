from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django import forms
from .models import Project


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'status': forms.RadioSelect  # Optional: display status choices horizontally
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and 'porn' in title.lower():
            raise forms.ValidationError('Titles containing "porn" or similar are not allowed.')
        return title


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    list_display = ('title', 'image_tag', 'address', 'colored_status', 'status')
    list_editable = ('status',)
    list_filter = ('status',)
    search_fields = ('title', 'address')
    ordering = ('-priority_order', 'pk')

    fieldsets = (
        (None, {
            'fields': (
                'title', 'image', 'image_tag', 'address', 'github_link',
                'tech_stack', 'priority_order',
            ),
        }),
        ('Additional Information', {
            'fields': ('description', 'status', 'slug', 'meta_title', 'meta_description',),
            'classes': ('collapse',)  # Optional: collapsible extra info
        }),
    )
    readonly_fields = ('image_tag',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Project Title"
        return form

    def image_tag(self, obj):
        """Display image thumbnail in admin panel."""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 70px; border-radius: 6px;" />')
        return format_html('<span style="color: #888;">No image</span>')

    image_tag.short_description = 'Preview'

    def colored_status(self, obj):
        """Return status with a colored label."""
        color_map = {
            Project.Status.PUBLISHED: 'green',
            Project.Status.DRAFT: 'orange',
        }
        color = color_map.get(obj.status, 'red')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_status_display()
        )

    colored_status.short_description = 'Status'
    colored_status.admin_order_field = 'status'
