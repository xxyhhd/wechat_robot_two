import time
import asyncio


def test():
    start_time = time.time()


    @asyncio.coroutine
    def request_data():
        print('开始')
        time.sleep(2.0)
        print('这是一个协程')

    loop = asyncio.get_event_loop() # 获取当前事件循环
    coroutine = request_data()
    task1 = loop.create_task(coroutine) # 任务一
    task2 = loop.create_task(coroutine) # 任务二
    a = asyncio.gather(task1,task2)
    loop.run_until_complete(a)
    end_time = time.time()
    print('运行耗时：{:.4f}'.format(end_time-start_time))
test()