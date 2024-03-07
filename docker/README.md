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
> 第一次启动，存在创建数据库的情况，需要等待几秒钟，到后端重启后即可正常访问