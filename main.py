# 在github中自动发布版本标签
import os
from functools import cmp_to_key
from natsort import natsorted, ns
from github import Github

def 版本号递进(version_str):
    # 版本号格式为 x.x.x 满十进一
    version_str = version_str.lstrip('v') # 去掉v
    version = version_str.split('.')
    if len(version) == 2:
        version.append('0')
    version = list(map(int, version))
    version[2] += 1
    if version[2] >= 10:
        version[2] = 0
        version[1] += 1
        if version[1] >= 10:
            version[1] = 0
            version[0] += 1
    return 'v' + '.'.join(map(str, version))

def 版本号从大小写排序(tags):
    tags = natsorted(tags, alg=ns.IGNORECASE | ns.LOCALE, reverse=True)
    return tags




# tags = ['latest', '0.0.10', '0.0.9', '0.0.8', '0.0.7']
# tags = 版本号从大小写排序(tags)
# print("使用 版本号大小比较 排序:", tags)
#
# exit()

def 检查当前项目并且将版本号码加一(token, project_name):
    # token = "token"
    # project_name = "duolabmeng6/QtEsayDesigner"

    g = Github(token)
    # print("用户名",g.get_user().name)
    repo = g.get_repo(project_name)
    # print("项目名称",repo.name)
    print("标签数量", repo.get_tags().totalCount)
    if repo.get_tags().totalCount == 0:
        # 没有标签的话 创建标签 0.0.1
        sha = repo.get_commits()[0].sha
        新版本号 = "0.0.1"
        repo.create_git_ref(f"refs/tags/{新版本号}", sha)
        return 新版本号

    # 版本号对比
    tags = []
    k = 0
    for tag in repo.get_tags():
        # print(tag.name)
        tags.append(tag.name)
        k += 1
        if k == 5:
            break  # 取前5个标签
    print("原来的 tags", tags)

    # 版本号排序
    tags = 版本号从大小写排序(tags)
    # print("版本号排序:", tags)
    新版本号 = 版本号递进(tags[0])
    # print("新版本号:", 新版本号)
    print("创建新版本", 新版本号)
    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{新版本号}", sha)

    return 新版本号

def main():
    print("进入自动发布版本标签程序")
    # print(os.environ)
    GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')
    print("GITHUB_REPOSITORY",GITHUB_REPOSITORY)
    INPUT_TOKEN = os.environ.get('INPUT_TOKEN')

    新版本号 = 检查当前项目并且将版本号码加一(INPUT_TOKEN, GITHUB_REPOSITORY)
    print(f"::set-output name=NewVersion::{新版本号}")
    print(f"::save-state name=NewVersion::{新版本号}")

    name = "NewVersion"
    value = 新版本号
    github_output = os.getenv("GITHUB_OUTPUT", "default_filename")
    print("写出版本号信息")
    with open(github_output, "a") as file:
        file.write(f"{name}={value}\n")


if __name__ == "__main__":
    main()
