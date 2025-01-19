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
     > or need to change capture parameters if you want to catch different pokémons than last time.

     \- 確認設定完成後，直接點擊下方 開始運行腳本！  
     &nbsp;&nbsp;&nbsp;*After confirming the settings are complete, click below "開始運行腳本" to start the script!*

     So go to the upper left "參數設定" first, for setting capture parameters and crawler data, click "參數設定".

     #### Setting page
     After clicking "參數設定", will jump to the Setting page, and will also bring up the Setting tutorial,  

     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/setting%201.png" width="500px">
     
     the descriptions of settings as follows:  
     - channelid：  
     想要爬蟲的DC伺服器中Pokedex100的頻道ID，  
     *The channel ID of the Pokedex100 in the DC server that you want to crawl,*

         在網頁版DC伺服器中Pokedex100的頻道的 F12 - Network - message?limit=50 - Request URl，  
     *F12 - Network - message?limit=50 - Request URl, for Pokedex100's channel in the web version of the DC server,*
     
       > Log in to the web version of DC server, go to Pokedex100 and find the channel that you want to crawl,  
       > click F12, then click F5 to refresh,  
       > then on the right screen, click Network - message?limit=50 - Request URl in order,  
       > that's the string of numbers in the Request URl, and paste it into the input box for "請輸入 channelid".

       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/channelid%201.png" width="500px">
     
         或網頁版DC伺服器中Pokedex100的頻道的網址最後一段數字。  
     *or the last string of numbers of the URL for Pokedex100's channel in the web version of the DC server.*

       > Log in to the web version of DC server, go to Pokedex100 and find the channel that you want to crawl,  
       > paste the last string of numbers of the URL into the input box for "請輸入 channelid".

       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/channelid%202.png" width="500px">

     - L_wanted：
     想要捕捉的寶可夢至少等級。（限整數，預設為0）  
     *The minimum level of pokémons you want to catch. (Limit to an integer, default is 0)*

       > Type in the input box for "請輸入 L_wanted".

     - more_check：
     想要多確認寶可夢是不是色違的次數（建議取決於該寶可夢的跳躍頻率）。（限整數，預設為0）  
     *The number of times of recheck whether the pokémon is shiny or not (Recommend to depend on the jumping frequency of the pokémon). (Limit to an integer, default is 0)*
       > Type in the input box for "請輸入 more_check".

     - check_delay：
     想要多確認寶可夢是否色違的間隔（建議取決於該寶可夢的上下移動頻率）。（限整數，預設為2）  
     *The delay time of recheck whether the pokémon is shiny or not (Recommend to depend on the up and down frequency of the pokémon). (Limit to an integer, default is 2)*

       > Type in the input box for "請輸入 check_delay".
       
     - wifi_delay：
     使用Wifi-連接模式時想要多等待的延遲時間（取決於網路速度）。（限整數，預設為0）  
     *The delay time want to wait when using Wifi-connect mode (Depend on network speed). (Limit to an integer, default is 0)*

       > Type in the input box for "請輸入 wifi_delay".
       
     - check_position：  
     遊戲視角畫面最大化時設置為0；  
     *Set to 0 when the game perspective is maximized;*

       > Type 0 in the input box for "請輸入 check_position".

       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/maximized%20game%20perspective.png" width="200px">

         遊戲視角畫面最小化時則設置為1（適合會飛行則不在腳邊的寶可夢，ex：飛翔皮卡丘）。（限0、1，預設為0）  
     *Set to 1 when the game perspective is minimized (Suitable for those pokémons that can fly or not beside the feet, ex: Flying Pikachu). (Limits 0, 1, default is 0)*

       > Type 1 in the input box for "請輸入 check_position".
       
       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/minimized%20game%20perspective.png" width="200px">

     - male_and_female：  
     若想要捕捉特定性別的寶可夢，  
     *If you want to catch pokémons of a specific gender,*

         公的設置為1；母的設置為0；若不指定，則空白。（限0、1和空白，預設為空白）  
     *Male is set to 1; Female is set to 0; if not specified, then blank. (Limits 0, 1, default is blank)*

       > Type in the input box for "請輸入 male_and_female".

     - specific_pokemon：  
     若在DC伺服器中Pokedex100的頻道中含有多種寶可夢但只想抓取特定幾種時；  
     *If there are multiple pokémons in the channel of the Pokedex100 in the DC server, but you only want to catch a few specific of them;*

         或在DC伺服器中Pokedex100的頻道中的寶可夢異常不具有色違符號時，  
     *or if a pokémon in the channel of the Pokedex100 in the DC server abnormally does not have a shiny symbol,*

         打上寶可夢名字（寶可夢間以半形逗號（需切換至英文輸入法）相隔，ex：Cranidos,Hisuian Voltorb,Larvitar）；若無，則空白。  
     *type the name of those pokémons (Pokémons need to be separated by semi-commas (need to switch to English input mode), ex: Cranidos,Hisuian Voltorb,Larvitar); if not, then blank.*

       > Note that when blank, will only click on those pokémons that normally have shiny symbol, if those pokémons you want to capture abnormally does not have a shiny symbol, still need to type the name of those pokémons to click on it individually.

     - phone_name：  
     手機在scrcpy的視窗名。
     *The window name of your phone in scrcpy.*

       > It is recommended that run scrcpy once before setting this phone_name to determine the window name, the way to run scrcpy is: after enable USB debugging on the phone and connecting to the computer with USB, run scrcpy.exe directly.

     - DC_headers：  
     網頁版DC的授權碼，在網頁版DC的 F12 - Network - message?limit=50 - Headers - authorization。  
     *F12 - Network - message?limit=50 - Headers - authorization, the authorization for the web version of the DC server.*

       > Log in to the web version of DC server, go to Pokedex100 and find the channel that you want to crawl,  
       > click F12, then click F5 to refresh,  
       > then on the right screen, click Network - message?limit=50 - Headers - authorization in order,  
       > that's the string of authorization, and paste it into the input box for "請輸入 DC_headers".

       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/DC_headers.png" width="500px">

     - Pokedex100_header_Cookie_csrftoken：  
     Pokedex100的Cookie，在Pokedex100座標網頁的 F12 - Network - Document - Headers - Cookie - csrftoken。  
     *Cookies for Pokedex100, F12 - Network - Document - Headers - Cookie - csrftoken, in the web page of Pokedex100.*

       > Click on the "Click for Coords" button of a pokémon in Pokedex100 channel randomly,
  
       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/Pokedex100_header_Cookie_csrftoken%201.png" width="500px">
       
       > then you will be directed to the Pokedex100 web page,  
       > and after authorizate with your DC account, press F12 on the browser,  
       > then you can find the string in the Network - Document - Cookie - csrftoken, the whole string is Pokedex100_header_Cookie_csrftoken,  
       > paste the string into the input box for "請輸入 Pokedex100_header_Cookie_csrftoken".  
       > (if you don't find it, press F5 and look again).

       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/Pokedex100_header_Cookie_csrftoken%202.png" width="500px">
        
     - Pokedex100_header_Cookie_sessionid：  
     Pokedex100的Cookie，在Pokedex100座標網頁的 F12 - Network - Document - Headers - Cookie - sessionid。
     *Cookies for Pokedex100, F12 - Network - Document - Headers - Cookie - sessionid, in the web page of Pokedex100.*

       > Click on the "Click for Coords" button of a pokémon in Pokedex100 channel randomly,
       
       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/Pokedex100_header_Cookie_csrftoken%201.png" width="500px">

       > then you will be directed to the Pokedex100 web page,  
       > and after authorizate with your DC account, press F12 on the browser,  
       > then you can find the string in the Network - Document - Cookie - sessionid, the whole string is Pokedex100_header_Cookie_sessionid,  
       > paste the string into the input box for "請輸入 Pokedex100_header_Cookie_sessionid".  
       > (if you don't find it, press F5 and look again).

       <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/Pokedex100_header_Cookie_sessionid.png" width="500px">
       
     This completes the settings, click "儲存" below to save.  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/setting%201.png" width="500px">

     #### Home page
     After clicking "儲存", will jump return the Home page.

     \- 確認設定完成後，直接點擊下方 開始運行腳本！  
     &nbsp;&nbsp;&nbsp;*After confirming the settings are complete, click below "開始運行腳本" to start the script!*

     Click "開始運行腳本" to start the script.

     \- 開始運行腳本！  
     &nbsp;&nbsp;&nbsp;*Start running the script!*

     \- 已自動開啟 NemoADB.exe，並將其最小化。  
     &nbsp;&nbsp;&nbsp;*Automatically opened NemoADB.exe and minimized it.*

     > At this point you will see NemoADB.exe open automatically and minimized it,  
     > if it doesn't open automatically, it will display
     > 
     \- 開啟 NemoADB.exe 失敗，請手動開啟。  
     &nbsp;&nbsp;&nbsp;*Open NemoADB.exe failed, please open it manually.*
     
     > please open NemoADB.exe manually,  
     > if successfully opened, it will display
     
     \- 已手動開啟 NemoADB.exe，並將其最小化。  
     &nbsp;&nbsp;&nbsp;*Manually opened NemoADB.exe and minimized it.*
 
     \- 請將手機啟用AtxAgent，  
     &nbsp;&nbsp;&nbsp;*Please enable AtxAgent on your phone,*
     
     &nbsp;&nbsp;&nbsp;開啟GPS Joystick傳送至任意位置並隱藏，  
     &nbsp;&nbsp;&nbsp;*turn on the GPS Joystick and send your game position to any location then hide it,*
     
     &nbsp;&nbsp;&nbsp;開啟Pokemon Go並確認遊戲視角與記事本設定相同。  
     &nbsp;&nbsp;&nbsp;*open Pokémon Go and make sure the game perspective is the same as setting.*
     
     \- 確認完成後，直接點擊下方 手機已就緒！  
     &nbsp;&nbsp;&nbsp;*After confirming are complete, click below "手機已就緒"!*

     Click "手機已就緒".

     \- 手機已就緒！  
     &nbsp;&nbsp;&nbsp;*The phone is ready!*
 
     \- 請點擊下方選擇手機連接模式，  
     &nbsp;&nbsp;&nbsp;*Please click below to select the phone connect mode.*
     
     &nbsp;&nbsp;&nbsp;USB連接：  請點擊 * USB-連接模式（建議）、  
     &nbsp;&nbsp;&nbsp;* USB connection: Please click * "USB-連接模式" (recommended)、*

     > Computer and phone connected via USB without delay.
     
     &nbsp;&nbsp;&nbsp;Wifi連接： 請點擊 * Wifi-連接模式。  
     &nbsp;&nbsp;&nbsp;* Wifi connection: Please click * "Wifi-連接模式".*

     > Computer and phone connected via Wifi may be delayed.

     Choose to click on a connect mode,
     if choose USB connection,

     \* USB-連接模式  
     &nbsp;&nbsp;&nbsp;*USB-connect mode*
 
     \- 請將手機以USB接上電腦，允許USB偵錯。  
     &nbsp;&nbsp;&nbsp;*Please connect the phone to the computer via USB to allow USB debugging.*
     
     > Please open and allow USB debugging on your phone.
     
     \- 確認完成後，直接點擊下方 手機已連接！  
     &nbsp;&nbsp;&nbsp;*After confirming are complete, click below "手機已連接"!*

     Click "手機已連接".
     
