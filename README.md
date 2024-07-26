# Django

## mvc 패턴
![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/800px-MVC-Process.svg.png)
- 자바의 스프링, 자바스크립트의 node와 같은 역할을 수행함

### 동작 과정
1. request 12
2. url.py
3. views.py / 프론트 역할
4. model.py
5. template(html) /백 역할
6. view.py
7. response html
8. 무한반복

## 튜토리얼

0. 전역 장고 설치
1. 프로젝트 생성

```bash
django-admin startproject first_pjt{프로젝트 이름} .

```
2. 가상환경 생성
```bash
python -m venv venv
```
3. 가상환경 활성화
```bash
source venv/Scripts/activate
```
4. 가상환경 장고 설치
```bash
pip install django
```
5. manage.py 서버 실행 (ctrl + C :서버 종료)
```bash
python manage.py runserver
```
6. 앱생성
```bash
django-admin startapp first_app{앱이름}
```

7. settings.py에 앱등록
```python
INSTALLED_APPS = [
    ...
    '{앱이름}',
]

8. urlpatterns > path (이정표 세우기)
어떤 경로(index) 가 들어오면 (요청), 실행할거야. (views.py)
```

/// 지금 루트 url > 앱 템플릿에 html 생성 > views.py에 기능 편집 
    url 페이지에 뉴스1
    뉴스2
    뉴스3
    ... 데이터베이스에서 가져와서 넣을거임. 이때 render 함수가 역할을 함