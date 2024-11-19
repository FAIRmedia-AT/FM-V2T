# FM-V2T Dataset: FAIRmedia English and German Video-to-Text (VTT) Annotations

## Overview
This dataset has been developed by [**JOANNEUM RESEARCH DIGITAL**](https://www.joanneum.at/digital/) as part of a collaborative research project. It contains short video clips derived from publicly available video sources with detailed annotations in English and German which are designed for tasks involving video-to-text (VTT) modeling and evaluation. The video captions specifically focus on long video descriptions which are tailored to LLM-based VTT methods, solely relying on visual inputs.

### Key Features
1. **Clips**: 258 manually curated short video clips, typically under 30 seconds, extracted using the [VidiCerT](https://www.vidicert.com/) shot boundary detector.
   - **Average Length**: 15.45 seconds.
   - **Min Length**: 5.12 seconds.
   - **Max Length**: 34.92 seconds.
   - **Median Length**: 13.63 seconds.
   - **STD of Length**: 7.79 seconds.
2. **Annotations**:
   - **Detailed Long Descriptions**: Generated using the [VideoLLama2](https://github.com/DAMO-NLP-SG/Video-LLaMA) VTT model and manually corrected for quality.
   - **Multiple Short Summary Descriptions**: Extracted 20 short single-sentence descriptions from detailed long descriptions using [ChatGPT](https://chatgpt.com/), formatted for [MSR-VTT](https://cove.thecvf.com/datasets/839) compatibility.
   - **Bilingual**: Long descriptions are available in English and German, with translations refined manually.
3. **No Audio**: Audio tracks have been excluded to focus exclusively on visual content.
4. **File Naming Convention**: `<CLIP_NR>_<VIDEO_NR>_<ID_FROM_URL>.ext` (e.g., `0_17_19F3A652-3AA-0032A-00000B64-19F2B6C5.webm`)

## License
This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. 

### Terms of Use
By using this dataset, you agree to the following:
1. Provide appropriate credit to [**JOANNEUM RESEARCH DIGITAL**](https://www.joanneum.at/digital/), link to the license, and indicate if changes were made.  
2. Not imply endorsement by the original authors or contributors without permission.  

For more details, see the full license text at [https://creativecommons.org/licenses/by/4.0/legalcode](https://creativecommons.org/licenses/by/4.0/legalcode).

## Directory Structure
```
FM-V2T/ 
├── README.md
├── LICENSE
├── annotations/
│ ├── clips-wvr-annotations-de.csv # German detailed annotations
│ ├── clips-wvr-annotations-eng.csv # English detailed annotations
│ ├── clips-wvr-msr-vtt-format.json # MSR-VTT formatted annotations
├── video_clips_metadata/
│ ├── Mediathek_WVR_Videos.xlsx # Metadata including download URLs
│ ├── VideoDownloader.py # Script for downloading original videos
│ ├── video_clips_cuts_info.csv # Metadata on video clips
├── img/ # Logos
```

## Annotation Details
- **Detailed Descriptions**:
  - English descriptions generated using [VideoLLama2](https://github.com/DAMO-NLP-SG/Video-LLaMA) with a 200-word prompt:
    <!-- PromptID = 18 -->
    ```
    Describe this video in detail, focus on what is visible. Limit the description to 200 words.
    ```
  - German translations produced using the [No Language Left Behind (NLLB)](https://ai.meta.com/research/no-language-left-behind/) model and manually refined.
- **Summary Descriptions**:
  - "gold_caption": 20 manually refined short captions created in the style of the [MSR-VTT](https://cove.thecvf.com/datasets/839) format, derived from detailed annotations using [ChatGPT](https://chatgpt.com/) with the prompt:
    ```
    I will give you a video caption and you have to extract the most important information into a short 10 word description and make different variations of the "pred_caption". These "gold_caption" are variations of the "pred_caption" and have the same meaning and maybe focus on a few other details from the original video caption and are all formulated in other words but without inventing any other details that where not in the original video caption. So similar like in the MSR_VTT dataset. 
    Here this is a example please also stay in this json format :
    {
        "video_id": "video8440",
        "pred_caption": "Wrestler in yellow trunks dominates match, opponent in orange trunks is defeated.",
        "gold_caption": [
            "a man gives commentary over wrestling",
            "a man hits another man while wrestling",
            "a man is punching another man in a wrestling match",
            "a professional wrestling match",
            "a wrestler gets punched while fighting hulk hogan",
            "a wrestler is winning his match",
            "hulk hogan fights in the ring",
            "hulk hogan wrestles another man in the wwe",
            "the boxing game ground",
            "the wrestler boots his opponent in the face",
            "two men pretend to fight in a ring",
            "two professional wrestlers are fighting in a ring",
            "two professional wrestlers are wrestling in front of a large crowd",
            "two wrestlers challenge each other",
            "ultimate warrior and hulk hogan",
            "wrestlers trading blows with each other",
            "wrestlers wrestling on television",
            "wwe sequence involving hulk hogan",
            "wrestlers wrestling on television",
            "ultimate warrior and hulk hogan"
        ]
    }
    ```

## Videos
### Metadata
- The `video_clips_cuts_info.csv` and the `Mediathek_WVR_Videos.xlsx` file provide detailed metadata for each clip, including:
  - URLs pointing to original video sources. (e.g. [19F3A652-3AA-0032A-00000B64-19F2B6C5.webm](https://www.mediathek.at/atom/19F3A652-3AA-0032A-00000B64-19F2B6C5))
  - Original and clip filenames with URL-IDs.
  - Timestamps for shot boundaries.
  - Keyframe statistics (e.g., count, distribution per second).

### Preparation Process
#### 1. Prepare the videos:
The [VideoDownloader.py](video_clips_metadata/VideoDownloader.py) script is included to facilitate the download of the original videos, utilizing the video URL information of the `Mediathek_WVR_Videos.xlsx` file.

#### 2. Generate the Clips:
After downloading the original videos, split them into short video clips using the `video_clips_cuts_info.csv` as a reference for shot boundaries and filenames.
Make sure to stick to the file naming convention described above.

NOTE: Only a selected subset of clips was annotated. Clips with faulty shot boundaries or poor quality were excluded from the annotations.

## Key Clips
During our initial tests with LLM-based Video-to-Text methods, we identified key clips that highlight specific challenges or qualities useful for qualitative evaluation of different models:
| Clip-ID   |  Description
|--------|-----
| 228_6_1D34CA5F-022-001DE-000077BA-1D3420AD.mp4 | Text description 1
| 169_26_1CF95195-145-0012C-0000156D-1CF8BF1D.mp4 | Text description 2
| 164_1_1CF94352-39C-000C2-0000156D-1CF8BF1D.mp4 | Text description 3
| 83_7_1CF6E58A-226-00007-000001D0-1CF61C1D.mp4 | Poster
| 10_2_1C534A29-3D7-000D6-00000FEC-1C526C36.mp4 | Known location: Uluru
| 143_32_1CF92973-052-00047-0000156D-1CF8BF1D.mp4 | Known location: Wat Arun
| 146_3_1CF92E87-001-00060-0000156D-1CF8BF1D.mp4 | Known location: Hongkong at night
| 146_3_1CF92E87-001-00060-0000156D-1CF8BF1D.mp4 | Known location: Hongkong Jumbo Restaurant
| 249_3_1D39F10B-3C6-004AD-00001946-1D3966AD.mp4 | Known location: Vienna train station
| 130_5_1CF814FF-3C6-00050-000003E4-1CF61C1DD.mp4 | Known location: Helsinki harbor
| 85_43_1CF6E9A7-128-0000C-000001D0-1CF61C1D.mp4 | Cars in American city
| 15_2_1C5477A5-255-00119-0000069C-1C53BDB6.mp4 | Tennis
| 132_6_1CF81A56-384-00054-000003E4-1CF61C1D.mp4 | Gold mining
| 264_9_1F1F7234-1E3-00174-000061A1-1F1E8EAD.mp4 | Paraglider
| 6_13_19F500FE-1F5-00249-000007D8-19F40846.mp4 | Train station


## Contact
For inquiries about this dataset, please reach out to:  
- [Werner Bailer](mailto:werner.bailer@joanneum.at)  
- [Stefan Arzberger](mailto:stefan.arzberger@joanneum.at)  


## Acknowledgement

FAIRmedia is funded the Austrian Federal Ministry for Climate Action, Environment, Energy, Mobility, Innovation and Technology in the programme Digital Technologies.

<img src="img/BMK_Logo_srgb.png" width="200"/><img src="img/ffg_logo.png" width="200"/>
