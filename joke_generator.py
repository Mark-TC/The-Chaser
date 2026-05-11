import requests
import json

def get_random_joke():
    """
    从 JokeAPI 获取一个随机笑话
    这是一个免费的 API，不需要任何密钥
    """
    try:
        # API 的网址
        url = "https://official-joke-api.appspot.com/random_joke"
        
        # 发送请求到 API
        response = requests.get(url)
        
        # 检查请求是否成功
        if response.status_code == 200:
            # 将响应转换为 JSON 格式
            joke_data = response.json()
            
            # 提取笑话的内容
            joke_type = joke_data.get('type')
            setup = joke_data.get('setup')
            punchline = joke_data.get('punchline')
            
            # 打印笑话
            print("\n" + "="*50)
            print("😂 今天的笑话：")
            print("="*50)
            print(f"类型: {joke_type}")
            print(f"\n{setup}")
            print(f"\n{punchline}")
            print("="*50 + "\n")
        else:
            print("❌ 获取笑话失败，请稍后重试")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络错误: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ 数据解析错误: {e}")

def main():
    """
    主函数 - 程序的入口点
    """
    print("\n🎉 欢迎使用笑话生成器！")
    print("这个程序会从网络获取随机笑话给你\n")
    
    while True:
        # 获取用户输入
        user_input = input("按 Enter 获取笑话，或输入 'q' 退出: ").strip().lower()
        
        if user_input == 'q':
            print("\n👋 谢谢使用！再见！\n")
            break
        else:
            # 获取并显示笑话
            get_random_joke()

if __name__ == "__main__":
    # 这里是程序的起点
    main()
