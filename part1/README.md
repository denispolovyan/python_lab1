# lab1 python

| Сommand list | part 1     |
| ------------ | ---------- |
| 1.           | mkdir lab1 |
| 2.           | cd lab1    |
| 3.           | git init   |

<br/> 

| Сommand list | part 2                                           |
| ------------ | ------------------------------------------------ |
| 1.           | mkdir part1                                      |
| 2.           | cd part1                                         |
| 3.           | git touch README.md                              |
| 4.           | git add .                                        |
| 5.           | git commit -m "feature: created part1/README.md" |
| 6.           | git push origin master                           |

<br/>

# log history (git log --oneline --decorate)

#### a4aead4 (HEAD -> master, origin/master) feature: modified README.md in master branch
#### fa18329 feature: created part1/README.md

<br/> 

# Working tree
|E:/kpi/Python/lab1_git  fa18329 [first_branch]

<br/> 

# Staging area

Changes not staged for commit:  
(use "git add <file>..." to update what will be committed)  
(use "git restore <file>..." to discard changes in working directory)  
modified:   README.md

<br/>

# Files stage
Before *git add .* or *git add README.md* changes in README.md are unstaged.

<br/>

# Working tree after merge
E:/kpi/Python/lab1_git  2bdb958 [master]

<br/>

# Project history
#### 2bdb958 (HEAD -> master) HEAD@{0}: commit (merge): Merge branch 'first_branch'  
#### 7953183 (origin/master) HEAD@{1}: commit: feature: added log history in master branch  
#### a4aead4 HEAD@{2}: commit: feature: modified README.md in master branch  
#### fa18329 HEAD@{3}: checkout: moving from first_branch to master  
#### 9179531 (origin/first_branch, first_branch) HEAD@{4}: commit: feature: modified README.md in first_branch branch  
#### fa18329 HEAD@{5}: checkout: moving from master to first_branch  
#### fa18329 HEAD@{6}: commit (initial): feature: created part1/README.md  

<br/>

| Сommand list | part 3                                                             |
| ------------ | ------------------------------------------------------------------ |
| 1.           | git checkout -b first_branch                                       |
| 2.           | git worktree list                                                  |
| 3.           | git status                                                         |
| 4.           | git add .                                                          |
| 5.           | git commit -m "feature: modified README.md in first_branch branch" |
| 6.           | git push origin first_branch                                       |

<br/>

| Сommand list | part 4                                                       |
| ------------ | ------------------------------------------------------------ |
| 1.           | git checkout master                                          |
| 2.           | git worktree list                                            |
| 3.           | git status                                                   |
| 4.           | git add .                                                    |
| 5.           | git commit -m "feature: modified README.md in master branch" |
| 6.           | git push origin master                                       |
| 7.           | git log --all                                                |

<br/>