#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import git
import sys


class GitOps:
    def __init__(self, repo_path, work_branch_name):
        self.repo = git.Repo(repo_path)

        self.zero_tag = None
        if not work_branch_name:
            self.active_branch_name = self.repo.active_branch.name        # master if you are on default
        else:
            self.active_branch_name = work_branch_name
        self.rename_prefix = 'xx_'

        self.tags = []
        self.tags_detached = []

        self.get_tag_lists()
        # self.dump_tag_infos()       # DEBUG only

        if self.guess_zero_tag() is None:
            print("No detached tags found. Exiting.")
            sys.exit(1)

    def is_tag_on_active_branch(self, tag):
        active_branch_commit = self.repo.active_branch.commit
        return self.repo.merge_base(active_branch_commit, tag.commit)[0].hexsha == tag.commit.hexsha

    def get_tag_lists(self):
        self.tags = sorted(self.repo.tags, key=lambda t: t.commit.committed_date, reverse=False)

        # TODO, BUG: all tags appear detached even ones are attached to master...
        # First detached should be tag: 0.4.2.9
        # tag class type: git.refs.tag.TagReference
        ## if branch_head.tags and tag_name not in branch_head.tags:
        ##     print("tag is not attached to branch head")
        # self.tags_detached = [tag for tag in self.tags if tag.is_detached]
        self.tags_detached = [tag for tag in self.tags if not self.is_tag_on_active_branch(tag)]

    def guess_zero_tag(self):
        if not self.is_tag_on_active_branch(self.tags[0]):
            print("First tag is not on active branch. Exiting.")
            return None
        previous_tag = None
        for tag in self.tags:
            if not self.is_tag_on_active_branch(tag):
                self.zero_tag = previous_tag
                return True
            else:
                previous_tag = tag
        return None     # if there was no detached tag

    def get_commit_count_distance_from_zero_tag(self, next_tag):     # DONE (testit)
        return next_tag.commit.count() - self.zero_tag.commit.count()

    # get commit which is on active branch AND is in distance from zero. Search direction: forward
    def get_commit_in_distance_from_zero(self, distance):                # TODO
        zero_commit = self.repo.commit(self.zero_tag.commit)

        commits = list(self.repo.iter_commits(zero_commit, max_count=distance + 1))  # max_count to limit the number of commits

        # Check if the distance is within the range of available commits
        if len(commits) <= distance or distance < 0:
            print(f"Invalid distance: the repo has fewer than {distance+1} commits from zero.")
            sys.exit(1)

        # Return the commit at the specified distance
        target_commit = commits[distance]
        return target_commit

    def rename_tag_with_prefix(self, original_tagname):         # DONE
        new_tag = f"{self.rename_prefix}{original_tagname}"
        commit = self.repo.commit(original_tagname)
        self.repo.create_tag(new_tag, commit)
        self.repo.delete_tag(original_tagname)
        return new_tag

    def iterate_and_fix_on_detached_tags(self):
        for tag in gg.tags_detached:
            distance = self.get_commit_count_distance_from_zero_tag(tag)
            print(f"ZERO tag ({self.zero_tag.name}) commit hash: {self.zero_tag.commit.hexsha}")
            print(f"tag: {tag.name}, distance from zero tag: {distance}")
            actual_tagname = tag.name
            # prefixed_tagname = self.rename_tag_with_prefix(actual_tagname)  # DEBUG: put back, when commits are passing

            active_commit = self.get_commit_in_distance_from_zero(distance)
            print(f"detached tag commit: '{tag.commit.hexsha}', message: '{tag.commit.message.strip()}'\n")
            print(f"onbranch commit: '{active_commit.hexsha}', message: '{active_commit.message.strip()}'\n")
            print("==========================================================================")

            # self.repo.git.create_tag(actual_tagname, active_commit)         # DEBUG: put back, when commits are passing
            # self.repo.git.tag('-d', prefixed_tagname)                       # DEBUG: put back, when commits are passing

    def dump_tag_infos(self):                                 # DONE
        for tag in self.tags:
            print(f"Normal tag: {tag.name}, Commit: {tag.commit}")
        for tag in self.tags_detached:
            print(f"Detached tag: {tag.name}, Commit: {tag.commit}, typeof class: {type(tag)}")


gg = GitOps(repo_path='/repo/github/szilank.code', work_branch_name='master')
gg.iterate_and_fix_on_detached_tags()
# gg.dump_tag_infos()

