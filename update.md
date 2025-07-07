git stash                # 暂存修改

git pull upstream main   # 同步上游

git stash pop           # 恢复修改

# 解决冲突（如果有）

git add .

git commit -m "更新后的修改"

git push origin main



## 分支工作流

1. 创建功能分支
git checkout -b feature/my-feature

2. 在分支上开发
git add .
git commit -m "实现新功能"

3. 准备合并前同步主分支
git checkout main
git pull upstream main
git push origin main

4. 合并到功能分支
git checkout feature/my-feature
git merge main

5. 推送功能分支
git push origin feature/my-feature

6. 在 GitHub 上创建 Pull Request
