class With_work(object):
    def __enter__(self):
        """进入with语句的时候被调用"""
        print("enter called")
        return "haha"

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with的时候被with调用"""
        print("exit called")


with With_work() as f:
    print(f)
    print("hello with")


class With_work2(object):
    def __enter__(self):
        """进入with语句的时候被调用"""
        print("enter called")
        return "haha"

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        离开with的时候被with调用
        exc_type: 异常的类型
        exc_val: 异常的信息
        exc_tb: 异常的追踪信息
        """
        print("exit called")
        print("exc_type: %s" % exc_type)
        print("exc_val: %s" % exc_val)
        print("exc_tb: %s" % exc_tb)


with With_work() as f:
    print(f)
    print("hello with")
    a = 1 / 0
    print("哈哈哈")