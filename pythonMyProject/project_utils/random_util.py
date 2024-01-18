import random


def get_random_email():
    """
    随机生成邮箱
    :return: Email
    """
    emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    randomEmail = random.choice(emailtype)
    rang = random.randint(4, 10)
    number = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    randomNumber = "".join(random.choice(number) for i in range(rang))
    email = randomNumber + randomEmail
    return email

def get_random_pwd():
    """
    随机生成密码
    :return: PassWold
    """
    chars = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    rang = random.randint(6, 16)
    randomPWD = "".join(random.choice(chars) for i in range(rang))
    return randomPWD


