# Crawler

Facebook爬社團貼文及其留言

## Getting Started
這個專案是一個用於從Facebook群組中爬取貼文的程式，直到使用者中斷或爬完所有文章，並把結果輸出成CSV檔案的工具。下面是如何安裝和使用這個工具的步驟。

### Prerequisites

* python3.7
* pip

### Installing

1.clone repository到local。

```
https://github.com/zzhewei/crawler.git
```

2.到專案目錄

```
cd crawler
```

3.安裝相關套件

```
pip install -r requirements.txt
```

### Usage

1.命令列輸入:

```
python ./src/crawler.py
```

2.等待程式執行完畢或中斷程式，輸出的CSV檔案將存儲在output/目錄下。

## Running the tests

運行測試

### Break down into end to end tests

在專案底下的命令列執行

```
pytest
```
即可觀看測試結果

### And coding style tests

想分析測試專案程式碼，可另外使用pylint進行分析

首先
```
pip install pylint
```

之後針對要分析的py檔執行:

```
python -m pylint ./src/crawler.py
```
即可觀看測試結果

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **ZheWei** - *Initial work* - [ZheWei](https://github.com/zzhewei)
