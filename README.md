# FM-V2T Dataset: FAIRmedia English and German Video-to-Text (V2T) Annotations

## Publication: ACM Multimedia 2025
The **FM-V2T Dataset** is published alongside our paper  
[**A Dataset and Metric for Textual Video Content Description**](https://doi.org/10.1145/3746027.3758224)  
(see [alternative link](https://zenodo.org/records/17287642))  
appearing in the *Proceedings of the 33rd ACM International Conference on Multimedia (ACM MM 2025)*.

This publication introduces both the dataset and a dedicated **LLM-based semantic correspondence metric** designed for evaluating video-to-text models. The prompts used for LLMFactsF1 can be found at `PAPER/LLMFactsF1_prompts`

### Updated Results
Revising the dataset, we discovered a minor issue with the **ShortRefs** counting 21 captions for each clip instead of the expected 20. The **updated results 🟩** show very marginal differences and appear just below the *inaccurate results 🟥* for comparison. For completeness, the outdated file is archived in `annotations/archive/clips-wvr-msr-vtt-format_21.json`.

| Model        | Ref        | Pred      | Words     | LLMFactsF1     | METEOR        | BLEU-1        | BLEU-2        | ROUGE-L       | CosPar        | CosSent       |
|---------------|-------------|-----------|------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| VideoLLama    | Ref         | Long-200  | 148±31     | 0.496±0.146    | 0.212±0.035    | 0.390±0.091    | 0.245±0.073    | 0.296±0.052    | 0.751±0.113    | 0.670±0.087    |
| InternLM      | Ref         | Long-200  | 136±22     | 0.529±0.184    | 0.198±0.047    | 0.380±0.085    | 0.223±0.083    | 0.283±0.072    | 0.711±0.112    | 0.648±0.099    |
| Tarsier       | Ref         | Long-200  | 59±14      | 0.476±0.175    | 0.135±0.032    | 0.257±0.107    | 0.150±0.069    | 0.257±0.047    | 0.771±0.092    | 0.644±0.094    |
| InternLM      | Ref         | Medium-50 | 61±22      | 0.508±0.186    | 0.129±0.044    | 0.248±0.125    | 0.142±0.086    | 0.246±0.065    | 0.729±0.108    | 0.640±0.101    |
| InternLM      | Ref         | Short-25  | 49±30      | 0.473±0.207    | 0.106±0.051    | 0.173±0.153    | 0.097±0.092    | 0.205±0.072    | 0.682±0.125    | 0.653±0.116    |
| InternLM      | Ref         | Brief-10  | 10±3       | 0.431±0.230    | 0.033±0.015    | 0.002±0.014    | 0.001±0.007    | 0.085±0.034    | 0.629±0.121    | 0.686±0.124    |
| 🟥 *InternLM*  | *ShortRefs-21* | *Brief-10* | *10±3* | *-* | *0.213±0.076* | *0.720±0.182* | *0.450±0.226* | *0.415±0.144* | *-* | *-* |
| 🟩 **InternLM** | **ShortRefs** | **Brief-10** | **10±3** | **-** | **0.213±0.077** | **0.717±0.183** | **0.444±0.227** | **0.413±0.145** | **-** | **-** |
| 🟥 *Tarsier*   | *ShortRefs-21* | *Brief-10* | *20±35* | *-* | *0.204±0.067* | *0.588±0.158* | *0.350±0.181* | *0.372±0.120* | *-* | *-* |
| 🟩 **Tarsier** | **ShortRefs** | **Brief-10** | **20±35** | **-** | **0.204±0.066** | **0.590±0.160** | **0.353±0.183** | **0.373±0.120** | **-** | **-** |


## Overview
This dataset has been developed by [**JOANNEUM RESEARCH DIGITAL**](https://www.joanneum.at/digital/en/) as part of a collaborative research project. It contains short video clips derived from publicly available video sources with detailed annotations in English and German which are designed for tasks involving video-to-text (V2T) modeling and evaluation. The video captions specifically focus on long video descriptions which are tailored to LLM-based V2T methods, solely relying on visual inputs. For a brief video overview of the dataset creation process, visit the [**FAIRmedia**](https://www.joanneum.at/digital/projekte/fairmedia/) project website.

### Key Features
1. **Clips**: 258 manually curated short video clips, typically under 30 seconds, extracted using the [VidiCert](https://www.vidicert.com/) shot boundary detector.
   - **Average Length**: 15.45 seconds.
   - **Min Length**: 5.12 seconds.
   - **Max Length**: 34.92 seconds.
   - **Median Length**: 13.63 seconds.
   - **STD of Length**: 7.79 seconds.
2. **Annotations**:
   - **Detailed Long Descriptions**: Generated using the [VideoLLama2](https://github.com/DAMO-NLP-SG/Video-LLaMA) V2T model with manual correction for quality.
   - **Multiple Short Summary Descriptions**: Extracted 20 short single-sentence descriptions from detailed long descriptions using [ChatGPT](https://chatgpt.com/), formatted for [MSR-VTT](https://cove.thecvf.com/datasets/839) compatibility.
   - **Bilingual**: Long descriptions are available in English and German, with translations refined manually.
3. **No Audio**: Audio tracks have been excluded to focus exclusively on visual content.
4. **File Naming Convention**: `<CLIP_NR>_<VIDEO_NR>_<ID_FROM_URL>.ext` (e.g., `0_17_19F3A652-3AA-0032A-00000B64-19F2B6C5.webm`)



## Directory Structure
```
FM-V2T/ 
├── README.md
├── annotations/
│ ├── clips-wvr-annotations-de.csv # German detailed annotations
│ ├── clips-wvr-annotations-eng.csv # English detailed annotations
│ ├── clips-wvr-msr-vtt-format.json # MSR-VTT formatted annotations
├── video_clips_metadata/
│ ├── Mediathek_WVR_Videos.xlsx # Metadata including download URLs
│ ├── VideoDownloader.py # Script for downloading original videos
│ ├── video_clips_cuts_info.csv # Metadata on video clips
├── PAPER/
│ ├── prompts/ # Detailed Prompts used
│ ├── qualitative_example_table3/ # Video used for metric validation
│ ├── results_prompt_experiments/ # Interactive plots from initial prompt experiments
```

## Annotation Details
- **Detailed Descriptions**:
  - English descriptions are manually corrected after pre-describing videos using [VideoLLama2](https://github.com/DAMO-NLP-SG/Video-LLaMA) with a 200-word prompt:
    <!-- PromptID = 18 -->
    ```
    Describe this video, exactly and only focus on what is visible, without imagining any details that are not visible! Answer what can be seen, where the video was shot, what persons, animals or buildings etc. can be seen. What is happening in the video? When was the video filmed at day or night for example ... Is there something unique to this video? Limit the description to 200 words!
    ```
  - German translations are manually revised after producing proposal-translations using [No Language Left Behind (NLLB)](https://ai.meta.com/research/no-language-left-behind/).
- **Summary Descriptions**:
  - "gold_caption": 20 manually refined short captions created in the style of the [MSR-VTT](https://cove.thecvf.com/datasets/839) format, derived from detailed annotations using [ChatGPT](https://chatgpt.com/) with the prompt:
    ```
    I will give you a video caption and you have to extract the most important information into a short 10 word description and make different variations of the "pred_caption". These "gold_caption" are variations of the "pred_caption" and have the same meaning and maybe focus on a few other details from the original video caption and are all formulated in other words but without inventing any other details that where not in the original video caption. So similar like in the MSR_VTT dataset. 
    Here this is a example please also stay in this json format :
    {
        "video_id": "video8440",
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
After downloading the original videos, split them into short video clips using the `video_clips_cuts_info.csv` as a reference for shot boundaries and filenames. For example, [FFmpeg](https://www.ffmpeg.org/) can be used for this purpose.
Make sure to stick to the file naming convention described above.

NOTE: Only a selected subset of clips was annotated. Clips with faulty shot boundaries or poor quality were excluded of annotation candidates. Finally, only a single clip per original video was randomly sampled.

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

## 


## Contact
For inquiries about this dataset, please reach out to:  
- [Werner Bailer](mailto:werner.bailer@joanneum.at)  
- [Stefan Arzberger](mailto:stefan.arzberger@joanneum.at)  

## License
This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. 

## Acknowledgement

FAIRmedia is funded the Austrian Federal Ministry for Climate Action, Environment, Energy, Mobility, Innovation and Technology in the programme Digital Technologies.

<img src="img/BMK_Logo_srgb.png" width="200"/><img src="img/ffg_logo.png" width="200"/>
