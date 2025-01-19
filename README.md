# new_autoshinyhunter_gui_version
new_autoshinyhunter_v4.0, made by Peter Yu.  

另有運行在 CMD 上的版本，[new_autoshinyhunter_cmd_version][1]。

[1]: https://github.com/peter890331/new_autoshinyhunter_cmd_version

> 一個在Pokémon GO中自動點擊色違且iv100的寶可夢的外掛腳本。    
> A game bot script that automatically clicks and only filters to those pokémons that is shiny and iv100 in Pokémon GO.
>
> I am a Taiwanese, so some instructions and description of parameters in the program are described in traditional Chinese, Taiwan No.1!!!!!

### ❗ 警告：僅以此練習程式編寫，請勿在遊戲中使用外掛，否則後果自負！本人對此內容不負任何法律責任。 ❗    
### ❗ WARNING: Practice programming only, please do not use it to cheat on the game!     
### The consequences are your own! I will not be responsible for any law liability to this content. ❗    
 <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/Pok%C3%A9mon%20GO%20icon.png" width="300px">

## Foreword
In Pokémon Go, beyond your pokémon’s CP (Combat Power), all your caught pokémons have semi-hidden base stats called individual values, or IVs. IVs determine how strong a Pokémon can potentially get. For example, a perfect IV Chansey will have a higher CP at its maxed out level, as opposed to a Chansey with only so-so IVs. There are just three stats to worry about: Attack, Defense, and Stamina, each of which maxes out at 15, and the pokémon with all three stats of 15 is called the iv100 pokémon, it means that this pokémon is the strongest in the same kind of pokémons. In addition, shiny pokémons are rare variants of pokémons that are differently colored than other pokémons of their species. In the game, the chance of having iv100 pokémons on the map is already very low, not to mention that it is also a shiny pokémon, so can see how difficult it is to obtain a pokémon with these two characteristics from the general game method.

## Overview
This game bot script can fully automatically send your game position to any location in the world where the specified iv100 pokémon appear, and click on the pokémon to determine whether it is a shiny, if not, then continue to try in the whole world, if yes, stop the script and wait for manual capture.    

Equipment and Software Requirements:
  1. A rooted Android phone with GPS JoyStick ([Google Play][2]) installed **IN THE SYSTEM**, install uiautomator2 ([Github][6]) services such as ATX-agent (may not be necessary for the new version), and of course, install Pokémon GO.
  2. A Windows computer.
  3. scrcpy ([Github][3], [scrcpy-win64-v2.7 download link][4]), this application mirrors Android devices connected via USB or over TCP/IP, and allows to control the device with the keyboard and the mouse of the computer.
  4. NemoADB by PokeNemo ([Official Website][5]), NemoADB is a GUI program useful to speed up your shundo snipe if you have an Android device with GPS Joystick and a Windows PC.
  5. A Discord ([Official Website][7]) account that has joined the Pokedex100 ([Official Website][8]) server, Pokedex100 provides pokémon coordinates all over 30 countries, it used to snipe iv100 pokémons. Free account is enough, no need to pay, because this game bot script also doesn't support croods crawler of donor channels.

[2]: https://play.google.com/store/apps/details?id=com.theappninjas.fakegpsjoystick
[3]: https://github.com/Genymobile/scrcpy
[4]: https://github.com/Genymobile/scrcpy/releases/download/v2.7/scrcpy-win64-v2.7.zip
[5]: https://www.pokenemo.com/nemoadb/
[6]: https://github.com/openatx/uiautomator2
[7]: https://discord.com/
[8]: https://pokedex100.com/

## How to use, For users
For users, you can directly download the final version in Releases, it contains a direct executable exe file.  
### Steps:
  1. Download the final version files in Releases, unzip each zip file into folders, then place the unziped folders with the new_autoshinyhunter_v4.0.exe file in the same folder you created, and for those who are not playing game in traditional Chinese, some of the template screenshots in the template folder will need to be re-screenshot in your game language.
  2. Download scrcpy and unzip it, then place in the the same folder you created too, the folder will look like this:   
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/folder%20looks%20like.png" width="200px">
  3. Run new_autoshinyhunter_v4.0.exe file.
     #### Home page
     First will be taken to the Home page, it contains a main window, the descriptions in the main window as follows:
     
     \- new_autoshinyhunter_v4.0 - made by Peter Yu.  

     \- 開始運行腳本前，請先記得先至左上角參數設定，  
     &nbsp;&nbsp;&nbsp;*Before start running the script, please remember go to the upper left "參數設定",*
     
     &nbsp;&nbsp;&nbsp;設定捕捉參數與爬蟲資料（csrftoken和sessionid偶爾需更新）。  
     &nbsp;&nbsp;&nbsp;*For setting capture parameters and crawler data (csrftoken and sessionid occasionally need to update).*
     
     > Need to set capture parameters and crawler data for the first time to use,  
     > or occasionally need to update the csrftoken and sessionid in crawler data;  
     > or need to change capture parameters if want to catch different Pokémons than last time.

     \- 確認設定完成後，直接點擊下方 開始運行腳本！  
     &nbsp;&nbsp;&nbsp;*After confirming the settings are complete, click below "開始運行腳本" to start the script!*

     So go to the upper left "參數設定" first, for setting capture parameters and crawler data, click "參數設定".

     #### Setting page
     After clicking "參數設定", will jump to the Setting page, and will also bring up the Setting tutorial, the descriptions of settings as follows:
     - channelid：  
     想要爬蟲的DC伺服器中Pokedex100的頻道ID，  
     *The channel ID of the Pokedex100 in the DC server that want to crawl,*

         在網頁版DC伺服器中Pokedex100的頻道的 F12 - Network - message?limit=50 - Request URl，  
     *F12 - Network - message?limit=50 - Request URl, for Pokedex100's channel in the web version of the DC server,*
     
       > Log in to the web version of DC, go to Pokedex100 and find the channel that want to crawl,  
       > click F12, then click F5 to refresh,  
       > then on the right screen, click Network - message?limit=50 - Request URl in order,  
       > that's the string of numbers in the Request URl, and paste it into the input box for channelid.

       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/channelid%201.png" width="500px">
     
         或網頁版DC伺服器中Pokedex100的頻道的網址最後一段數字。  
     *or the last string of numbers of the URL for Pokedex100's channel in the web version of the DC server.*

       > Log in to the web version of DC, go to Pokedex100 and find the channel that want to crawl,  
       > paste the last string of numbers of the URL into the input box for channelid.

         <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/channelid%202.png" width="500px">

     - L_wanted：
     想要捕捉的寶可夢至少等級。（限整數，預設為0）  
     *The minimum level of Pokémons want to capture. (Limit to an integer, default is 0)*

     - more_check：
     想要多確認寶可夢是不是色違的次數（建議取決於該寶可夢的跳躍頻率）。（限整數，預設為0）  
     *The number of times want to recheck whether the Pokémon is shiny or not (Recommend to depend on the jumping frequency of the Pokémon). (Limit to an integer, default is 0)*
     
