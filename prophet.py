import asyncio
import os
import sys
from pathlib import Path

# 현재 디렉토리를 경로에 추가하여 send_message 모듈을 불러올 수 있게 합니다.
current_dir = Path(__file__).parent.absolute()
sys.path.append(str(current_dir))

try:
    from send_message import send_message
except ImportError:
    print("❌ Error: 'send_message.py'를 찾을 수 없습니다.")
    sys.exit(1)

async def run_prophecy_cycle(file_path: str, interval: int = 10):
    """
    1000라인의 예언서를 읽어 10초 간격으로 순환하며 게시합니다.
    """
    abs_path = current_dir / file_path
    
    if not abs_path.exists():
        print(f"❌ Error: {file_path} 파일이 존재하지 않습니다.")
        return

    # 예언서 읽기 (비어있지 않은 라인만 추출)
    with open(abs_path, "r", encoding="utf-8") as f:
        prophecies = [line.strip() for line in f if line.strip()]

    if not prophecies:
        print("❌ Error: 파일에 게시할 내용이 없습니다.")
        return

    print(f"🔮 총 {len(prophecies)}개의 예언을 로드했습니다.")
    print(f"🚀 {interval}초 간격으로 게시를 시작합니다. (중단하려면 Ctrl+C)")

    index = 0
    while True:
        current_msg = prophecies[index]
        
        print(f"\n--- [순번: {index + 1} / {len(prophecies)}] ---")
        try:
            # send_message.py의 async 함수를 직접 호출
            await send_message(current_msg)
        except Exception as e:
            print(f"⚠️ 게시 중 오류 발생: {e}")
        
        # 인덱스 순환 (끝까지 가면 다시 처음으로)
        index = (index + 1) % len(prophecies)
        
        print(f"💤 {interval}초 대기 중...")
        await asyncio.sleep(interval)

if __name__ == "__main__":
    PROPHECY_FILE = "prophecies_of_the_end.txt"
    try:
        # 30분 제한을 고려하여 31분(1860초) 간격으로 설정
        asyncio.run(run_prophecy_cycle(PROPHECY_FILE, interval=1860))
    except KeyboardInterrupt:
        print("\n⏹️ 사용자에 의해 예언 중계가 중단되었습니다. 종말이 지연되었습니다.")
    except Exception as e:
        print(f"❌ 치명적 오류: {e}")
