import sys
import time, datetime
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
        rc.set(f"a:{CNT}", 11)

    end_time = time.time() # 종료시간
    print("[key 1] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간




    # [테스트, key 2]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.set(f"a:{CNT}", 11)
        rc.set(f"b:{CNT}", 22)

    end_time = time.time() # 종료시간
    print("[key 2] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간




    # [테스트, key 3]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.set(f"a:{CNT}", 11)
        rc.set(f"b:{CNT}", 22)
        rc.set(f"c:{CNT}", 33, datetime.timedelta(seconds=300))    ## TTL 300초(5분)

    end_time = time.time() # 종료시간
    print("[key 3] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간



if __name__ == '__main__':
    # spt_cluster(sys.argv[1], sys.argv[2])
    # 만건 성능테스트
    spt_cluster(10000)

