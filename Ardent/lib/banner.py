from colorama import Fore


def get_banner():
    banner = "Welcome to...\n" + Fore.LIGHTBLACK_EX
    banner += """                             ,,
      db                   `7MM                     mm    .M\"\"\"bgd
     ;MM:                    MM                     MM   ,MI    \"Y
    ,V^MM.    `7Mb,od8  ,M\"\"bMM  .gP\"Ya `7MMpMMMb.mmMMmm `MMb.      ,p6\"bo   ,6\"Yb.  `7MMpMMMb.
   ,M  `MM      MM' \"',AP    MM ,M'   Yb  MM    MM  MM     `YMMNq. 6M'  OO  8)   MM    MM    MM
   AbmmmqMA     MM    8MI    MM 8M\"\"\"\"\"\"  MM    MM  MM   .     `MM 8M        ,pm9MM    MM    MM
  A'     VML    MM    `Mb    MM YM.    ,  MM    MM  MM   Mb     dM YM.    , 8M   MM    MM    MM
.AMA.   .AMMA..JMML.   `Wbmd\"MML.`Mbmmd'.JMML  JMML.`MbmoP\"Ybmmd\"   YMbmd'  `Moo9^Yo..JMML  JMML.
         Created by: @CalumBoal                                https://onsecurity.co.uk"""
    banner += Fore.RESET + "\n"
    return banner
