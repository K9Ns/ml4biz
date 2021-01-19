# 비즈니스 머신러닝
### **Machine Learning for Business**

<p align="center">
<img width="565" alt="책 표지" src="https://user-images.githubusercontent.com/8121792/102049161-b700ea00-3e23-11eb-85c4-aa407f0af6e2.jpg">
</p>


### 비즈니스를 위한 머신러닝 예제

**저자** 더그 허전, 리처드 니콜  
**출판사** 한빛미디어(주)  
**원출판사** Manning  
**원서명** Machine Learning for Business  
**ISBN** 979-11-6224-365-7  


## 페이지 소개
《비즈니스 머신러닝》의 공식 Git 저장소 입니다. 책 내의 소스코드를 확인 및 다운로드 받을 수 있습니다.   
   
또한 책에서 설명하는 내용 중 AWS 서비스의 변경 사항에 대해 수정해 제공합니다.

## 책 소개

### 예제 코드 수정
> AWS의 세지메이커 파이썬 SDK 버전이 지난 2020년 9월에 2.x 으로 업데이트되었습니다.   
> 이로 인해 예제 수행 시 어려움이 예상되어 코드를 수정해 최신 SDK 버전에서도 수행 가능하도록 수정하였습니다.   
> 각 챕터안의 동일한 이름 뒤에 *_v2.ipnb* 라는 파일은 2.x 버전에서 구동 가능하며 몇가지 저자 코드의 오류를 수정하였습니다.
### 예제 목차
* [Chapter 2: 기술 담당자에게 구매 결재 검토 요청을 전달해야 하는가](/ch02)
* [Chapter 3: 이탈 조짐을 보이는 고객 찾기](/ch03)
* [Chapter 4: 고객 문의사항을 고객지원팀에 전달 여부 결정](/ch04)
  - 챕터 4장에서 사용하는 *inbound.csv* 데이터의 경우 파일이 크기 문제로 Git LFS 서비스에 의해 저장되어 있습니다.
  - LFS 를 설치/연동 후 정상적으로 다운로드 받을 수 있습니다.
  - [Git LFS 튜터리얼](https://github.com/git-lfs/git-lfs/wiki/Tutorial)
  - 또는 [다운로드 링크](https://s3.amazonaws.com/mlforbusiness/ch04/inbound.csv) 를 통해 다운로드 하신 후 사용하시기 바랍니다.
* [Chapter 5: 공급업체가 보낸 청구서에 대해 추가 질의 여부 결정](/ch05)
* [Chapter 6: 월간 전력 사용량 예측](/ch06)
* [Chapter 7: 월간 전력 사용량 예측 성능 향상](/ch07)
* [Chapter 8: 웹 서비스로 예측 모델 제공하기](/ch08)  
  
   
### 본문 업데이트
* [Appendix B: S3 파일을 저장하기 위한 S3 설정 및 사용 방법(변경된 S3 콘솔 UI 대응)](/appendix/b_s3.md)


### 설치 방법
Git 설치 방법은 [링크](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98)를 확인하시기 바랍니다.
설치 후 git 명령어로 저장소를 다운받습니다.

```sh
$ git clone https://github.com/K9Ns/ml4biz.git
$ cd ml4biz
```
   
또는   
아래 그림과 같이 오른쪽 상단의 `Code` 버튼을 클릭 후 `Download ZIP` 버튼을 통해 압축 파일을 다운 받은 후 사용하셔도 됩니다.      
<p align="center">
<img width="565" alt="코드 다운" src="https://user-images.githubusercontent.com/8121792/102132088-7e4e2880-3e96-11eb-92e8-ba71400c182e.png">
</p>
