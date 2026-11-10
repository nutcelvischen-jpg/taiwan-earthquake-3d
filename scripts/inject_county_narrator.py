import os
import json

counties_info = {
  "花蓮縣": {
    "badge": "M 7.2 強震 (2024)",
    "desc": "2024年4月3日規模7.2強震，為板塊隱沒前緣逆衝錯動，釀成太魯閣落石、天王星大樓傾斜；2018年亦有0206規模6.2米崙斷層震災。",
    "beats": [
      {
        "voice_text": "花蓮縣歷史上最強烈有感地震，是2024年4月3日壽豐鄉外海發生的規模7.2強震，深度僅15.5公里。",
        "location": "花蓮壽豐外海震央",
        "camera": { "lon": 121.67, "lat": 23.77, "depth": 15.5, "dist": 80, "tilt": 45 },
        "subtitle": "2024/04/03 規模 7.2 · 震源深度 15.5 km · 菲律賓海板塊向北隱沒推擠"
      },
      {
        "voice_text": "花蓮地處歐亞板塊與菲律賓海板塊碰撞前緣，強震造成蘇花公路崇德段嚴重坍方，米崙斷層破裂帶市區多處建築受損。",
        "location": "花蓮米崙斷層帶",
        "camera": { "lon": 121.61, "lat": 23.98, "depth": 10.0, "dist": 60, "tilt": 35 },
        "subtitle": "米崙斷層地表破裂與太魯閣落石崩塌 · 歷史震度達 6 強"
      },
      {
        "voice_text": "在3D視圖中，向東傾斜的密集震源清晰展示了板塊隱沒的班尼奧夫帶，花蓮長年為臺灣地震釋放能量最頻繁的區域。",
        "location": "花蓮東部海域隱沒帶",
        "camera": { "lon": 121.5, "lat": 23.9, "depth": 40.0, "dist": 130, "tilt": 30 },
        "subtitle": "班尼奧夫帶立體剖面 · 累積逾 4,800 筆密集餘震"
      }
    ]
  },
  "南投縣": {
    "badge": "M 7.3 (921大地震)",
    "desc": "1999年9月21日凌晨集集發生規模7.3大地震，震源深度僅8公里，車籠埔斷層垂直破裂近10公尺，為百年傷亡最重震災。",
    "beats": [
      {
        "voice_text": "南投縣歷史上最強烈的地震，正是1999年9月21日凌晨1點47分發生的921集集大地震，芮氏規模達到7.3。",
        "location": "南投縣集集鎮",
        "camera": { "lon": 120.82, "lat": 23.85, "depth": 8.0, "dist": 75, "tilt": 45 },
        "subtitle": "1999/09/21 規模 7.3 · 震源深度 8.0 km · 臺灣世紀大震"
      },
      {
        "voice_text": "車籠埔斷層地表撕裂長達100公里，最大垂直錯距達9.8公尺，並誘發國姓鄉九份二山3500萬立方公尺的大規模崩塌形成堰塞湖。",
        "location": "九份二山崩塌地",
        "camera": { "lon": 120.84, "lat": 23.97, "depth": 10.0, "dist": 65, "tilt": 35 },
        "subtitle": "車籠埔斷層逆衝抬升9.8m · 九份二山大走山"
      },
      {
        "voice_text": "全年度南投與中部山區觀測到多達16次規模6以上強烈餘震，地貌劇烈改變，是臺灣現代防災史的重要轉折點。",
        "location": "南投中央山脈全景",
        "camera": { "lon": 120.91, "lat": 23.87, "depth": 30.0, "dist": 140, "tilt": 25 },
        "subtitle": "1999年餘震破 5,900 次 · 臺灣防震建築法規全面升級"
      }
    ]
  },
  "台南市": {
    "badge": "M 6.3 / M 6.6",
    "desc": "1964年白河地震（M 6.3）與2016年美濃地震（M 6.6場址效應），引發永康維冠大樓倒塌與白河嚴重地裂與火災。",
    "beats": [
      {
        "voice_text": "臺南市近代受創最深的地震包括1964年規模6.3的白河大地震，以及2016年2月6日規模6.6的美濃地震。",
        "location": "臺南市白河區",
        "camera": { "lon": 120.45, "lat": 23.37, "depth": 18.0, "dist": 80, "tilt": 40 },
        "subtitle": "1964 白河大地震 (M 6.3) · 觸口斷層逆衝"
      },
      {
        "voice_text": "2016年美濃地震震波向西北傳遞，在臺南軟弱沖積層產生盆地聚焦效應，造成永康維冠金龍大樓倒塌，震度達到7級。",
        "location": "臺南永康區",
        "camera": { "lon": 120.25, "lat": 23.01, "depth": 15.0, "dist": 65, "tilt": 35 },
        "subtitle": "場址效應能量聚焦 · 永康維冠大樓震度 7 級"
      },
      {
        "voice_text": "臺南地質多為嘉南平原鬆軟泥砂沉積，新化斷層與左鎮斷層周遭易發生土壤液化，具有顯著的長週期放大特性。",
        "location": "臺南全境俯瞰",
        "camera": { "lon": 120.37, "lat": 23.17, "depth": 25.0, "dist": 130, "tilt": 25 },
        "subtitle": "嘉南平原沉積層土壤液化與地質共振監測"
      }
    ]
  },
  "台東縣": {
    "badge": "M 6.8 (2022池上)",
    "desc": "2022年9月18日池上大地震（M 6.8），中央山脈斷層與縱谷縫合帶劇烈錯動，高寮大橋震斷、花東鐵路鐵軌嚴重變形扭曲。",
    "beats": [
      {
        "voice_text": "臺東縣近期最強烈地震為2022年9月18日下午發生的池上大地震，芮氏規模達6.8，深度僅7公里。",
        "location": "臺東縣池上鄉",
        "camera": { "lon": 121.19, "lat": 23.14, "depth": 7.0, "dist": 75, "tilt": 45 },
        "subtitle": "2022/09/18 規模 6.8 · 極淺層破裂 7.0 km"
      },
      {
        "voice_text": "震央位於板塊縫合帶的中央山脈斷層系統，劇烈走滑造成高寮大橋坍塌、崙天大橋斷裂與池上萬安磚窯震損。",
        "location": "花東縱谷斷層帶",
        "camera": { "lon": 121.25, "lat": 23.25, "depth": 15.0, "dist": 80, "tilt": 35 },
        "subtitle": "板塊縫合面逆衝破裂 · 花東鐵公路嚴重受創"
      },
      {
        "voice_text": "歷史上臺東海岸山脈與縱谷斷層長年承擔菲律賓海板塊每年約8公分西北推擠，能量釋放相當活躍。",
        "location": "臺東海岸山脈",
        "camera": { "lon": 121.3, "lat": 22.8, "depth": 25.0, "dist": 140, "tilt": 25 },
        "subtitle": "年推擠速率 8 cm · 板塊縫合邊界觀測"
      }
    ]
  },
  "宜蘭縣": {
    "badge": "M 6.8 (2002/331)",
    "desc": "2002年3月31日宜蘭外海規模6.8地震（331地震），深層隱沒帶震波引發台北101施工吊車墜落；沖繩海槽擴張地震頻仍。",
    "beats": [
      {
        "voice_text": "宜蘭縣外海常發生深層板塊隱沒地震，2002年331大地震規模達6.8，震源深度約13.8公里至更深處。",
        "location": "宜蘭外海海槽",
        "camera": { "lon": 122.0, "lat": 24.66, "depth": 40.0, "dist": 90, "tilt": 45 },
        "subtitle": "2002/03/31 規模 6.8 · 東北海域深層隱沒帶"
      },
      {
        "voice_text": "此處是沖繩海槽向西張裂與琉球隱沒帶的複雜交會處，深層震波向西傳入臺北盆地引發顯著共振，曾造成台北101吊車墜落意外。",
        "location": "蘭陽平原與龜山島",
        "camera": { "lon": 121.8, "lat": 24.75, "depth": 20.0, "dist": 80, "tilt": 35 },
        "subtitle": "沖繩海槽張裂構造 · 盆地長週期震波共振"
      }
    ]
  },
  "嘉義縣": {
    "badge": "M 7.1 (1906梅山)",
    "desc": "1906年梅山大地震規模7.1，梅山斷層右移地表錯動長達25公里，梅山民雄數千房屋倒塌；1999年亦有1022嘉義地震（M 6.4）。",
    "beats": [
      {
        "voice_text": "嘉義縣最具代表性的強震是1906年3月17日的梅山大地震，規模高達7.1，是臺灣近代地表破裂最顯著的強震之一。",
        "location": "嘉義縣梅山鄉",
        "camera": { "lon": 120.55, "lat": 23.57, "depth": 10.0, "dist": 75, "tilt": 45 },
        "subtitle": "1906/03/17 梅山大地震 · 規模 7.1 · 梅山斷層右移破裂"
      },
      {
        "voice_text": "梅山斷層產生長達25公里的地表破裂帶，伴隨劇烈噴砂與地裂，造成梅山與大林地區超過千人罹難。",
        "location": "梅山斷層帶",
        "camera": { "lon": 120.48, "lat": 23.55, "depth": 15.0, "dist": 70, "tilt": 35 },
        "subtitle": "斷層破裂帶長 25 km · 民房全毀達數千棟"
      }
    ]
  },
  "嘉義市": {
    "badge": "M 6.4 (1999嘉義)",
    "desc": "1999年10月22日嘉義大地震規模6.4，深度僅16.6公里，震央鄰近市區，多棟建物結構受損與引發局部火災。",
    "beats": [
      {
        "voice_text": "1999年10月22日，在921地震後一個月，嘉義市西側發生規模6.4強震，震源深度僅16.6公里。",
        "location": "嘉義市區西側",
        "camera": { "lon": 120.42, "lat": 23.52, "depth": 16.6, "dist": 70, "tilt": 40 },
        "subtitle": "1999/10/22 規模 6.4 · 震源深度 16.6 km"
      },
      {
        "voice_text": "由於震央極淺且鄰近都會密集區，市區震度達到6級，導致多處民宅塌陷與瓦斯外洩火災，突顯嘉南平原淺層地震的威脅。",
        "location": "嘉義市中心",
        "camera": { "lon": 120.45, "lat": 23.48, "depth": 10.0, "dist": 60, "tilt": 30 },
        "subtitle": "極淺層都會型地震 · 震度 6 級劇烈晃動"
      }
    ]
  },
  "台中市": {
    "badge": "M 7.1 (1935屯子腳)",
    "desc": "1935年新竹台中大地震（屯子腳斷層錯動重創后里豐原）及1999年921地震車籠埔斷層北段將石岡水壩生生撕裂抬升9公尺。",
    "beats": [
      {
        "voice_text": "臺中市歷史上受創最嚴重的震災包含1935年屯子腳大地震，以及1999年921地震車籠埔斷層往北撕裂。",
        "location": "臺中市石岡水壩",
        "camera": { "lon": 120.78, "lat": 24.28, "depth": 10.0, "dist": 70, "tilt": 45 },
        "subtitle": "車籠埔斷層北段撕裂 · 石岡水壩抬升 9.8 公尺"
      },
      {
        "voice_text": "車籠埔斷層在石岡壩產生將近10公尺垂直落差，大甲溪河床瞬間被截斷，東勢與新社山區多處道路被截斷坍塌。",
        "location": "臺中東勢與新社",
        "camera": { "lon": 120.83, "lat": 24.25, "depth": 12.0, "dist": 75, "tilt": 35 },
        "subtitle": "斷層崖橫跨大甲溪 · 地表落差近三層樓高"
      }
    ]
  },
  "苗栗縣": {
    "badge": "M 7.1 (1935獅潭)",
    "desc": "1935年4月21日新竹台中大地震（震央苗栗獅潭，規模7.1），獅潭斷層垂直錯動3公尺，龍騰斷橋即因此震斷裂，全台傷亡逾萬。",
    "beats": [
      {
        "voice_text": "苗栗縣歷史上最著名的大地震為1935年4月21日清晨發生的獅潭大地震，規模達到7.1。",
        "location": "苗栗縣獅潭鄉",
        "camera": { "lon": 120.88, "lat": 24.52, "depth": 10.0, "dist": 75, "tilt": 45 },
        "subtitle": "1935/04/21 規模 7.1 · 臺灣史上傷亡最重世紀大震"
      },
      {
        "voice_text": "獅潭斷層產生長達十餘公里的垂直斷層崖，三義魚藤坪鐵橋（即著名的龍騰斷橋）磚造拱橋在劇震中嚴重斷裂，留存至今成為歷史地標。",
        "location": "三義龍騰斷橋",
        "camera": { "lon": 120.77, "lat": 24.36, "depth": 8.0, "dist": 60, "tilt": 35 },
        "subtitle": "獅潭斷層垂直錯動 3m · 魚藤坪龍騰斷橋斷裂遺址"
      }
    ]
  },
  "高雄市": {
    "badge": "M 6.6 (2016美濃)",
    "desc": "2016年2月6日凌晨美濃地震規模6.6，深度14.6公里，旗山斷層周遭左移破裂，震波傳遞造成高雄與台南嚴重震動受損。",
    "beats": [
      {
        "voice_text": "高雄市境內近期最顯著的強震是2016年2月6日凌晨3點57分的美濃地震，芮氏規模達到6.6。",
        "location": "高雄市美濃區",
        "camera": { "lon": 120.54, "lat": 22.92, "depth": 14.6, "dist": 75, "tilt": 40 },
        "subtitle": "2016/02/06 規模 6.6 · 震源深度 14.6 km"
      },
      {
        "voice_text": "震央鄰近旗山斷層帶，破裂面呈西北西走向，能量朝西北方釋放，造成高屏地區強烈晃動與建物災情。",
        "location": "高雄旗山斷層",
        "camera": { "lon": 120.48, "lat": 22.88, "depth": 15.0, "dist": 80, "tilt": 30 },
        "subtitle": "左移斷層分量破裂 · 震波朝西北傳遞"
      }
    ]
  },
  "屏東縣": {
    "badge": "M 7.0 (2006恆春雙震)",
    "desc": "2006年12月26日恆春外海發生兩起規模7.0強震，深度約50公里，震斷8條國際海底光纜，使東亞各國對外網際網路大中斷。",
    "beats": [
      {
        "voice_text": "屏東縣歷史上最具國際影響力的強震是2006年12月26日晚間發生的恆春外海雙震，芮氏規模高達7.0。",
        "location": "恆春西南外海",
        "camera": { "lon": 120.42, "lat": 21.97, "depth": 50.2, "dist": 90, "tilt": 45 },
        "subtitle": "2006/12/26 規模 7.0 雙震 · 呂宋隱沒帶交界"
      },
      {
        "voice_text": "強震引發海床大規模濁流坍滑，生生扯斷了行經呂宋海峽的8條主要國際海底通訊電纜，重創東亞各國網路與跨國金融連線。",
        "location": "巴士海峽海底電纜路徑",
        "camera": { "lon": 120.6, "lat": 21.7, "depth": 40.0, "dist": 110, "tilt": 30 },
        "subtitle": "8條國際海纜斷裂 · 東亞網際網路通訊癱瘓數週"
      }
    ]
  },
  "台北市": {
    "badge": "M 7.0+ (1694康熙大震)",
    "desc": "1694年康熙台北大地震山腳斷層陷落，台北盆地沉降積水成「康熙台北湖」；盆地沉積層對遠震具顯著共振放大特性。",
    "beats": [
      {
        "voice_text": "臺北市歷史上最具地質規模的是1694年康熙臺北大地震，估計規模超過7.0，為山腳斷層陷落所誘發。",
        "location": "臺北盆地關渡隘口",
        "camera": { "lon": 121.47, "lat": 25.12, "depth": 10.0, "dist": 75, "tilt": 40 },
        "subtitle": "1694 康熙臺北大地震 (M 7.0+) · 山腳斷層正斷層錯動"
      },
      {
        "voice_text": "盆地地盤大幅下陷數公尺，淡水河與新店溪水灌入形成廣達數十平方公里的康熙臺北湖，呈現正斷層構造的劇烈地表變化。",
        "location": "臺北盆地中心",
        "camera": { "lon": 121.54, "lat": 25.04, "depth": 15.0, "dist": 80, "tilt": 30 },
        "subtitle": "盆地沉積層厚達數百公尺 · 遠震長週期波共振放大效應"
      }
    ]
  },
  "新北市": {
    "badge": "山腳斷層破裂帶",
    "desc": "山腳斷層沿五股、泰山延伸至金山外海，為北部關鍵活動斷層；1867年基隆海嘯與1986年花蓮遠震均在低窪沉積層引發災情。",
    "beats": [
      {
        "voice_text": "新北市地質最重要的斷層是山腳斷層，從五股、泰山綿延至北海岸金山，向外海延伸數十公里。",
        "location": "新北市五股泰山山腳斷層",
        "camera": { "lon": 121.42, "lat": 25.07, "depth": 10.0, "dist": 75, "tilt": 40 },
        "subtitle": "山腳斷層構造線 · 新北盆地西緣正斷層"
      },
      {
        "voice_text": "新北市幅員廣闊，沿海與河谷沖積地層鬆軟，當東部外海發生強震時，長週期地震波常在都會區引發明顯大樓搖擺晃動。",
        "location": "新北淡水河谷全貌",
        "camera": { "lon": 121.66, "lat": 25.06, "depth": 25.0, "dist": 130, "tilt": 25 },
        "subtitle": "長週期震波共振觀測 · 都會耐震防護關鍵"
      }
    ]
  },
  "桃園縣": {
    "badge": "全臺地塊最穩固",
    "desc": "桃園台地由厚實紅土礫石層構成，地質安定且無活動斷層穿過，歷史地震發生次數全台最低，受地震災害影響最小。",
    "beats": [
      {
        "voice_text": "桃園市是臺灣地質條件最穩定的縣市之一，基盤由厚實堅硬的古老紅土礫石層所構成，境內幾乎沒有活動斷層穿過。",
        "location": "桃園古老紅土台地",
        "camera": { "lon": 121.26, "lat": 24.92, "depth": 25.0, "dist": 90, "tilt": 35 },
        "subtitle": "全臺地震活動最安定區域 · 堅硬礫石台地基盤"
      },
      {
        "voice_text": "在過去百年地震紀錄中，桃園自主發生的中大型地震極為罕見，是臺灣極少數未曾發生災難性本土大震的幸運寶地。",
        "location": "桃園全境俯瞰",
        "camera": { "lon": 121.2, "lat": 24.95, "depth": 35.0, "dist": 130, "tilt": 25 },
        "subtitle": "無活動斷層貫穿 · 災害風險相對全臺最低"
      }
    ]
  },
  "新竹市": {
    "badge": "新城斷層帶",
    "desc": "新竹市東南側鄰近新城斷層，1935年新竹台中大地震曾在香山地區造成地裂與噴沙現象；竹科為高耐震防護示範區。",
    "beats": [
      {
        "voice_text": "新竹市境內及周邊主要受新城斷層與竹東地震帶影響，1935年新竹台中大地震時曾引發劇烈震動與局部地裂。",
        "location": "新竹新城斷層帶",
        "camera": { "lon": 120.95, "lat": 24.78, "depth": 10.0, "dist": 70, "tilt": 40 },
        "subtitle": "新城斷層逆移構造 · 鄰近新竹科學園區"
      },
      {
        "voice_text": "由於新竹科學園區為全球半導體製造樞紐，所有精密晶圓廠與高科技設施皆具備最高等級的防震與實時避震阻尼系統。",
        "location": "新竹科學園區",
        "camera": { "lon": 121.0, "lat": 24.77, "depth": 15.0, "dist": 60, "tilt": 30 },
        "subtitle": "全球半導體重鎮 · 頂級防震與自動斷電阻尼系統"
      }
    ]
  },
  "新竹縣": {
    "badge": "M 7.1 (1935震災)",
    "desc": "1935年新竹台中大地震造成峨眉、關西、竹東一帶房屋傾倒；境內有新城斷層、湖口斷層與大坪地塹地質構造。",
    "beats": [
      {
        "voice_text": "新竹縣在1935年新竹台中大地震中受創顯著，峨眉、竹東與關西一帶許多古老土埆造聚落因強烈震動而損毀坍塌。",
        "location": "新竹縣峨眉與竹東",
        "camera": { "lon": 121.13, "lat": 24.71, "depth": 12.0, "dist": 80, "tilt": 40 },
        "subtitle": "1935年大震受災區 · 丘陵地階地地裂"
      },
      {
        "voice_text": "新竹縣地形由平原向雪山山脈西北側升高，境內有湖口斷層與大坪地塹，地質上受到向西北逆衝的擠壓構造推動。",
        "location": "新竹雪山山脈前緣",
        "camera": { "lon": 121.2, "lat": 24.6, "depth": 25.0, "dist": 120, "tilt": 30 },
        "subtitle": "湖口斷層與褶皺逆衝帶構造"
      }
    ]
  },
  "彰化縣": {
    "badge": "M 7.0+ (1848鹿港)",
    "desc": "1848年彰化大地震（鹿港大地震），彰化活動斷層錯動重創鹿港古城；921地震時員林地區亦發生大規模土壤液化湧砂現象。",
    "beats": [
      {
        "voice_text": "彰化縣歷史上最嚴重的震災為1848年發生的彰化大地震，又稱鹿港大地震，估計規模超過7.0。",
        "location": "彰化鹿港龍山寺",
        "camera": { "lon": 120.43, "lat": 24.05, "depth": 10.0, "dist": 70, "tilt": 40 },
        "subtitle": "1848 彰化鹿港大地震 (M 7.0+) · 古城重創"
      },
      {
        "voice_text": "彰化斷層沿著八卦台地西側分布，1999年921地震時，強烈震波更在員林地區誘發嚴重的土壤液化噴砂，多棟房屋沉陷傾斜。",
        "location": "八卦台地與員林",
        "camera": { "lon": 120.57, "lat": 23.96, "depth": 15.0, "dist": 75, "tilt": 30 },
        "subtitle": "彰化活動斷層 · 八卦山台地西緣與員林土壤液化"
      }
    ]
  },
  "雲林縣": {
    "badge": "草嶺大走山 (921)",
    "desc": "1999年921地震誘發古坑草嶺堀沓山順向坡大規模崩塌，滑動土石量達1.2億立方公尺，阻斷清水溪形成著名天然堰塞湖「草嶺潭」。",
    "beats": [
      {
        "voice_text": "雲林縣歷史上最震撼的地質事件，是1999年921大地震誘發古坑鄉草嶺地區發生的世紀大走山。",
        "location": "雲林古坑草嶺潭遺址",
        "camera": { "lon": 120.69, "lat": 23.58, "depth": 10.0, "dist": 70, "tilt": 45 },
        "subtitle": "1999 921大地震 · 草嶺順向坡世紀大崩塌"
      },
      {
        "voice_text": "高達1.2億立方公尺的岩層瞬間順坡滑移衝入清水溪谷，築起天然壩體形成草嶺潭，是世界級的地震邊坡崩塌地質教材。",
        "location": "清水溪堰塞湖河谷",
        "camera": { "lon": 120.65, "lat": 23.6, "depth": 15.0, "dist": 80, "tilt": 35 },
        "subtitle": "崩塌土石量 1.2 億立方公尺 · 清水溪堰塞湖"
      }
    ]
  },
  "基隆市": {
    "badge": "1867 基隆大海嘯",
    "desc": "1867年12月18日基隆外海大地震（規模估計7.0），誘發高達數公尺的海嘯狂濤淹入基隆港市街，為臺灣歷史上最著名海嘯紀錄。",
    "beats": [
      {
        "voice_text": "基隆市歷史上最著名的震災為1867年12月18日發生的基隆外海大地震，估計規模達7.0，並誘發了罕見的毀滅性海嘯。",
        "location": "基隆港外海海嘯源",
        "camera": { "lon": 121.78, "lat": 25.18, "depth": 15.0, "dist": 75, "tilt": 45 },
        "subtitle": "1867/12/18 基隆大地震海嘯 · 規模 7.0 · 臺灣罕見海嘯浩劫"
      },
      {
        "voice_text": "當時海水迅速倒退露出港底岩礁，隨後數丈巨浪排山倒海灌入基隆市區，房屋多被沖毀，數百人溺水遇難。",
        "location": "基隆和平島與市港",
        "camera": { "lon": 121.75, "lat": 25.14, "depth": 12.0, "dist": 65, "tilt": 35 },
        "subtitle": "海水倒退後巨浪反撲 · 和平島與基隆港市街全浸水"
      }
    ]
  },
  "澎湖縣": {
    "badge": "地質構造安定",
    "desc": "澎湖列島為厚實玄武岩火山熔岩台地，地殼堅硬厚實無活動斷層穿過，本土極少強震，主要感受台灣海峽深部震波與遠震波及。",
    "beats": [
      {
        "voice_text": "澎湖縣位於臺灣海峽海盆西部，由多次火山噴發凝固形成的厚實柱狀玄武岩台地所組成，地殼構造非常穩定。",
        "location": "澎湖玄武岩火山台地",
        "camera": { "lon": 119.59, "lat": 23.58, "depth": 15.0, "dist": 80, "tilt": 35 },
        "subtitle": "火山柱狀玄武岩基盤 · 地質構造極為厚實安定"
      },
      {
        "voice_text": "澎湖境內沒有任何活動斷層，歷史上極少本土強震，偶爾感受到的晃動多來自臺灣本島或臺灣海峽南部的遠震波動。",
        "location": "澎湖群島與臺灣海峽",
        "camera": { "lon": 119.6, "lat": 23.5, "depth": 25.0, "dist": 120, "tilt": 25 },
        "subtitle": "本土無活動斷層 · 僅感受海峽南部與本島遠震波動"
      }
    ]
  }
}

