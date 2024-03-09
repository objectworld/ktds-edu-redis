import time
import redis
import configparser

config  = configparser.ConfigParser()  ## 클래스 객체 생성
config.read('./config.ini', encoding='utf-8')


def spt_cluster(CNT):
    redis_host=config["REDISMR"]["host"]
    redis_port=config["REDISMR"]["port"]
    redis_password=config["REDISMR"]["password"]
    redis_db=config["REDISMR"]["db"]
    
    # redis 연결
    rd = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)


    # [테스트, key 1]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rd.get("a")

    end_time = time.time() # 종료시간
    print("[key 1] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간

    # 테스트 결과
    # duration time : 0.628307580947876
    # duration time : 3.6477291584014893




    # [테스트, key 2]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rd.get("a")
        rd.get("b")

    end_time = time.time() # 종료시간
    print("[key 2] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간

    # 테스트 결과
    # duration time : 1.9884583950042725
    # duration time : 6.154340505599976



    # [테스트, key 3]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rd.get("a")
        rd.get("b")
        rd.get("c")

    end_time = time.time() # 종료시간
    print("[key 3] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간

    # 테스트 결과
    # duration time : 3.3824830055236816
    # duration time : 9.962273597717285


if __name__ == '__main__':
    # spt_cluster(sys.argv[1], sys.argv[2])
    # 만건 성능테스트
    spt_cluster(10000)

