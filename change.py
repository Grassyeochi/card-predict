import os

# 저장할 경로 (현재 디렉토리에 저장)
output_dir = "."

# 카드 숫자 변환 함수
def get_card_value(num):
    if num == 11:
        return "J"
    elif num == 12:
        return "Q"
    elif num == 13:
        return "K"
    return str(num)

# 52장의 카드에 대한 HTML 파일 생성
for i in range(52):
    filename = f"{i:02}.html"  # 00 ~ 51.html 형식

    # suit 및 value 결정
    if 0 <= i <= 12:  # ♠ (스페이드)
        suit = "♠"
        color = "black"
        value = get_card_value(i + 1)
    elif 13 <= i <= 25:  # ♣ (클럽)
        suit = "♣"
        color = "black"
        value = get_card_value(i - 12)
    elif 26 <= i <= 38:  # ♦ (다이아몬드)
        suit = "♦"
        color = "red"
        value = get_card_value(i - 25)
    else:  # 39 <= i <= 51 (♥ 하트)
        suit = "♥"
        color = "red"
        value = get_card_value(i - 38)

    # HTML 코드 생성
    html_content = f"""<!DOCTYPE HTML>
<html>

<head>
  <title>{i}</title>
  <meta charset="utf-8">
  <meta property="og:url" content="grassyeochi.github.io/card-predict/{i:02}.html" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="카드 확인" />
  <meta property="og:description" content="카드 확인용 페이지 입니다." />
  <meta property="og:image" content="thumnail.jpg" />
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <style>
    #cardButton {{
      position: absolute;
      top: 5%;
      left: 50%;
      transform: translateX(-50%);
      width: 150px;
      height: 60px;
      font-size: 20pt;
    }}

    /* 중앙 정렬을 위한 스타일 */
    .center-container {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
    }}

    .button {{
      width: 150px;
      height: 60px;
      font-size: 20pt;
      margin: 10px;
    }}

    .card-result {{
      display: none; /* 초기에 숨김 */
      font-size: 300%;
      text-align: center;
      margin-top: 300px;
    }}

    /* 캡처 버튼 숨김 */
    #captureBtn {{
      display: none;
    }}
  </style>
</head>

<body>
    <input type="button" id="cardButton" value="이 카드는" onclick="myFunction()" />

    <br>
    <!-- 카드 결과 표시 -->
    <div id="cardDisplay" class="card-result">
      <span id="value"></span>
      <span id="suit" style="color:{color};"></span>
      <span id="comment"></span>
    </div>

    <div class="center-container">
      <input type="button" id="captureBtn" class="button" value="화면 캡처" onclick="captureScreen()" />
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script>
      function myFunction() {{
        document.getElementById("value").innerHTML = "{value}";
        document.getElementById("suit").innerHTML = "{suit}";
        document.getElementById("comment").innerHTML = "입니다!";
        document.getElementById("cardDisplay").style.display = "block";
        document.getElementById("captureBtn").style.display = "block";
      }}

      function captureScreen() {{
        html2canvas(document.body).then(canvas => {{
          let link = document.createElement("a");
          link.href = canvas.toDataURL("image/png");
          link.download = "screenshot.png";
          link.click();
        }});
      }}
    </script>

</body>
</html>"""

    # 파일 저장
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as file:
        file.write(html_content)

print("✅ 모든 HTML 파일이 성공적으로 생성되었습니다!")
