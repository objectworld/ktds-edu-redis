# Redis on Kubernetes

> Container 기반 Redis 교육자료 !!

본 교육은 Container를 기반으로 한 Redis 를 학습하는 과정으로 kubernetes 환경에서 Redis install수행하는 방법과 각각 모니터링 솔루션을 확인하는 방법을 알아보며 Redis-cli 환경 및 Spring Boot / Python 으로 실습한다.

문의: 송양종( yj.song@kt.com / ssongmantop@gmail.com )



## 1. 시작전에 ( [가이드 문서 보기](beforebegin/beforebegin.md) )

### 1) 실습 환경 준비

* MobaxTerm 설치, GitBash설치, Typora 설치,  Java/STS설치
* 교육자료 Download
* 실습환경준비(Cloud), 개인VM서버 주소 확인, SSH 확인



## 2. Redis ( [가이드 문서 보기](redis/2.Redis.md) )

### 1) Redis 개요

* Redis 개요
* Redis vs Memcached 비교
* Atomic 자료구조
* Redis 운영모드 비교
  * Stand Alone / Master Replica / Sentinel /  Redis Cluster

* Redis 운영시 주의사항





## 3. Cache ( [가이드 문서 보기](redis/3.Cache.md) )

### 1) Caching

* Caching 정의
* Cache Hit & Miss

### 2) Cache Pattern

* Pattern 1 : 코드성 데이터 캐싱
* Pattern 2 : 주기적 생성 데이터 캐싱
* Pattern 3 : E2E 구간 성능 향상



## 4. Redis Hands-in ( [가이드 문서 보기](redis/4.Redis-hands-in.md) )

### 1) Redis Install 준비

### 2) Redis Cluster Install

* helm chart download / Redis Cluster Install
* Internal Access - Redis client 실행, Redis-cluster 상태 확인, set/get 확인
* 성능테스트(Python)

### 3) Redis Install

* helm chart download / Redis(Master Replica) Install

* Internal Access : Redis client, set/get 확인, 성능테스트(Python )
* External Access : Node IP 확인, Redis client 확인(Docker), set/get 확인

### 5) Redis Metrics

* Redis Info, Memory, Stats, Clients, Replication, Commandstats, Persistence

### 6) ACL

* ACL 기본명령
* 읽기전용 계정 생성
* 특정 key만 접근 허용 권한





## 5. Redis Hands-in2 ( [가이드 문서 보기](redis/5.Redis-hands-in2.md) )

### 1) [EduCluster] Redis-MR 서버 접근

* Docker Redis-cli, Docker Python-cli, 성능테스트(Python )
* p3x, grafana monitoring

### 2) [EduCluster] Redis-Cluster 서버 접근

* 개인 client  namespace 생성
* Redis Client POD, Python Client POD, 성능테스트(Python )
* p3x, grafana monitoring

### 3) Collection

* 실습준비
  
* String, List, Set, Sorted Sets, Hash, Bit
  

### 4) Redis 자료구조 활용 사례

* 1일 1회 참여가능 이벤트
* 인증문자 대기시간
* 실시간 랭킹 시스템
* 좋아요 기능
* 좋아요를 한 개수 조회하기
* 최근 본 상품 목록

### 5) Java Sample

* Jedis vs Lettuce
* redis-sample 소스 확인 및 수행
* CRUD 테스트





## 6. Redis Hands-in3 ( [가이드 문서 보기](redis/6.Redis-hands-in3.md) )

### 1) Master-Replica FailOver

* Master Backup 없이 재기동
* Master Backup 후 재기동



### 2) Redis Cluster FailOver Test

* Master node down
* Cluster Fail Over 처리





## 별첨. Cloud Setup ( [가이드 문서 보기](cloud-setup/cloud-setup.md) )

### 1) Bastion Server Setup

* kubernetes Install (k3s)
* Helm Install
* 기타 Tool Setup

### 2) Redis on Cloud

* Redis Cluster Install, Redis Insatll
* Web UI (P3X / RedisInsight)
* Monitoring(Metric Exporter, Prometheus, Grafana) 설치 및 Dashboard 설정
