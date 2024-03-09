import time
from rediscluster import RedisCluster
import configparser

config  = configparser.ConfigParser()  ## 클래스 객체 생성
config.read('./config.ini', encoding='utf-8')


def spt_cluster(CNT):
    redis_host=config["REDISCLUSTER"]["host"]
    redis_port=config["REDISCLUSTER"]["port"]
    redis_password=config["REDISCLUSTER"]["password"]
        
    startup_nodes = [{"host":redis_host, "port":redis_port}]
    rc = RedisCluster(startup_nodes=startup_nodes, 
                    decode_responses=True, 
                    skip_full_coverage_check=True,
                    password=redis_password)

    # [테스트, key 1]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.get("a")

    end_time = time.time() # 종료시간
    print("duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간

    # 테스트 결과
    # duration time : 0.628307580947876
    # duration time : 3.6477291584014893






    # [테스트, key 2]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.get("a")
        rc.get("b")

    end_time = time.time() # 종료시간
    print("duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간

    # 테스트 결과
    # duration time : 1.9884583950042725
    # duration time : 6.154340505599976



    # [테스트, key 3]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.get("a")
        rc.get("b")
        rc.get("c")

    end_time = time.time() # 종료시간
    print("duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간

    # 테스트 결과
    # duration time : 3.3824830055236816
    # duration time : 9.962273597717285


if __name__ == '__main__':
    # spt_cluster(sys.argv[1], sys.argv[2])
    # 만건 성능테스트
    spt_cluster(10000)

