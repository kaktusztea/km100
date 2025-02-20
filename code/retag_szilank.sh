#!/bin/bash

cd /repo/github/szilank.code/

# Get the list of tags
tags=$(git tag)

# Iterate over each tag
for tag in $tags; do
    # Get the commit hash associated with the tag
    commit=$(git rev-parse $tag)
    cmessage=$(log --grep="<commit_message>" --pretty=format:"%H")

    # Find the new commit hash after the rebase
    new_commit=$(git rev-list --grep="$commit" master | tail -n 1)

    # xtag="x${tag}"
    # echo "Addig xtag: '$xtag' to detached commit: ${commit}"
    # git tag -f $xtag $commit

    # echo "Removing original tag: $tag from detached commit: ${commit}"
    # git tag -d $tag


    echo "Tag: $tag, Commit: $commit, New Commit: $new_commit"
    # Create a new tag on the new commit
    ## git tag -f $tag $new_commit
done