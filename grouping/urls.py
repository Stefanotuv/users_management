
from django.urls import path
from . import views
from .views import *
    # ProjectReviewSubmitView

from django.contrib.auth import views as auth_view

urlpatterns = [
    path("",HomeView.as_view(template_name='grouping/home_grouping.html'),name='home'),

    path("home/",HomeView.as_view(template_name='grouping/home_grouping.html'),name='home'),

    path('create_project/', ProjectCreateView.as_view(template_name='grouping/create.html'),name='createproject'),

    path("create_project/upload_from_file",
         ProjectCreateFromFileView.as_view(template_name='grouping/upload_from_file.html'),
         name='project_upload_from_file_view'),

    path("create_project/upload_from_file/<pk>",
         ProjectCreateFromFileView.as_view(template_name='grouping/upload_from_file.html'),
         name='project_upload_from_file_view'),

    path("create_project/review/<pk>",
         ProjectReviewView.as_view(template_name='grouping/review.html'),
         name='project_review_view'),

    path("create_project/reviewed/<pk>",
         ProjectReviewedView.as_view(template_name='grouping/reviewed.html'),
         name='project_reviewed_view'),

    path("create_project/submit/<pk>",
         ProjectSubmitView.as_view(template_name='grouping/submit.html'),
         name='project_submit_view'),

    path("analytics/<pk>",
         ProjectAnalyticsView.as_view(template_name='grouping/analytics_modified.html'),
         name='project_analytics_view'),

    path("analytics_select",
         ProjectAnalyticsSelectView.as_view(template_name='grouping/analytics_select.html'),
         name='project_analytics_select_view'),

    path('view_project/',ProjectListView.as_view(template_name='grouping/view.html'),name='viewlist'),

    path('view_project_details/<pk>',ProjectDetailsView.as_view(template_name='grouping/view_details.html'),name='viewdetails'),

    path("settings",
         ProjectSettingsView.as_view(template_name='grouping/settings.html'),
         name='project_settings_view'),

    path("constraints",
         ProjectConstraintsView.as_view(template_name='grouping/constraints.html'),
         name='project_constraints_view'),

    path("constraints_uploaded",
         ProjectUploadedConstraintsView.as_view(template_name='grouping/updated_constraints_table.html'),
         name='project_constraints_uploaded_view'),

    path("constraints_upload",
         ProjectUploadConstraintsView.as_view(template_name='grouping/update_constraints_table.html'),
         name='project_constraints_upload_view'),

    # path("constraints_upload/review",
    #      ProjectUploadConstraintsView.as_view(template_name='grouping/update_constraints_table_review.html'),
    #      name='project_constraints_upload_review_view'),
]