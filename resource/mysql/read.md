DESC col_test
group_concat
select a,b from t group by a,b
select字段基本跟在group by 后
分组 聚合 having  分组后having再一次筛选
一对一,一对多,多对多建表
union all
内外链接  自然链接 natual join X
native cat query_build
事物acid
一句sql是事物,多句使用 start transtion;
脏读--幻读
用户权限
视图与权限 增删改  数据的增删改 视图中的数据不直接来自基表,就不能修改

explain select *
触发器
sql优化 日志 分析 缓存 profiles
show open tables ;
主从集群
帮助文档,help