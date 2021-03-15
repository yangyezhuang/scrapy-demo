# Scrapy settings for Scrapy_sina project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Scrapy_sina'

SPIDER_MODULES = ['Scrapy_sina.spiders']
NEWSPIDER_MODULE = 'Scrapy_sina.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 10
CONCURRENT_REQUESTS_PER_IP = 10

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Scrapy_sina.middlewares.ScrapySinaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Scrapy_sina.middlewares.ScrapySinaDownloaderMiddleware': 543,
    'Scrapy_sina.middlewares.RandomUserAgent': 544
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Scrapy_sina.pipelines.Json_Pipeline': 301,
    'Scrapy_sina.pipelines.Mysql_Pipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DEFAULT_COOKIE = {'U_TRS1': '0000005a.f45f9f1f.5e6db9b1.c35f5d94', 'UOR': 'www.baidu.com,finance.sina.com.cn,',
                  'SCF': 'Aio_yCEK7PdXaT1IvaJv25O3vhX3Z74Jw4M2BCsQAGy7JbN95RNg4K2932XCOHpk1wovN1xhY7nxqVcX_3CEHfs.',
                  'sso_info': 'v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLWOk5i2jbOUuI2DlLKJp5WpmYO0tY6TmLaNs5S4jYOUsg',
                  'UM_distinctid': '1755a65b8cc424-037a578ef99b7e-b7a1334-144000-1755a65b8cd881',
                  'SINAGLOBAL': '121.238.243.149_1604154938.825564', 'Apache': '58.211.250.146_1606807392.586098',
                  'name': 'sinaAds', 'post': 'massage', 'page': '23333',
                  'ULV': '1606807394112:4:1:1:58.211.250.146_1606807392.586098:1604661121074',
                  'SGUID': '1606807395625_69824467',
                  'CNZZDATA5832809': 'cnzz_eid%3D306119988-1606802834-%26ntime%3D1606802834', 'lxlrttp': '1578733570',
                  'NowDate': 'Tue Dec 01 2020 15:30:24 GMT+0800 (中国标准时间)',
                  'CNZZDATA1271237680': '1351611256-1606807474-%7C1606807474',
                  'CNZZDATA1271230489': '958668403-1606802084-%7C1606806825', 'directAd': 'true', '__gads': 'ID',
                  'ULOGIN_IMG': 'tc-1cb286a6099ff7df970facfabe9c29a85684'}