html_card = """
      <!-- County Historical Disaster Info & Voice Guide Card -->
      <div id="county-history-card" style="display: none; background: rgba(15, 23, 42, 0.95); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 8px; padding: 12px; margin-top: 10px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <span style="font-weight: 700; color: #f59e0b; font-size: 13px;" id="chc-title">📍 縣市歷史強震</span>
          <span style="font-size: 10px; background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); padding: 2px 6px; border-radius: 4px; font-weight: 600;" id="chc-badge">歷史最大</span>
        </div>
        <div style="font-size: 11px; color: #cbd5e1; line-height: 1.55; margin-bottom: 10px;" id="chc-desc">
          點擊下方按鈕，AI 語音助理將帶您飛越該縣市震央並深入解說！
        </div>
        <button id="btn-narrate-county" onclick="narrateCurrentCounty()" style="width: 100%; background: linear-gradient(135deg, #f59e0b, #d97706); color: #0f172a; border: none; font-weight: 700; font-size: 12px; padding: 8px 12px; border-radius: 6px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px; transition: all 0.2s; box-shadow: 0 2px 8px rgba(245, 158, 11, 0.3);">
          <span>🔊 聆聽 AI 語音解說此縣市歷史最大地震</span>
        </button>
        <label style="display: flex; align-items: center; gap: 6px; margin-top: 8px; font-size: 11px; color: #94a3b8; cursor: pointer;">
          <input type="checkbox" id="chk-auto-narrate" style="accent-color: #f59e0b; cursor: pointer;">
          <span>切換縣市時自動播放語音導覽</span>
        </label>
      </div>"""

