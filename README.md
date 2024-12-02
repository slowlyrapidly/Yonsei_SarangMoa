# Yonsei_SarangMoa

연세 사랑모아는 연세대학교 구성원들이 함께 만들어가는 기부와 나눔의 웹 플랫폼입니다. 
연세 구성원들이 함께 만들어가는 따뜻한 나눔의 장으로, 학교와 사회에 긍정적인 변화를 불러오고자 합니다.

연세 사랑모아에서는 학생과 교직원이 더 이상 사용하지 않는 물품을 기부하면,
해당 물품을 저렴하게 판매하여 얻은 수익금을 학교 내외 봉사단체 및 다양한 프로젝트 지원에 사용합니다.
물품을 기부한 사람에게는 마일리지를 제공하여, 마일리지 페이지에서 원하는 상품으로 교환할 수 있습니다.
 
또한, 연세 사랑모아는 기부 및 운영을 돕기 위한 자원봉사자를 모집하고, 
이들에게 봉사점수 및 봉사활동 증명서를 지급하여 나눔의 가치를 실천할 기회를 제공합니다.

이 프로젝트는 Django를 기반으로 개발되었습니다.
---

## 프로젝트 실행 방법

### 1. 저장소 클론
GitHub에서 프로젝트 Clone:
```bash
git clone https://github.com/lkh599810/Yonsei_SarangMoa.git
cd Yonsei_SarangMoa
```

---

### 2. Python 가상환경 생성 및 활성화

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. 필수 패키지 설치
`requirements.txt` 파일을 사용해 필요한 패키지를 설치:
```bash
pip install -r requirements.txt
```

---

### 4. 데이터베이스 설정

#### 4.1 데이터베이스 테이블 생성
GitHub에 포함된 `migrations/` 폴더를 기반으로 데이터베이스 구조를 생성:
```bash
python manage.py migrate
```

#### 4.2 초기 데이터는 제공되지 않으며, 관리자 계정(Django admin 아님)을 만드신 후 직접 데이터를 삽입할 것.


---

### 5. 서버 실행
로컬 서버를 실행하여 프로젝트 확인:
```bash
python manage.py runserver
```

서버가 실행 후 브라우저에서 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)로 접속

---

## 초기 관리자 계정은 제공하지 않음. 유저 권한 2로 설정하여 진행할 것.

---



## 라이선스
이 프로젝트는 [MIT 라이선스](LICENSE)를 따름.
