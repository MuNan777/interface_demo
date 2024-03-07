## Docker

##### 准备

```bash
# ./web
npm run build
```

##### 启动

```bash
# ./docker
docker-compose up -d
```

##### 访问

http://localhost

> 注意！！
>
> 前端端口：80
>
> 后端端口：8000
>
> 数据库端口：3366
>
> 第一次启动
>
> 1. 需要构建 python 镜像，需要较长时间
>
> 2. 构建完成启动的时候，存在创建数据库的情况，需要等待几秒钟，到后端重启后即可正常访问