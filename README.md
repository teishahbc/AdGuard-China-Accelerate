# AdGuard国内加速方案

此项目初忠是为了将国内网站走国内DNS，国外网站（漏网之鱼）走国外无污染的加密DNS

## 使用方式

1. 在 AdGuardHome 配置中设置 `upstream_dns_file` 指向 `configuration.txt`
2. 配置 `crontab` 定时拉取 `configuration.txt` 文件
```
0 0 * * * wget -O /opt/AdGuardHome/configuration.txt https://raw.githubusercontent.com/teishahbc/AdGuard-China-Accelerate/refs/heads/main/configuration.txt
```

## 数据来源/致谢

- Dnsmasq转AdGuard规则 [rwx9032/AdguardHome](https://github.com/rwx9032/AdguardHome)
- 数据来源[felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)
