#!/usr/bin/env python3
"""
シンプルな挨拶プログラム
"""

def greet(name: str) -> str:
    """
    名前を受け取って挨拶メッセージを返す関数
    
    Args:
        name: 挨拶する相手の名前
    
    Returns:
        挨拶メッセージ
    """
    return f"こんにちは、{name}さん！"


def main():
    """メイン関数"""
    print(greet("世界"))
    print("このプログラムは正常に動作しています。")


if __name__ == "__main__":
    main()
