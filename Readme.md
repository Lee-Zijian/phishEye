# phishTest：钓鱼攻击部署工具
前端：使用 HTML 编写的 PayPal 高仿网站

后端：基于 Flask 框架开发的前后端交互功能，并使用面向 Web 服务的分布式反向代理 ngrok 以生成网站链接

部署所需工具：`python3 (version 3.6+)`, `pip3`

**本工具仅用于论文复现测试，请勿用作钓鱼攻击！！！如违规使用，后果自负！！！**

## 安装部署方式
*注：以下操作建议在开启全局 VPN 的网络环境下操作（科学上网），否则某些工具包的安装以及反向代理生成链接可能无法正常完成*
1. 进入 phishTest 所在目录: `$ cd phishTest`
2. 安装依赖的工具包: `$ pip3 install -r requirements.txt`
3. 访问 Ngrok 官网：<https://dashboard.ngrok.com/get-started/setup>，根据官方指引步骤注册账号，并将其提供的`authtoken`添加至本地环境以开通反向代理服务
4. 启动 phishTest: `$ sudo python3 phishTest.py -s paypal -d pc -p 1234`，
  * `-s, -d`: 用于指定仿造的目标网站，目前仅提供 PayPal 前端网页
  * `-p`: 用于指定本地监听端口
  * *（注：请使用超级用户权限执行，否则反向代理初始化可能由于权限不足无法完成）*
5. 使用浏览器访问生成的 `Ngrok public address` 或者 `Phishing short link` 网站链接即可，后端进程会抓取用户提交的输入数据，并记录至本地日志文件`captured.db`
