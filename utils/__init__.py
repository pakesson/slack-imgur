#!/usr/bin/python
# -*- coding: utf-8 -*-

def query_string_from_text(text):
    split_text = text.split(' ')
    if len(split_text) >= 2:
        return " ".join(split_text[1:])
