# README



## Redis on Kubernetes

> Container 기반 Redis 교육자료 !!

본 교육은 Container를 기반으로 한 Redis 를 학습하는 과정으로 kubernetes 환경에서 Redis install수행하는 방법과 각각 모니터링 솔루션을 확인하는 방법을 알아보며 Spring Boot / Python 으로 실습한다.

문의: 송양종( yj.song@kt.com / ssongmantop@gmail.com )



## 1. 시작전에 ( [가이드 문서 보기](beforebegin/beforebegin.md) )

### 1) 실습 환경 준비

* MobaxTerm 설치
* Typora 설치
* 교육자료 Download
* 실습환경준비(Cloud)



## 2. Redis 개념 ( [가이드 문서 보기](redis/redis-개념.md) )

### 1) Redis 개요

* Redis 개요
* Redis / Redis Cluster

### 2) Caching

* Caching 정의
* hit 관련 용어
* Cache 사용시 주의사항

### 3) Cache Pattern

* Pattern 1 : 코드성 데이터 캐싱
* Pattern 2 : 주기 생성 데이터 캐싱
* Pattern 3 : E2E 구간 성능 향상



## 3. Redis Hands-in ( [가이드 문서 보기](redis/redis-hands-in.md) )

### 1) Redis Install 준비

### 2) Redis Cluster Install

* helm chart download / Redis Cluster Install
* Internal Access - Redis client 실행, Redis-cluster 상태 확인, set/get 확인

### 3) Redis Install

* helm chart download / Redis Install

### 4) Accessing Redis

* Internal Access : Redis client, set/get 확인
* External Access : Node IP 확인, Redis client 확인(Docker), set/get 확인

### 5) ACL

* ACL 기본명령
* 읽기전용 계정 생성
* 특정 key만 접근 허용 권한

### 6) EduCluster Redis Server

* 모니터링 tool
  * P3X
  * RedisInsight

* EduCluster Redis Access

### 7) Java Sample

* Jedis vs Lettuce
* redis-sample 소스 확인 및 수행
* CRUD 테스트





## 별첨. Cloud Setup ( [가이드 문서 보기](cloud-setup/cloud-setup.md) )

### 1) Bastion Server Setup

* kubernetes Install (k3s)
* Helm Install
* 기타 Tool Setup

### 2) Redis on Cloud

* Redis Cluster Install
* Web UI (P3X / RedisInsight)
