import asyncio
import edge_tts
import os
from remove_file import remove_file
#from play_file import play_audio

VOICE = "en-AU-WilliamNeural"
BuFFER_SIZE = 1024

async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
    except Exception as e:
        print(f"Error : {e}")

# Example usage
if __name__ == "__main__":
    output_file = f"{os.getcwd()}/test_voice.mp3"
    asyncio.run(amain("Testing the voice module", output_file))
    print(f"Audio saved to {output_file}")