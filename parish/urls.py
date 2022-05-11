from django.urls import path
from parish import views
app_name = 'parish'

urlpatterns = [
    path("list/church/members", views.list_church_members,
         name="list_church_members"),
    path("add/church/member", views.add_church_member,
         name="add_church_member"),
    path("edit/church/<int:id>/member", views.edit_church_member,
         name="edit_church_member"),
    path("delete/church/<int:id>/member", views.delete_church_member,
         name="delete_church_member"),
    path("view/church/<int:id>/member", views.view_church_member,
         name="view_church_member"),
    path("list/member/contributions", views.list_member_contributions,
         name="list_member_contributions"),
    path("add/member/contribution", views.add_member_contribution,
         name="add_member_contribution"),
    path("add/member/contribution", views.add_member_contribution,
         name="add_member_contribution"),
    path("add/member/contribution/<int:id>/direct", views.add_member_contribution,
         name="add_member_contribution_direct"),
    path("edit/member/contribution/<int:id>", views.edit_member_contribution,
         name="edit_member_contribution"),
    path("delete/member/contribution/<int:id>", views.delete_member_contribution,
         name="delete_member_contribution"),
]

