# python Automatic label version number python自动标签版本号

Automatically creating a version in the tag starts from 0.0.1 by default 默认情况下，在标记中自动创建版本从0.0.1开始

It's simple It's simple

## Usage 用法

The following is an example `.github/workflows/main.yml` that will execute when a `push` to the `master` branch occurs.

以下是一个示例“.github/workflows/main.yml”，当“推送”到“master”分支时将执行该示例。

### Example workflow  工作流程示例


If you need a tag to trigger the build, you need to apply for the key yourself.

Please pay attention to the trigger condition to avoid loop execution

If you use the `${{ secrets.GITHUB_TOKEN }}` If you don't have enough permissions, you can't trigger the workflow.

It's okay. He still creates tags.

如果您需要标签来触发构建，则需要自己申请密钥。
请注意触发条件，避免循环执行
如果您使用 '${{ secrets.GITHUB_TOKEN }}'，如果您没有足够的权限，则无法触发工作流。
没关系。他仍然创建标签。

```
# 下面是一个基础的工作流，你可以基于它来编写自己的 Github Actions
name: auto_tag

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      NewVersion: ${{ steps.create_version.outputs.NewVersion }} 
    steps:
      - uses: actions/checkout@master
      - uses: duolabmeng6/action-autotag-python@master
        id: create_version
        with:
          token: ${{ secrets.GITHUB_TOKEN }} # ${{ secrets.LONGLONG }} # Use your own key to trigger tags' workflow
      - name: View variable
        run: |
          echo ${{ format('version={0}', steps.create_version.outputs.NewVersion ) }}
```
