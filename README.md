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
    <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/NemoADB.png" width="200px">
  5. A Discord ([Official Website][7]) account that has joined the Pokedex100 ([Official Website][8]) server, Pokedex100 provides pokémon coordinates all over 30 countries, it used to snipe iv100 pokémons. Free account is enough, no need to pay, because this game bot script also doesn't support croods crawler of donor channels.  
    <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/Pokedex100.png" width="500px">

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
     First will be taken to the Home page, it contains a main window,  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/Home%20page.png" width="250px">

     the descriptions in the main window as follows:

     ---
     
     \- new_autoshinyhunter_v4.0 - made by Peter Yu.  

     \- 開始運行腳本前，請先記得先至左上角參數設定，  
     &nbsp;&nbsp;&nbsp;*Before start running the script, please remember go to the upper left "參數設定",*
     
     &nbsp;&nbsp;&nbsp;設定捕捉參數與爬蟲資料（csrftoken和sessionid偶爾需更新）。  
     &nbsp;&nbsp;&nbsp;*For setting capture parameters and crawler data (csrftoken and sessionid occasionally need to update).*
     
     > Need to set capture parameters and crawler data for the first time to use,  
     > or occasionally need to update the csrftoken and sessionid in crawler data;  
     > or need to change capture parameters if you want to catch different pokémons than last time.

     \- 確認設定完成後，直接點擊下方 開始運行腳本！  
     &nbsp;&nbsp;&nbsp;*After confirming the settings are complete, click below "開始運行腳本" to start running the script!*

     So go to the upper left "參數設定" first, for setting capture parameters and crawler data, click "參數設定".

     ---
     
     #### Setting page
     After clicking "參數設定", will jump to the Setting page, and will also bring up the Setting tutorial,
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/setting%201.png" width="700px">
     
     the descriptions of settings as follows:  
     - channelid：  
     想要爬蟲的DC伺服器中Pokedex100的頻道ID，  
     *The channel ID of the Pokedex100 in the DC server that you want to crawl,*

       > There is usually a channel called 100communitcy, or a special channel on community days,  
       > however, only free-to-use channels are supported,  
       > i.e. channels where the button displays "Click for Coords" instead of "Click for Donor coord".

         在網頁版DC伺服器中Pokedex100的頻道的 F12 - Network - message?limit=50 - Request URl，  
     *F12 - Network - message?limit=50 - Request URl, for Pokedex100's channel in the web version of the DC server,*
     
       > Log in to the web version of DC server, go to Pokedex100 and find the channel that you want to crawl,  
       > press F12, then press F5 to refresh,  
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

       > Note that when blank, will only check those pokémons that normally have shiny symbol, if those pokémons you want to capture abnormally does not have a shiny symbol, still need to type the name of those pokémons to check it individually.

     - phone_name：  
     手機在scrcpy的視窗名。
     *The window name of your phone in scrcpy.*

       > It is recommended that run scrcpy once before setting this phone_name to determine the window name, the way to run scrcpy is: after enable USB debugging on the phone and connecting to the computer with USB, run scrcpy.exe directly.

     - DC_headers：  
     網頁版DC的授權碼，在網頁版DC的 F12 - Network - message?limit=50 - Headers - authorization。  
     *F12 - Network - message?limit=50 - Headers - authorization, the authorization for the web version of the DC server.*

       > Log in to the web version of DC server, go to Pokedex100 and find the channel that you want to crawl,  
       > press F12, then press F5 to refresh,  
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
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/setting%202.png" width="700px">

     After saving, a parameter.json will appear in the folder,  
     so next time you don't need to reset all the settings, but still need to be aware that csrftoken and sessionid occasionally need to update.  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/folder%20looks%20like%20after%20saving.png" width="200px">

     ---
     
     #### Home page
     After clicking "儲存", will jump return the Home page.

     \- 確認設定完成後，直接點擊下方 開始運行腳本！  
     &nbsp;&nbsp;&nbsp;*After confirming the settings are complete, click below "開始運行腳本" to start running the script!*

     Click "開始運行腳本" to start running the script.

     ---
     
     \- 開始運行腳本！  
     &nbsp;&nbsp;&nbsp;*Start running the script!*

     \- 已自動開啟 NemoADB.exe，並將其最小化。  
     &nbsp;&nbsp;&nbsp;*Automatically opened NemoADB.exe and minimized it.*

     At this point you will see NemoADB.exe open automatically and minimized it,  
     if it doesn't open automatically, it will display
     
     \- 開啟 NemoADB.exe 失敗，請手動開啟。  
     &nbsp;&nbsp;&nbsp;*Open NemoADB.exe failed, please open it manually.*
     
     please open NemoADB.exe manually,  
     if successfully opened, it will display
     
     \- 已手動開啟 NemoADB.exe，並將其最小化。  
     &nbsp;&nbsp;&nbsp;*Manually opened NemoADB.exe and minimized it.*

     > Make sure NemoADB.exe is open, otherwise can't use GPS Joystick to send your game position.

     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/NemoADB.png" width="200px">
 
     \- 請將手機啟用AtxAgent，  
     &nbsp;&nbsp;&nbsp;*Please enable AtxAgent on your phone,*
     
     &nbsp;&nbsp;&nbsp;開啟GPS Joystick傳送至任意位置並隱藏，  
     &nbsp;&nbsp;&nbsp;*turn on the GPS Joystick and send your game position to any location then hide it,*

     > Manually turn on the GPS Joystick on your phone and send your game position to any location,  
     > or open any GPX and pause it, then hide it.
     
     &nbsp;&nbsp;&nbsp;開啟Pokemon Go並確認遊戲視角與記事本設定相同。  
     &nbsp;&nbsp;&nbsp;*open Pokémon Go and make sure the game perspective is the same as setting.*

     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/maximized%20game%20perspective.png" width="200px">
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/minimized%20game%20perspective.png" width="200px">
     
     \- 確認完成後，直接點擊下方 手機已就緒！  
     &nbsp;&nbsp;&nbsp;*After confirming are complete, click below "手機已就緒"!*

     Click "手機已就緒".

     ---
     
     \- 手機已就緒！  
     &nbsp;&nbsp;&nbsp;*The phone is ready!*
 
     \- 請點擊下方選擇手機連接模式，  
     &nbsp;&nbsp;&nbsp;*Please click below to select the phone connect mode,*
     
     &nbsp;&nbsp;&nbsp;USB連接：  請點擊 * USB-連接模式（建議）、  
     &nbsp;&nbsp;&nbsp;*USB connection: Please click * "USB-連接模式" (recommended)、*

     > Computer and phone connected via USB without delay.
     
     &nbsp;&nbsp;&nbsp;Wifi連接： 請點擊 * Wifi-連接模式。  
     &nbsp;&nbsp;&nbsp;*Wifi connection: Please click * "Wifi-連接模式".*

     > Computer and phone connected via Wifi may be delayed.

     Choose to click on a connect mode,
     
     ---
     #### USB-connect mode

     if choose USB connection,

     \* USB-連接模式  
     &nbsp;&nbsp;&nbsp;*USB-connect mode*
 
     \- 請將手機以USB接上電腦，允許USB偵錯。  
     &nbsp;&nbsp;&nbsp;*Please connect the phone to the computer via USB and allow USB debugging.*
     
     > Please remember to open and allow USB debugging on your phone.
     
     \- 確認完成後，直接點擊下方 手機已連接！  
     &nbsp;&nbsp;&nbsp;*After confirming are complete, click below "手機已連接"!*

     Click "手機已連接".
          
     ---
     #### Wifi-connect mode

     And if choose Wifi connection,

     \* Wifi-連接模式  
     &nbsp;&nbsp;&nbsp;*Wifi-connect mode*
 
     \- 請將手機連上Wifi並以USB接上電腦，允許USB偵錯，  
     &nbsp;&nbsp;&nbsp;*Please connect the phone to Wifi, and connect to the computer via USB and allow USB debugging,*

     > Connect your phone to the same Wifi network as your computer,  
     > and connect your phone to your computer via USB and allow USB debugging.  
     > Please remember to open and allow USB debugging on your phone.
     
     &nbsp;&nbsp;&nbsp;並在下方輸入手機的IP位置。  
     &nbsp;&nbsp;&nbsp;*enter the phone's IP address below.*

     > Enter your phone's IP address below (need to switch to English input mode),  
     > it can usually be found in the phone's settings, looks like: 192.XXX.XX.XXX.

     \- 確認完成後，直接點擊下方 手機已連接！。  
     &nbsp;&nbsp;&nbsp;*After confirming are complete, click below "手機已連接"!*

     Click "手機已連接".

     ---

     \- 已輸入手機IP地址: 192.XXX.XX.XXX。  
     &nbsp;&nbsp;&nbsp;*Already enter the phone's IP address: 192.XXX.XX.XXX*
 
     \- 手機已連接！  
     &nbsp;&nbsp;&nbsp;*The phone is connected!*

     \- 請將手機與電腦的USB連接拔除。  
     &nbsp;&nbsp;&nbsp;*Please disconnect the phone to the computer via USB.*
     
     \- 確認完成後，直接點擊下方 手機已拔除！  
     &nbsp;&nbsp;&nbsp;*After confirming are complete, click below "手機已拔除"!*

     > Disconnect your phone to your computer via USB.
     
     Click "手機已拔除".

     ---
     
     \- 手機已拔除！  
     &nbsp;&nbsp;&nbsp;*The phone is disconnect to the computer via USB!*
     
     ---
     
     \- 即將投影手機，  
     &nbsp;&nbsp;&nbsp;*Project the phone's screen to computer,*
     
     &nbsp;&nbsp;&nbsp;若手機需要允許USB偵錯，請在允許USB偵錯後重啟腳本。  
     &nbsp;&nbsp;&nbsp;*If the phone needs to allow USB debugging, please restart the script after allowing USB debugging.*
     
     &nbsp;&nbsp;&nbsp;若投影失敗請檢查問題後重啟腳本。  
     &nbsp;&nbsp;&nbsp;*If project failed, please check the problem and restart the script.*
 
     \- 請稍等，此時視窗可能暫時沒有回應，屬正常現象。  
     &nbsp;&nbsp;&nbsp;*Please wait for a while, it is normal that the script may not be responding at the moment.*

     \~ 開始時間：20XX-XX-XX XX\:XX:XX.XXXXXX  
     &nbsp;&nbsp;&nbsp;*Start time: 20XX-XX-XX XX\:XX:XX.XXXXXX*

     At this point you will see your phone's screen project to computer automatically,  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/project%20phone's%20screen.png" width="500px">
     
     there are three programs in total.  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/minimized.png" width="200px">

     \~ 腳本正在執行。  
     &nbsp;&nbsp;&nbsp;*The script is running.*
     
     ---
     
     Now, the script will starting to send your game position to any location in the world and starting to check if the pokémon is shiny.

     \~ 若發現手機畫面無法自動點擊，  
     &nbsp;&nbsp;&nbsp;*If notice that the phone screen is not automatically clickable,*
     
     &nbsp;&nbsp;&nbsp;請開啟AtxAgent並手動點擊"启动 UIAUTOMATOR"，  
     &nbsp;&nbsp;&nbsp;*Please open AtxAgent and click "启动 UIAUTOMATOR" manually,

     &nbsp;&nbsp;&nbsp;再返回遊戲即可。  
     &nbsp;&nbsp;&nbsp;*then can go back to the game.*
     
     > If you notice that your phone screen is not automatically clickable,
     > please close Pokémon Go first, find the ATX app,

     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/ATX.png" width="50px">
     
     > and click “启动 UIAUTOMATOR”, then can go back to the game.

     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/%E5%90%AF%E5%8A%A8%20UIAUTOMATOR.png" width="200px">

     If in the Pokedex100 channel you set, has a pokémon that matches your settings, the descriptions in the main window as follows:  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/start%20check.png" width="300px">

     \~ Tp to：43.550079,-79.748105  
     \~ Name：Poochyena (土狼犬), CP：329, L：17, ♂  
     \~ Checked：1  
     \~ Not Shiny or Clicked Error !

     It contains the coord send to, the name of the pokémon in English and traditional Chinese, CP, level, gender, and how many pokémons were checked.

     And if there is no pokémon that matches your settings for the time being, the instructions in the main window are as follows:  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/no%20crood.png" width="300px">

     \~ No new coord, waiting . . .

     > Just wait for new pokémons appear, wait for the Pokedex100 channel to update.

     When the shiny pokémon appeard and clicked on, the descriptions in the main window as follows:  
     <img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/shiny%20appear.png" width="300px">

     \~  !!! Shiny !!!
     
     \~ 結束時間：20XX-XX-XX XX\:XX:XX.XXXXXX  
     &nbsp;&nbsp;&nbsp;*End time: 20XX-XX-XX XX\:XX:XX.XXXXXX*

     \~  Please STOP the code !

     Then you can check if is clicked on the right pokémon, and catch it manually! Congratulations on getting a shiny and iv100 pokémon!

  5. Enjoy the convenience brought by this scripts 🤓.

