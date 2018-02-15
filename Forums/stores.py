#!/usr/bin/python
class MemberStore:

    members = []

    def __init__(self):
        pass

    def get_all(self):
        # get the list of all members
        return [(member.mem_id, member.name, member.age) for member in self.members]

    def add(self, member):
        # add member to the list
        # print member
        self.members.append(member)

    def get_by_id(self, id_member):
        # get member by id
        for member in self.members:
            if member.mem_id == id_member:
                return member
        return "Not found"
        # return [(member.mem_id, member.name, member.age) for member in self.members if (member.mem_id == id_member)]

    def update_member(self, member):
        old_mem = self.get_by_id(member.mem_id)
        if old_mem != "Not found":
            index = self.members.index(old_mem)
            old_mem.name = member.name
            old_mem.age = member.age
            self.members[index] = old_mem
            print 'updated'
            return True
        return False

    def delete(self, id_member):
        m = self.get_by_id(id_member)
        if m != "Not found":
            self.members.remove(m)
            print 'deleted!!'
        return m

    def is_exist(self, member):
        return self.get_by_id(member.mem_id) != "Not found"


class PostStore:

    posts = []

    def __init__(self):
        pass

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return [(post.author.name, post.title, post.body) for post in self.posts]

    def get_by_id(self, post_id):
        for post in self.posts:
            if post.post_id == post_id:
                return post
        return False

    def update_post(self, post):
        old_post = self.get_by_id(post.post_id)
        if old_post != "Not found":
            index = self.posts.index(old_post)
            old_post.title = post.title
            old_post.body = post.body
            self.posts[index] = old_post
            print 'updated'
            return True
        return False

    def delete(self, post_id):
        p = self.get_by_id(post_id)
        if p != "Not found":
            self.posts.remove(p)
            print 'deleted!!'
        return p

    def is_exist(self, post):
        return self.get_by_id(post.post_id) != "Not found"
