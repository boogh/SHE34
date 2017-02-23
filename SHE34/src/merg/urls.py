from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^project/(?P<pk>[0-9]+)/$', views.DesktopMerge.as_view(), name='merge-project-desktop'),
    url(r'^project/(?P<pk>[0-9]+)/Making-an-Evaluation-list$', views.EvaluationList.as_view(), name='making-evaluation-list'),
    url(r'^project/(?P<list_id>[0-9]+)/export-docx', views.exportDocFile, name='export-doc-file'),
    url(r'^project/(?P<list_id>[0-9]+)/export-html$', views.exportHtmlFile, name='export-html-file'),
    url(r'^project/(?P<list_id>[0-9]+)/export-csv$', views.exportCsvFile, name='export-csv-file'),
]