---

## About anthor
#### Home page
About me and some of this script's introduction, can go to the upper left "作者介紹" to get it.

Click "作者介紹".

---

#### Author page
After clicking "作者介紹", will bring up the introduce about me and some of this script's introduction.  
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/author.png" width="300px">

---
## Some examples when using
### screen record
These videos are the gains of my actual use for a period of time.  
Includes previously captured using some [older script][1]s.  
(Click in to download to watch the full video.)

<a href="https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/screen-20250120-224249.mp4">
  <img src="https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/ezgif-7-54f9603501%20(1).gif" width="200" height=auto>
</a>

<a href="https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/screen-20250120-224537.mp4">
  <img src="https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/ezgif-7-6bb932a945%20(1).gif" width="200" height=auto>
</a>

<a href="https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/screen-20250120-224729.mp4">
  <img src="https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/ezgif-7-615d77c1e1%20(1).gif" width="200" height=auto>
</a>

### screenshot
These screenshots are my actual usage, including testing while developing, I also like to use the script while doing other things, while I focus on other things, the script will continue to click pokémons for me.  
Includes previously captured using [older script][1].

#### [new_autoshinyhunter_cmd_version][1], [older script][1]：
<p>
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/1.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/2.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/3.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/4.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/5.png" width="100px">
</p><p>
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/6.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/7.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/8.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/9.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/10.png" width="100px">
</p><p>
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/11.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/12.jpg" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v3.0/13.png" width="100px">
<p>

