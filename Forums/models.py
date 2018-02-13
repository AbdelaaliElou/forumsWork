#!/usr/bin/env python3
class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_member(self):
        print ('Name: {}\t\tAge: {}'.format(self.name, self.age))


class Post:
    def __init__(self, title, body, author_name, author_age):
        self.title = title
        self.body = body
        self.author = Member(author_name, author_age)   # Member

    def show_topic(self):
        print ('Title:{}\t\t\tAuthor{}\n{}'.format(self.title, self.author.name, self.body))

    # def show_author(self):
    #     print ('author name: {}\t\tauthor age: {}'.format(self.author.name, self.author.age))
