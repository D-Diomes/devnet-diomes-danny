# Module 1 — Git & GitHub

**Student:** Diomes, Danny D.
**Date:** September 25, 2026

---
    
## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is like a save checkpoint, where you can save as many as you want, commit as man as you want, while the Github is like an online cloud, you can access it remotely, share to your works to your friend and more. Git is a tool while Github is a storage.
---

## Key vocabulary (in your own words)

- repository: Is a like a folder, you can create as many repository (folder) as you want, and store as many file as you want. 
- commit: Is a checkpoint of what you change, and you can add message to it.
- branch: A separate workspace, where you can add, delete, change any file without affecting the original.
- push / pull: pull is you will be getting the latest contents inside of the repository. While push send the commited files you commit and store them to your repository
- pull request: A feature where the owner of the repository have the ability to merge your pull reques to the main brancg. It merges your branch to the main branch.
- merge conflict: When two changes happened at the same time and cant be merge, since there's 2 changes happening, and this can only be resolve manually.

---

## Walking through what I did
First is i forked or use as templae like this repository, and i created a branch and i begin to create my midterm, you can right click the explorer and new file or you can use the command touch, after that i created my first commit, and after makeing my midterm i pushed it, and in did my pull requst on the github repository itself.

```
    git switch -c midterm-movie-collection
    touch midterm.py
    git add midterm.py
    git commit -m "added movie list and choices"
    git push -u origin midterm-movie-collection
```

---

## A mistake I made (or one I want to avoid)

What tripped me up was using git commit and git push. I normally use git commit -m "message" because I know that the -m lets me add a message to my commit. When I accidentally used just git commit, Git opened another screen that I wasn't familiar with. so i search it up and you can end that by presing ctrl + c to terminate it in th terminal

I also tried using git push by itself and got an error. I didn't understand the error at first because I normally don't use Git commands very often. I learned that Git sometimes needs to know which remote and branch I want to push to, especially when pushing a branch for the first time.

If you push for the first time you need to be specific
    git push -u origin midterm-movie-collection
After that you can use the git push only with encountering an error
    git push
---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
