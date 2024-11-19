"""
This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/

Copyright (c) 2024 JOANNEUM RESEARCH
"""
import pandas as pd
import requests
import os
import argparse


def updateLinksWVRMedia(old_links, base_url):
    updated_links = []
    for old_link in old_links:
        if 'atom/' in old_link:
            identifier = old_link.split('atom/')[1]
            new_link = f"{base_url}?t=media&i={identifier}&ft=webm"
            updated_links.append((new_link, identifier))
        else:
            print(f"Warning: 'atom/' not found in link: {old_link}")
    return updated_links

def downloadVideos(updated_links, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    for new_link, identifier in updated_links:
        response = requests.get(new_link, stream=True) # if SSL certificate expired, add verify=False to the request
        
        if response.status_code == 200:
            filename = f"{identifier}.webm"
            file_path = os.path.join(download_folder, filename)
            with open(file_path, "wb") as video_file:
                for chunk in response.iter_content(chunk_size=8192):
                    video_file.write(chunk)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download video from {new_link}. Status code: {response.status_code}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download videos from Mediathek WVR.')
    parser.add_argument('--download_folder', type=str, default='videos', help='Folder to download videos into')
    parser.add_argument('--input_excel', type=str, default='Mediathek_WVR_Videos.xlsx', help='Input Excel file name with public links')
    parser.add_argument('--output_excel', type=str, default='Updated_Mediathek_WVR_Videos.xlsx', help='Output Excel file name with updated download links')
    parser.add_argument('--base_url', type=str, default='https://h5.mediathek.at/cdn.php', help='Base URL for constructing new links')
    parser.add_argument('--links_col_nr', type=int, default=7, help='Column in the excel where the download link of the video is ...')
    args = parser.parse_args()

    download_link_cols = [args.links_col_nr]
    media_links = pd.read_excel(args.input_excel, usecols=download_link_cols)
    old_links = media_links.iloc[:, 0].tolist()
    updated_links = updateLinksWVRMedia(old_links, args.base_url) # Create a new function to get the list of media links that can be downloaded, this depends on the website...

    # updated_links_df = pd.DataFrame(updated_links, columns=['New Link', 'Identifier'])
    # updated_links_df.to_excel(args.output_excel, index=False)

    downloadVideos(updated_links, args.download_folder)
