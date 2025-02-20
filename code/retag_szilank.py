#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import git
import sys


class GitOps:
    def __init__(self, repo_path):
        self.repo = git.Repo(repo_path)

        self.zero_tag = None
        self.active_branch_name = self.repo.active_branch.name        # master if you are on default
        self.rename_prefix = 'xx'

        self.tags = []
        self.tags_detached = []

        self.get_tag_lists()
        if not self.guess_zero_tag():
            print("No detached tags found. Exiting.")
            sys.exit(1)

    def get_tag_lists(self):
        self.tags = sorted(self.repo.tags, key=lambda t: t.commit.committed_date, reverse=True)
        self.tags_detached = [tag for tag in self.tags if not tag.is_detached]

    def guess_zero_tag(self):                     # DONE (testit)
        previous_tag = None
        for tag in self.tags:
            if tag.is_detached:
                self.zero_tag = previous_tag
                return
            else:
                previous_tag = tag
        return None     # if there was no detached tag

    def get_commit_count_distance_from_zero_tag(self, next_tag):        # DONE (testit)
        return next_tag.commit.count() - self.zero_tag.commit.count()

    def get_commit_hash_from_tag(self, distance):               # DONE (testit)
        commit = self.repo.commit(self.zero_tag)
        for _ in range(distance):
            commit = commit.children[0]
        return commit.hexsha

    def rename_tag_with_prefix(self, original_tagname):         # DONE
        new_tag = f"{self.rename_prefix}{original_tagname}"
        commit = self.repo.commit(original_tagname)
        self.repo.create_tag(new_tag, commit)
        self.repo.delete_tag(original_tagname)
        return new_tag

    def dump_tag_infos(self):                                 # DONE
        for tag, commit in self.tags_detached.items():
            print(f"Tag: {tag}, Commit: {commit}")

    def iterate_and_fix_on_detached_tags(self):
        for tag in gg.tags_detached:
            distance = self.get_commit_count_distance_from_zero_tag(tag)
            actual_tagname = tag.tagname
            prefixed_tagname = self.rename_tag_with_prefix(actual_tagname)

            active_commit = self.get_commit_hash_from_tag(distance)
            self.repo.git.create_tag(actual_tagname, active_commit)

            self.repo.git.tag('-d', prefixed_tagname)


gg = GitOps(repo_path='/repo/github/szilank.code')
gg.iterate_and_fix_on_detached_tags()
gg.dump_tag_infos()