#### new_autoshinyhunter_gui_version, this script：
<p>
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v4.0/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-07%20223448.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v4.0/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-27%20230831.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v4.0/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-28%20173747.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter_gui_version/blob/figures/new_autoshinyhunter_v4.0/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-30%20234051.png" width="100px">
<p>

### live stream
This is the playlist of live stream of my actual use, occasionally live stream.  
The right side of each live stream will show current pokémons to check on, and the down side will also have current description.

[Pokémon GO 自製外掛腳本直播][9]

[9]: https://www.youtube.com/watch?v=8h2jUKUrAkY&list=PLN0w7j_rRAO8jQKUtQZqwDHsG4QiPCuCx&pp=gAQB

---

## Notes
### scrcpy
scrcpy ([Github][3], [scrcpy-win64-v2.7 download link][4]), this application mirrors Android devices connected via USB or over TCP/IP, and allows to control the device with the keyboard and the mouse of the computer.  
Here are some command steps can use to test the Wifi connection mode:
1. cd /d C:\Users\XXX\scrcpy-win64-vX.XX
2. adb tcpip 5555
3. adb connect 192.XXX.XX.XXX:5555
4. scrcpy -t -b2M -m800
   
Then here are two useful shortcuts to turn off the phone screen while connected:
- Turn device screen off (keep mirroring):	MOD+o
- Turn device screen on:	MOD+Shift+o  
  (MOD key is usually Alt)
  
