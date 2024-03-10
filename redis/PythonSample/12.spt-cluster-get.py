import sys
import time
from rediscluster import RedisCluster
import configparser

config  = configparser.ConfigParser()  ## 클래스 객체 생성
config.read('./config.ini', encoding='utf-8')


def spt_cluster(redis_host='ds-redis-master', redis_port='6379', key_prefix='user01', CNT=10000):
    # redis_host=config["REDISCLUSTER"]["host"]
    # redis_port=config["REDISCLUSTER"]["port"]
    redis_password=config["REDISCLUSTER"]["password"]
        
    startup_nodes = [{"host":redis_host, "port":redis_port}]
    rc = RedisCluster(startup_nodes=startup_nodes, 
                    decode_responses=True, 
                    skip_full_coverage_check=True,
                    password=redis_password)

    print("[SPT] system performance testing ....")
    
    # [테스트, key 1]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.get(f"{key_prefix}:a:{i}")

    end_time = time.time() # 종료시간
    print("[key 1] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간





    # [테스트, key 2]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.get(f"{key_prefix}:a:{i}")
        rc.get(f"{key_prefix}:b:{i}")

    end_time = time.time() # 종료시간
    print("[key 2] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간




    # [테스트, key 3]============================================================
    start_time = time.time() # 시작시간
    for i in range(CNT):
        # print(i)
        rc.get(f"{key_prefix}:a:{i}")
        rc.get(f"{key_prefix}:b:{i}")
        rc.get(f"{key_prefix}:c:{i}")

    end_time = time.time() # 종료시간
    print("[key 3] duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간



if __name__ == '__main__':
    # 성능테스트
    # arg1 : host
    # arg2 : port
    # arg3 : keyprefix
    # arg4 : 건수
    spt_cluster(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))

