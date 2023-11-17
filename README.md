# GOOPAPA

## Recent Issue
### 2022.10: 404 Client Error
> Error: requests.exceptions.HTTPError: 404 Client Error: Not Found for url:

모든 코드 수정은 `google_trans_new.py`에서 진행됩니다.</br>
All code revisions are performed in the python translator package `google_trans_new.py`.

Line 16 (기본 URL 서픽스 수정)
```diff
- URL_SUFFIX_DEFAULT = 'cn'
+ URL_SUFFIX_DEFAULT = 'com'
```

Line 90 (기본 URL 서픽스 수정)
```diff
- def __init__(self, url_suffix="cn", timeout=5, proxies=None):
+ def __init__(self, url_suffix="com", timeout=5, proxies=None):
```

Line 151 (번역 함수에서 올바른 동작을 위한 디코드 형식 수정)
```diff
- response = (decoded_line + ']')
+ response = decoded_line
```

Line 233 (언어 감지 함수에서 올바른 동작을 위한 디코드 형식 수정)
```diff
- response = (decoded_line + ']')
+ response = decoded_line
```