And a traditional Chinese teaching video on [Youtube][10].

[10]: https://youtu.be/WkTd5OxDZ-8

### WindowThumbnail
If you are using your computer to do other things at the same time as running this script, and want to keep checking if shiny pokémon has appeared, you can use WindowThumbnail ([Github][11], [WindowThumbnail-v1.0 download link][13]) to continuously displays your phone screen or the cmd of this script in a small window on the upper level of your computer.

And a traditional Chinese tutorial on [巴哈姆特][12].

[11]: https://github.com/neilchennc/WindowThumbnail
[12]: https://forum.gamer.com.tw/Co.php?bsn=19017&sn=318177
[13]: https://github.com/neilchennc/WindowThumbnail/releases/download/v1.0/WindowThumbnail-v1.0.exe


### PyInstaller
If there are updates to this script in the future, can use PyInstaller to package the .py file into an .exe file, use 'pyinstaller -F XXX.py' command,  
to add your own icon, use 'pyinstaller --onefile --windowed --icon=icon.ico XXX.py' command.

---

### ❗ 警告：僅以此練習程式編寫，請勿在遊戲中使用外掛，否則後果自負！本人對此內容不負任何法律責任。 ❗    
### ❗ WARNING: Practice programming only, please do not use it to cheat on the game!     
### The consequences are your own! I will not be responsible for any law liability to this content. ❗    
