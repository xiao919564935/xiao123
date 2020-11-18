"""
性能测试
"""
import math

from locust import HttpUser, between, task, LoadTestShape

'''
1、为要模拟的用户定义一个类，从HttpUser继承
'''


class CarRental(HttpUser):
    # between 是User类中定义的一个方法
    # wait_time是User类定义的一个属性，表示等待时间
    wait_time = between(3, 8)  # 任务跟任务之间的等待时间在3~8之间取随机数

    @task
    def loadAllRent(self):
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllMenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")


# 加压的模型
# class StepLoadShape(LoadTestShape):
#     step_time = 30
#     step_load = 10
#     spawn_rate = 10
#     time_limit = 600
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         if run_time > self.time_limit:
#             return None
#
#         current_step = math.floor(run_time / self.step_time) + 1
#         return (current_step * self.step_load, self.spawn_rate)

class DoubleWave(LoadTestShape):
    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                (self.peak_one_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                + (self.peak_two_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None

# class StagesShape(LoadTestShape):
#     stages = [
#         {"duration": 60, "users": 10, "spawn_rate": 10},
#         {"duration": 100, "users": 50, "spawn_rate": 10},
#         {"duration": 180, "users": 100, "spawn_rate": 10},
#         {"duration": 220, "users": 30, "spawn_rate": 10},
#         {"duration": 230, "users": 10, "spawn_rate": 10},
#         {"duration": 240, "users": 1, "spawn_rate": 1},
#     ]
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         for stage in self.stages:
#             if run_time < stage["duration"]:
#                 tick_data = (stage["users"], stage["spawn_rate"])
#                 return tick_data
#         return None


# -f 要执行的文件
# --host 被测系统
# --web-host locust Web页面的访问地址
# --web-post locust Web页面的访问端口
# locust -f locust_test.py --host=http://127.0.0.1:8080  --web-host=http://127.0.0.1:8088
# locust -f locust_test.py --step-load

