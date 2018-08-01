# replace_prefix
替换以指定字符串为前缀的文件及文件中的单词

使用方法:

```python
./replace_prefix.py '原前缀' '新前缀' '文件路径'
```
例如：
```
ABCLogin.h
ABCLogin.m
- (void)abc_login;
```

```
./replace_prefix.py 'ABC' 'DM'
```
结果:
```
DMLogin.h
DMLogin.m
- (void)dm_login;
```
