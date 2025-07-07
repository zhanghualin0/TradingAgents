# 1. 日常工作流程
## 推送你的修改到自己的仓库

git add .

git commit -m "你的修改说明"

git push origin main

## 拉取原仓库的最新更新：

获取上游仓库的最新变更

git fetch upstream

合并到你的本地分支

git merge upstream/main

推送到你的远程仓库

git push origin main

## 一步到位的同步命令：

git pull upstream main && git push origin main

# 2. 如果有本地修改但想同步上游

暂存本地修改
git stash

同步上游
git pull upstream main

恢复本地修改
git stash pop

推送到你的仓库
git push origin main

