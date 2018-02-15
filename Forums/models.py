#!/usr/bin/env python3
class Member:
    def __init__(self, name, age, mem_id):
        self.name = name
        self.age = age
        self.mem_id = mem_id

    # def show_member(self):
    #    print ('Name: {}\t\tAge: {}'.format(self.name, self.age))
    def __str__(self):
        return 'Name: {}\t\tAge: {}'.format(self.name, self.age)


class Post:
    def __init__(self, title, body, author, post_id):
        self.title = title
        self.body = body
        self.author = author   # Member
        self.post_id = post_id

    # def show_topic(self):
    #    print ('Title:{}\t\t\tAuthor{}\n{}'.format(self.title, self.author.name, self.body))

    def show_author(self):
         print ('author name: {}\t\tauthor age: {}'.format(self.author.name, self.author.age))
