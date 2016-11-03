from django.shortcuts import get_object_or_404

from community.models import Community, Membership, Application, Invitation
from badge.models import BadgeClass, BadgeInstance

def community_object(community_tag):
    # this commounity, based on tag
    try:
       community = Community.objects.get(tag=community_tag)
    except Community.DoesNotExist:
       community = None
    return community

def all_community_applications(community):
    # all community applications
    all_applications = Application.objects.filter(
        community=community,
    )
    return all_applications

def u_application(community, user):
    # user's application
    try:
       application = Application.objects.get(
           community=community,
           applicant=user,
       )
    except Application.DoesNotExist:
       application = None
    return application

def all_community_memberships(community):
    # all community memberships
    all_memberships = Membership.objects.filter(
        community=community,
    )
    return all_memberships

def u_membership(community, user):
    # user's membership return first object or none
    try:
       membership = Membership.objects.get(community=community, user=user)
    except Membership.DoesNotExist:
       membership = None
    return membership

def all_community_badge_classes(community):
    # all community badgeclasses
    all_badges = BadgeClass.objects.filter(
        community=community,
    )
    return all_badges

def u_invitation(community, user):
    # user's invitation return first object or none
    try:
       invitation = Invitation.objects.get(
           community=community,
           recipient=user,
       )
    except Invitation.DoesNotExist:
       invitation = None
    return invitation

def all_community_invitations(community):
    # all community invitations
    all_invitations = Invitation.objects.filter(
        community=community,
    )
    return all_invitations