from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings
from sitetree.sitetreeapp import register_i18n_trees

from client.api.views import *
from .views import *


def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    path('', login_required(DashboardView.as_view()), name='home'),

    # macrogroups urls
    path('macrogroups/', login_required(MacroGroupListView.as_view()), name='macrogroup-list'),
    path('macrogroups/add/', login_required(MacroGroupCreateView.as_view()), name='macrogroup-add'),
    path('macrogroups/update/<slug:slug>/', login_required(MacroGroupUpdateView.as_view()),
        name='macrogroup-update'),
    path('macrogroups/delete/<slug:slug>/', login_required(MacroGroupDeleteView.as_view()),
        name='macrogroup-delete'),
    path('macrogroups/<slug:slug>/', login_required(MacroGroupDetailView.as_view()),
        name='macrogroup-detail'),

    # group urls
    path('groups/', login_required(GroupListView.as_view()), name='group-list'),
    path('groups/add/', login_required(GroupCreateView.as_view()), name='group-add'),
    path('groups/update/<slug:slug>/', login_required(GroupUpdateView.as_view()), name='group-update'),
    path('groups/delete/<slug:slug>/', login_required(GroupDeleteView.as_view()), name='group-delete'),
    path('groups/<slug:slug>/', login_required(GroupDetailView.as_view()), name='group-detail'),
    path('jx/groups/<slug:slug>/setpanoramic/<project_type>/<int:project_id>/',
        login_required(GroupSetProjectPanoramicView.as_view()), name='group-set-project-panoramic'),
    path('jx/groups/<slug:slug>/setpanoramic/<project_type>/<project_id>/',
        login_required(GroupSetProjectPanoramicView.as_view()), name='group-set-project-panoramic'),

    # project urls
    path('groups/<slug:group_slug>/projects/', login_required(ProjectListView.as_view()),
        name='project-list'),

    path('generalsuitedata/', login_required(GeneralSuiteDataUpdateView.as_view()), name='generaldata-update'),
    path('search/', login_required(SearchAdminView.as_view()), name='search-admin')



]

