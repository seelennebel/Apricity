from flask import Flask, request
from flask import render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from word_cloud import Word_Cloud

from apricity_server.py import app, main_page, success, form_page