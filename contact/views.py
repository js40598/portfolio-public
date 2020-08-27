from django.shortcuts import render, redirect, get_object_or_404
from pages.models import Page, Skill
from django.core.mail import send_mail

from projects.models import Subpage, Project
from .models import Message
from django.contrib import messages

# Create your views here.

