#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import os
import random
import re
from utils import query_string_from_text

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

app = Flask(__name__)

subreddit_pattern = re.compile("^/r/(\w+)/?$")

def random_link_from_gallery_list(gallery_list, client):
    if not gallery_list:
        return None

    choice = random.choice(gallery_list)

    if choice.is_album:
        images = client.get_album_images(choice.id)
        choice = random.choice(images)

    return choice.link

def first_link_from_gallery_list(gallery_list, client):
    if not gallery_list:
        return None

    choice = gallery_list[0]

    if choice.is_album:
        images = client.get_album_images(choice.id)
        choice = images[0]

    return choice.link

def get_imgur_image(text):
    client_id = os.environ.get('IMGUR_CLIENT_ID')
    client_secret = os.environ.get('IMGUR_CLIENT_SECRET')

    if client_id and client_secret:
        client = ImgurClient(client_id, client_secret)

        query_string = query_string_from_text(text)
        subreddit_match = subreddit_pattern.match(query_string)

        if subreddit_match:
            subreddit = subreddit_match.group(1)
            result = client.subreddit_gallery(subreddit)
            result = random_link_from_gallery_list(result, client)
        else:
            result = client.gallery_search(query_string, sort='top')
            result = first_link_from_gallery_list(result, client)

        if not result:
            return "No matching image found"

        return result


@app.route('/', methods=['GET', 'POST'])
def return_imgur_image():
    if request.method == 'POST':
        text = request.form['text']
        req = {'text': get_imgur_image(text)}
        return jsonify(**req)
    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