js_code = f"""
    // 20 縣市歷史最大地震與地質影響知識庫 (全台完整版)
    const COUNTY_HISTORICAL_INFO = {json.dumps(counties_info, ensure_ascii=False, indent=4)};

    function updateCountyHistoryCard(county) {{
      const card = document.getElementById('county-history-card');
      if (!card) return;
      if (county === 'all' || !COUNTY_HISTORICAL_INFO[county]) {{
        card.style.display = 'none';
        return;
      }}
      const info = COUNTY_HISTORICAL_INFO[county];
      card.style.display = 'block';
      document.getElementById('chc-title').innerText = '📍 ' + county + ' 歷史強震';
      document.getElementById('chc-badge').innerText = info.badge || '歷史最大';
      document.getElementById('chc-desc').innerText = info.desc;
    }}

    function narrateCurrentCounty() {{
      const county = document.getElementById('sel-county').value;
      if (!county || county === 'all') return;
      const promptQuery = `請解說${{county}}歷史上發生過最大的地震與災情地質影響？`;
      document.getElementById('input-query').value = promptQuery;
      submitQuery(promptQuery);
    }}
"""

def patch_file(filepath):
    print(f"Patching {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Insert html_card after </select> in the county control group
    target_select = '</select>\n    </div>\n\n    <!-- Year Filter -->'
    replacement_select = f'</select>{html_card}\n    </div>\n\n    <!-- Year Filter -->'
    if target_select in content:
        content = content.replace(target_select, replacement_select)
        print("  -> Inserted HTML card")
    else:
        print("  -> Warning: target_select not found!")

    # 2. Insert js_code before `// 8. County Change & Presets`
    target_county_fn = '// 8. County Change & Presets'
    if target_county_fn in content:
        content = content.replace(target_county_fn, js_code + "\n    " + target_county_fn)
        print("  -> Inserted JS code and functions")
    else:
        print("  -> Warning: target_county_fn not found!")

    # 3. Update onCountyChange() to invoke updateCountyHistoryCard and auto-narrate
    old_occ = """    function onCountyChange() {
      const county = document.getElementById('sel-county').value;
      for (const name in countyLinesMap) {
        const isSelected = (county === name);
        countyLinesMap[name].forEach(l => {
          if (county === 'all') {
            l.material.color.setHex(0x38bdf8);
            l.material.opacity = 0.8;
          } else if (isSelected) {
            l.material.color.setHex(0xf59e0b);
            l.material.opacity = 1.0;
          } else {
            l.material.color.setHex(0x1e293b);
            l.material.opacity = 0.25;
          }
        });
      }

      if (county !== 'all' && COUNTY_DATA[county]) {
        const c = COUNTY_DATA[county];
        const targetPos = geoTo3D(c.center_lon, c.center_lat, 25);
        animateCameraTo(targetPos.x, targetPos.y, targetPos.z, 110);
      } else if (county === 'all') {
        animateCameraTo(0, -30, 0, 220);
      }
      buildEarthquakes();
    }"""

    new_occ = """    function onCountyChange() {
      const county = document.getElementById('sel-county').value;
      for (const name in countyLinesMap) {
        const isSelected = (county === name);
        countyLinesMap[name].forEach(l => {
          if (county === 'all') {
            l.material.color.setHex(0x38bdf8);
            l.material.opacity = 0.8;
          } else if (isSelected) {
            l.material.color.setHex(0xf59e0b);
            l.material.opacity = 1.0;
          } else {
            l.material.color.setHex(0x1e293b);
            l.material.opacity = 0.25;
          }
        });
      }

      updateCountyHistoryCard(county);

      if (county !== 'all' && COUNTY_DATA[county]) {
        const c = COUNTY_DATA[county];
        const targetPos = geoTo3D(c.center_lon, c.center_lat, 25);
        animateCameraTo(targetPos.x, targetPos.y, targetPos.z, 110);
        if (document.getElementById('chk-auto-narrate') && document.getElementById('chk-auto-narrate').checked) {
          narrateCurrentCounty();
        }
      } else if (county === 'all') {
        animateCameraTo(0, -30, 0, 220);
      }
      buildEarthquakes();
    }"""

    if old_occ in content:
        content = content.replace(old_occ, new_occ)
        print("  -> Updated onCountyChange()")
    else:
        print("  -> Warning: old_occ not found!")

    # 4. Update getLocalAnswer(q) to check COUNTY_HISTORICAL_INFO
    target_local_ans = "function getLocalAnswer(q) {\n      const query = q.toLowerCase();"
    new_local_ans = """function getLocalAnswer(q) {
      const query = q.toLowerCase();

      // Check if query matches any county
      for (const cName in COUNTY_HISTORICAL_INFO) {
        const shortName = cName.replace(/[縣市]/g, '');
        if (query.includes(cName) || query.includes(shortName)) {
          const info = COUNTY_HISTORICAL_INFO[cName];
          return {
            topic: cName + '歷史強震與地質影響',
            beats: info.beats
          };
        }
      }"""

    if target_local_ans in content:
        content = content.replace(target_local_ans, new_local_ans)
        print("  -> Updated getLocalAnswer with 20-county lookup")
    else:
        print("  -> Warning: target_local_ans not found!")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  -> Done.")

patch_file("/Users/chenchunchih/Desktop/taiwan-earthquake-3d/index.html")
patch_file("/Users/chenchunchih/Desktop/taiwan-earthquake-3d/taiwan_earthquake_3d.html")
