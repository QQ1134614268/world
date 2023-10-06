yum
docker
mysql redis
nginx 
python 
nodejs  

git.ggok.top
jiangxin
renrenying
worker
test
template

docker-- 打包环境,任意尽快部署.配置清晰.  性能轻微损失(类mysql, 任意环境部署,性能要求高)

docker 以镜像为主, 非临时build镜像

# 1. docker环境
# 方案1: 使用dockerfile,现场拉代码,打包, 使用手动命令
# 方案2: 使用sh, dockerfile, git; 自动化部署
# 方案3: 携带(下载),直接执行docker命令

# 官方软件-- 稳定, 安装迅速, 意外情况少,可脱离docker
# sdk工具包,稳定,可脱离docker
# 代码不稳定,反复升级,bug修复, 依赖环境, 适合docker容器化
