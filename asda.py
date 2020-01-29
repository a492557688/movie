import celery
backend='redis://:123456@127.0.0.1:6379/1' #任务提交后放在这个库里
broker='redis://:123456@127.0.0.1:6379/2' #任务执行完后结果的db
cel=celery.Celery('test',backend=backend,broker=broker)
#装饰函数
@cel.task
def add(x,y):
    return x+y


result = add.delay(4,5) #4,5为参数  #启动任务
print(result.id)  #拿到这个用于查看任务的CDK


