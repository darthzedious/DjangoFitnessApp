from django.views.generic import TemplateView


class TrainingsView(TemplateView):
    template_name = "training/training_template.html"
