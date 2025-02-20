#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import git

class ListCursor:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def move_next(self):
        if self.index < len(self.lst) - 1:
            self.index += 1

    def move_prev(self):
        if self.index > 0:
            self.index -= 1

    def get_value(self):
        return self.lst[self.index]


class GitOps:
    def __init__(self, repo_path):
        self.repo = git.Repo(repo_path)

        # zero_tag_name: The last "good" tag on the master branch
        # self.zero_tag_name = zero_tag_name
        # self.zero_commit = self.repo.commit(self.zero_tag_name)
        self.zero_tag = None
        self.active_branch_name = self.repo.active_branch.name        # master if you are ondefault
        self.rename_prefix = 'xx'

        self.tags = []
        self.tags_detached = []

        self.get_tag_lists()
        self.cursor = ListCursor(self.tags_detached)
        self.cursor.move_next()      # move pointer to the first tag after the zero tag

    def get_tag_lists(self):
        self.tags = sorted(self.repo.tags, key=lambda t: t.commit.committed_date, reverse=True)
        self.tags_detached = [tag for tag in self.tags if not tag.is_detached]

    def guess_zero_tag(self):
        previous_tag = None
        for tag in self.tags:
            if tag.is_detached:
                self.zero_tag = previous_tag
                return
            else:
                previous_tag = tag
        return None     # if there was no detached tag

    # def get_next_tag_from_tag_infos_list(self):
    #     try:
    #         index = self.tags_detached.keys().index(self.pointer_tag.name)
    #         if index + 1 < len(self.tags_detached.keys()):
    #             self.pointer_tag.name = self.tags_detached.keys()[index + 1]
    #             return self.tags_detached[index + 1]
    #         else:
    #             return None
    #     except ValueError:
    #         return None

    def get_tag_count_distance_to_zero_tag(self, next_tag):
        pass


    def rename_tag_with_prefix(self, original_tagname):
        new_tag = f"{self.rename_prefix}{original_tagname}"
        commit = self.repo.commit(original_tagname)
        self.repo.create_tag(new_tag, commit)
        self.repo.delete_tag(original_tagname)

    def retag_on_active_branch(self):
        for tag in self.tags_detached:
            distance = self.get_tag_count_distance_to_zero_tag(tag)
            tagname = tag.name
            self.rename_tag_with_prefix(tagname)




    # def get_tag_distances(self):
    #     # tags = sorted(self.repo.tags, key=lambda t: t.commit.committed_date, reverse=True)
    #     for tag in self.tags:
    #         if tag.name != self.zero_tag_name:
    #             self.tags_detached[tag.name] = self.get_distance_between_tags(self.zero_tag_name, tag.name)





    def delete_all_tags(self, skip_prefix):
        for tag in self.repo.tags:
            if skip_prefix not in tag.name:
                self.repo.git.tag('-d', tag)



    def rename_all_tags_with_prefix(self, prefix):
        for tag in self.repo.tags:
            self.rename_tag_with_prefix(tag.name, prefix)


    def dump_tag_infos(self):
        for tag, commit in self.tags_detached.items():
            print(f"Tag: {tag}, Commit: {commit}")




gg = GitOps(repo_path='/repo/github/szilank.code', zero_tag_name='0.4.0.0')

## sequence of operations
gg.get_tag_lists()
gg.guess_zero_tag()
gg.get_tag_distances()
gg.rename_all_tags_with_prefix('xx')
gg.delete_all_tags('xx')




gg.dump_tag_infos()
