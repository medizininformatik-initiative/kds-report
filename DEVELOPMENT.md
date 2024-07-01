# Development


## Release Checklist

* Change to develop branch
* update the CHANGELOG based on the milestone
* create a commit with the title `Release v<version>`
* create a PR from the release branch (develop) into the main branch
* merge that PR (after proper review)
* create and push a tag called `v<version>` like `v1.1.0` on the main branch at the merge commit
* create release notes on GitHub
