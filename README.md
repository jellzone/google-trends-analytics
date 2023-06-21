# google-trends-analytics
# 关键字趋势比较工具

本项目提供了一个简单的Python工具，用于比较多个关键字的趋势。通过使用matplotlib和pandas库，该工具可以从CSV文件中读取数据，绘制样条曲线图，并根据需要筛选关键字。默认情况下，代码显示前4个关键字的趋势。

## 步骤一：

首先，确保您已安装pandas库，以便与pytrends库一起使用。如果尚未安装，请使用以下命令安装：

```pip install pandas pytrends```

接下来，我们将修改示例代码以读取CSV文件并获取关键字列表。假设您的CSV文件名为keywords.csv，结构如下：

```
keyword
关键字1
关键字2
关键字3
...
```
运行  st1_google_trends.py

```bash
python st1_google_trends.py
```
这段代码将读取keywords.csv文件中的关键字，使用Google Trends API获取数据，并将结果保存到名为trends_data.csv的文件中。请注意，频繁请求可能导致访问受限。请遵守Google的服务条款和数据使用政策。

## 步骤二
## 功能

- 从CSV文件（例如：trends_data.csv）中读取关键字趋势数据。
- 使用matplotlib绘制样条曲线图，以便于比较多个关键字的趋势。
- 根据需要筛选关键字，只显示所选关键字的趋势。
- 默认显示前4个关键字的趋势。

## 安装依赖库

在开始使用本工具之前，请确保安装了以下Python库：

- pandas
- matplotlib

可以使用以下命令安装所需库：

```bash
pip install pandas matplotlib
```

## 使用方法

1. 将你的趋势数据保存为CSV文件，例如：trends_data.csv。确保文件中包含了关键字和对应的趋势数据。（第一段代码运行完后即包含这些数据）

2. 下载本项目中提供的Python代码，并将其保存在与CSV文件相同的目录中。

3. 根据你的需求修改代码中的参数，例如：要显示的关键字数量或要筛选的关键字。

4. 在命令行中，导航至包含代码和CSV文件的目录，然后运行以下命令：

```bash
python st2_check_the_trends.py
```

5. 代码将读取CSV文件中的数据，并根据指定的参数绘制样条曲线图。你可以查看生成的图像，以比较多个关键字的趋势。

## 贡献

如果你有任何改进或功能请求，请随时提交Pull Request或创建Issue。
有任何技术方面问题可以联系Wechat: Jellzone

## 许可

本项目采用GUN许可证。有关详细信息，请参阅[LICENSE](LICENSE)文件。
