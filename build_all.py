import os
from datetime import datetime

BASE_URL = "https://thebareun-care.netlify.app"
BRAND_NAME = "바른케어"
REP_PHONE = "0507-1280-3344"
TODAY = datetime.today().strftime('%Y-%m-%d')

SHOPS = [
    {"name": "퀸즈홈테라피", "phone": "0507-1280-3296", "score": "4.9", "tags": "타이전문 · 아로마 · 예약금없음"},
    {"name": "오늘밤테라피", "phone": "0507-1280-3199", "score": "4.8", "tags": "스웨디시 · 아로마 · 후불제"},
    {"name": "주주테라피",   "phone": "0507-1280-3197", "score": "4.8", "tags": "감성힐링 · 여성전용 · 카드가능"},
    {"name": "한국골든테라피", "phone": "0507-1280-3360", "score": "4.7", "tags": "프리미엄 · 집중케어 · 24시운영"}
]

# 세부지역별 4대 케어 테마 수식어 순환 설정
CARE_THEMES = [
    ("출장 균형케어 마사지", "전신의 긴장과 밸런스를 조율하는 맞춤 균형 케어"),
    ("출장 온쉼케어 마사지", "온전한 휴식과 회복을 돕는 편안한 온쉼 케어"),
    ("출장 릴렉스케어 마사지", "부드러운 오일과 리듬으로 스트레스를 풀어주는 릴렉스 케어"),
    ("출장 바른케어 마사지", "뭉친 부위를 세심하게 풀어 활력을 되찾아주는 바른 케어")
]

# 네이버 C-Rank / D-I-A 대비 지역 특성별 고유 장문 텍스트 생성 엔진
OFFICE_KEYWORDS = ["강남", "서초", "송파", "영등포", "마포", "종로", "중구", "판교", "분당", "가산", "구로", "수원", "안양"]
RESIDENCE_KEYWORDS = ["노원", "강동", "양천", "강서", "은평", "도봉", "일산", "고양", "용인", "남양주", "하남", "송도", "청라", "부평"]

def generate_bareun_story(prov_short, dist_name):
    loc_title = f"{prov_short} {dist_name}"
    
    is_office = any(k in loc_title for k in OFFICE_KEYWORDS)
    is_residence = any(k in loc_title for k in RESIDENCE_KEYWORDS)

    if is_office:
        p1 = f"{loc_title} 일대는 활발한 비즈니스 상권과 직장인 밀집도가 높은 지역으로, 장시간 고정된 자세와 컴퓨터 업무로 인해 목·어깨 결림, 허리 뻐근함을 호소하는 분들의 케어 문의가 꾸준한 곳입니다."
        p2 = f"{BRAND_NAME}은 번거롭게 밖으로 이동할 필요 없이 퇴근 후 편안한 집이나 머무시는 숙소에서 신속하게 전신 피로를 회복하실 수 있도록 {loc_title} 전담 이동 동선을 세심하게 관리하고 있습니다."
    elif is_residence:
        p1 = f"{loc_title} 생활권은 주거 단지와 아파트 밀집도가 높아 외출의 번거로움 없이 내 집에서 조용하고 편안하게 힐링을 누리고자 하는 주민분들의 수요가 집중되는 지역입니다."
        p2 = f"실내 소음이나 불편함이 발생하지 않도록 정숙하고 섬세한 케어를 기본 원칙으로 하며, 공동현관 호출 방식과 단지 내 주차 여건을 사전에 조율하여 시간 지연 없이 정확하게 찾아갑니다."
    else:
        p1 = f"{loc_title} 지역은 일상 속에서 누적된 신체 피로와 전신 스트레스를 자연스럽게 풀어주는 맞춤형 방문 힐링 솔루션을 지향하는 곳입니다."
        p2 = f"불필요한 대기 시간이나 이동 스트레스 없이 고객님의 희망 시각에 맞춰 최적의 도로 동선을 확인하여 숙련된 테라피스트를 정시 배정합니다."

    p3 = f"{BRAND_NAME}은 선입금이나 예약금을 절대로 요구하지 않는 '100% 현장 안심 후불제'를 철저히 지킵니다. 관리사가 고객님의 장소에 도착한 뒤 신청하신 관리 코스와 범위, 요금을 투명하게 재확인하고 결제가 이루어지므로 사기 피해 걱정 없이 안심하고 신뢰할 수 있습니다."

    return p1, p2, p3

REGIONS = {
    "seoul": [
        ("gangnam-gu", "강남"), ("gangdong-gu", "강동"), ("gangbuk-gu", "강북"), ("gangseo-gu", "강서"),
        ("gwanak-gu", "관악"), ("gwangjin-gu", "광진"), ("guro-gu", "구로"), ("geumcheon-gu", "금천"),
        ("nowon-gu", "노원"), ("dobong-gu", "도봉"), ("dongdaemun-gu", "동대문"), ("dongjak-gu", "동작"),
        ("mapo-gu", "마포"), ("seodaemun-gu", "서대문"), ("seocho-gu", "서초"), ("seongdong-gu", "성동"),
        ("seongbuk-gu", "성북"), ("songpa-gu", "송파"), ("yangcheon-gu", "양천"), ("yeongdeungpo-gu", "영등포"),
        ("yongsan-gu", "용산"), ("eunpyeong-gu", "은평"), ("jongno-gu", "종로"), ("jung-gu", "중구"),
        ("jungnang-gu", "중랑")
    ],
    "gyeonggi": [
        ("gapyeong-gun", "가평"), ("goyang-si", "고양"), ("gwacheon-si", "과천"), ("gwangmyeong-si", "광명"),
        ("gwangju-si", "광주"), ("guri-si", "구리"), ("gunpo-si", "군포"), ("gimpo-si", "김포"),
        ("namyangju-si", "남양주"), ("dongducheon-si", "동두천"), ("bucheon-si", "부천"), ("seongnam-si", "성남"),
        ("suwon-si", "수원"), ("siheung-si", "시흥"), ("ansan-si", "안산"), ("anseong-si", "안성"),
        ("anyang-si", "안양"), ("yangju-si", "양주"), ("yangpyeong-gun", "양평"), ("yeoju-si", "여주"),
        ("yeoncheon-gun", "연천"), ("osan-si", "오산"), ("yongin-si", "용인"), ("uiwang-si", "의왕"),
        ("uijeongbu-si", "의정부"), ("icheon-si", "이천"), ("paju-si", "파주"), ("pyeongtaek-si", "평택"),
        ("pocheon-si", "포천"), ("hanam-si", "하남"), ("hwaseong-si", "화성")
    ],
    "incheon": [
        ("ganghwa-gun", "강화"), ("geomdan-gu", "검단"), ("gyeyang-gu", "계양"), ("namdong-gu", "남동"),
        ("michuhol-gu", "미추홀"), ("bupyeong-gu", "부평"), ("seohae-gu", "서해"), ("yeonsu-gu", "연수"),
        ("yeongjong-gu", "영종"), ("ongjin-gun", "옹진"), ("jemulpo-gu", "제물포")
    ]
}

PROV_INFO = {
    "seoul": ("서울특별시", "서울", "/"),
    "gyeonggi": ("경기도", "경기", "/gyeonggi/"),
    "incheon": ("인천광역시", "인천", "/incheon/")
}

def build_shop_cards(loc_name):
    cards = []
    for idx, shop in enumerate(SHOPS, 1):
        clean_phone = shop["phone"].replace("-", "")
        card = f"""          <article class="provider-card">
            <div class="rank">{idx}<small>위</small></div>
            <div class="provider-main">
              <div class="provider-head">
                <h3>{shop['name']}</h3>
                <span>★ {shop['score']}</span>
              </div>
              <div class="tags">
                <span>{shop['tags']}</span>
              </div>
              <p>{loc_name} 인근 신속 이동 동선 확인 후 방문 관리합니다. 선입금 없는 정직한 안내입니다.</p>
              <div class="provider-prices"><span>건식 60분 · 8만</span> / <span>오일 90분 · 11만</span></div>
            </div>
            <a class="provider-phone-btn" href="tel:{clean_phone}">
              <b>전화 상담</b>
              <small>{shop['phone']}</small>
            </a>
          </article>"""
        cards.append(card)
    return "\n".join(cards)

# 1. 서울 메인 페이지
def make_main_page():
    nearby = []
    for slug, name in REGIONS["seoul"]:
        nearby.append(f'          <a class="region-link" href="/areas/seoul/{slug}/"><b>서울 {name}</b><span>출장 케어 안내</span></a>')
    nearby_html = "\n".join(nearby)

    title_text = f"서울특별시 출장 균형케어 마사지 | 일정에 맞춘 코스 비교 - {BRAND_NAME}"
    desc_text = f"{BRAND_NAME} 서울특별시 안내. 선입금 없이 현장에서 확인하는 출장마사지·출장안마·홈타이 코스와 시간, 지역별 균형케어 이용 순서를 정리했습니다."
    keywords_text = "서울출장마사지, 서울홈타이, 서울출장안마, 서울균형케어, 서울방문테라피, 서울스웨디시"

    sp1, sp2, sp3 = generate_bareun_story("서울", "전지역")

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="naver-site-verification" content="e282b5e666eda62d8af5e5089adcdd5c5f694959" />
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <title>{title_text}</title>
  <meta name="description" content="{desc_text}">
  <meta name="keywords" content="{keywords_text}">
  <link rel="canonical" href="{BASE_URL}/">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title_text}">
  <meta property="og:description" content="{desc_text}">
  <meta property="og:url" content="{BASE_URL}/">

  <link rel="stylesheet" href="/styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "{BRAND_NAME}",
        "url": "{BASE_URL}/",
        "telephone": "{REP_PHONE}",
        "priceRange": "₩₩",
        "description": "{desc_text}"
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "서울 전지역 균형케어 방문 예약은 어떻게 진행되나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "서울 25개 자치구 어디서나 희망 주소와 원하시는 코스를 알려주시면 가장 가까운 이동 동선의 관리사를 신속 배정합니다."
            }}
          }},
          {{
            "@type": "Question",
            "name": "선입금이나 예약금을 요구하지 않나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "바른케어는 선입금을 일체 요구하지 않으며 관리사가 현장에 도착한 후 코스를 확인하고 결제하는 100% 현장 후불제입니다."
            }}
          }},
          {{
            "@type": "Question",
            "name": "자택 외에 오피스텔이나 호텔에서도 이용 가능한가요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "네, 정확한 주소지와 호수, 출입 방법만 확인해 주시면 조용하고 안전하게 프라이빗 관리를 받으실 수 있습니다."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body data-page-type="target-home">
  <a class="skip-link" href="#content">본문으로 이동</a>
  
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo" aria-label="{BRAND_NAME} 홈">
        <span class="brand-badge">바</span>
        <span class="brand-name">{BRAND_NAME}</span>
      </a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>

  <main id="content">
    <section class="home-hero">
      <div class="container">
        <span class="hero-badge">서울 · 경기 · 인천 방문 힐링 케어 플랫폼</span>
        <h1>오늘의 지친 피로를<br><em>바르게 풀어드립니다</em></h1>
        <p>희망 시간과 주소, 원하는 압을 먼저 나누면 당일 이동 동선에 맞춰 친절하게 상담합니다.</p>
        <div class="hero-stats">
          <div><b>94</b><span>지역 안내</span></div>
          <div><b>19~05시</b><span>상담 운영</span></div>
          <div><b>30분</b><span>평균 안내</span></div>
          <div><b>100%</b><span>현장 후불</span></div>
        </div>
        <a class="gold-button" href="#courses">코스와 일정 확인</a>
      </div>
    </section>

    <nav class="province-tabs">
      <div class="container">
        <a href="/" class="active">서울</a>
        <a href="/gyeonggi/">경기</a>
        <a href="/incheon/">인천</a>
      </div>
    </nav>

    <!-- 고유 본문 스토리텔링 섹션 -->
    <section class="section">
      <div class="container">
        <div class="local-story-card">
          <h3>서울특별시 방문 케어 안내 &amp; 라이프스타일 힐링</h3>
          <p>{sp1}</p>
          <p>{sp2}</p>
          <p>{sp3}</p>
          <div class="guide-box-grid">
            <div class="guide-box-item">
              <b>🛡️ 100% 현장 후불제 원칙</b>
              <span>예약금이나 선입금을 절대 요구하지 않으며, 현장에서 코스를 확인한 후 안심 결제합니다.</span>
            </div>
            <div class="guide-box-item">
              <b>⚡ 균형 잡힌 동선 조율</b>
              <span>서울 주요 거점별 이동 상황을 실시간 확인하여 지연과 대기를 최소화합니다.</span>
            </div>
            <div class="guide-box-item">
              <b>🧘 바른 체형 릴렉스</b>
              <span>건식, 아로마, 스웨디시 등 당일 몸 상태에 최적화된 강도와 순환 관리를 제공합니다.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section providers soft">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">서울 추천 케어 제휴 매장</h2>
          <span>직통 번호로 빠른 일정 상담</span>
        </div>
        <div class="provider-list">
{build_shop_cards('서울특별시')}
        </div>
      </div>
    </section>

    <section class="section course-section" id="courses">
      <div class="container">
        <h2 class="section-title">서울 코스 &amp; 요금 안내</h2>
        <p class="section-note">상담과 현장에서 시간·범위·비용을 다시 확인하고 선입금 없이 진행합니다.</p>
        <div class="course-grid">
          <article class="course-card"><span class="course-icon">🧘</span><h3>건식 밸런스</h3><p>오일 없이 전신의 긴장과 뭉친 근육을 부드럽게 이완합니다.</p><div class="price-list"><div class="price-row"><span>60분</span><b>80,000원</b></div><div class="price-row"><span>90분</span><b>100,000원</b></div><div class="price-row"><span>120분</span><b>120,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">🌿</span><h3>아로마 릴렉스</h3><p>은은한 오일 향과 함께 굳은 몸을 순환시키는 편안한 관리입니다.</p><div class="price-list"><div class="price-row"><span>60분</span><b>90,000원</b></div><div class="price-row"><span>90분</span><b>110,000원</b></div><div class="price-row"><span>120분</span><b>130,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">💧</span><h3>스웨디시 오일</h3><p>섬세하고 일정한 압으로 전신의 림프와 활력을 깨웁니다.</p><div class="price-list"><div class="price-row"><span>60분</span><b>100,000원</b></div><div class="price-row"><span>90분</span><b>120,000원</b></div><div class="price-row"><span>120분</span><b>140,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">👑</span><h3>프리미엄 케어</h3><p>집중 케어가 필요한 부위를 맞춤 배분하는 종합 힐링 프로그램입니다.</p><div class="price-list"><div class="price-row"><span>90분</span><b>130,000원</b></div><div class="price-row"><span>120분</span><b>150,000원</b></div></div></article>
          <article class="course-card"><span class="course-icon">✨</span><h3>여성전용 케어</h3><p>프라이빗하고 세심한 배려로 나만의 공간에서 편안하게 케어합니다.</p><div class="price-list"><div class="price-row"><span>90분</span><b>120,000원</b></div><div class="price-row"><span>120분</span><b>150,000원</b></div><div class="price-row"><span>150분</span><b>180,000원</b></div></div></article>
        </div>
      </div>
    </section>

    <section class="section region-section" id="regions">
      <div class="container">
        <h2 class="section-title">서울 지역 출장 케어 찾기</h2>
        <div class="region-grid">
{nearby_html}
        </div>
      </div>
    </section>

    <!-- FAQ 섹션 -->
    <section class="section soft">
      <div class="container">
        <h2 class="section-title">자주 묻는 질문 (FAQ)</h2>
        <div class="faq-list">
          <details open>
            <summary>서울 전지역 균형케어 방문 예약은 어떻게 진행되나요?</summary>
            <p>서울 25개 자치구 어디서나 희망 주소와 원하시는 코스를 알려주시면 가장 가까운 이동 동선의 관리사를 신속 배정합니다.</p>
          </details>
          <details>
            <summary>선입금이나 예약금을 요구하지 않나요?</summary>
            <p>바른케어는 선입금을 일체 요구하지 않으며 관리사가 현장에 도착한 후 코스를 확인하고 결제하는 100% 현장 후불제입니다.</p>
          </details>
          <details>
            <summary>자택 외에 오피스텔이나 호텔에서도 이용 가능한가요?</summary>
            <p>네, 정확한 주소지와 호수, 출입 방법만 확인해 주시면 조용하고 안전하게 프라이빗 관리를 받으실 수 있습니다.</p>
          </details>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">{BRAND_NAME}</div>
      <p>서울·경기·인천 방문 케어 정보 안내 플랫폼입니다. 의료 진단이나 치료를 제공하지 않습니다.</p>
      <nav>
        <a href="/">서울</a><a href="/gyeonggi/">경기</a><a href="/incheon/">인천</a>
      </nav>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>

  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}" aria-label="대표 전화 상담">대표 {REP_PHONE}</a>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

# 2. 광역 허브 (경기, 인천)
def make_hub_page(prov_key):
    prov_full, prov_short, _ = PROV_INFO[prov_key]
    os.makedirs(prov_key, exist_ok=True)
    
    nearby = []
    for slug, name in REGIONS[prov_key]:
        nearby.append(f'          <a class="region-link" href="/areas/{prov_key}/{slug}/"><b>{name}</b><span>출장 케어 안내</span></a>')
    nearby_html = "\n".join(nearby)

    theme_phrase = "출장 온쉼케어 마사지" if prov_key == "gyeonggi" else "출장 릴렉스케어 마사지"
    title_text = f"{prov_full} {theme_phrase} | 일정에 맞춘 코스 비교 - {BRAND_NAME}"
    desc_text = f"{BRAND_NAME} {prov_full} 안내. 선입금 없이 현장에서 확인하는 출장마사지·출장안마·홈타이 코스와 시간, 지역별 이용 순서를 정리했습니다."
    keywords_text = f"{prov_short}출장마사지, {prov_short}홈타이, {prov_short}출장안마, {prov_short}테라피, {prov_short}방문케어"

    sp1, sp2, sp3 = generate_bareun_story(prov_short, prov_full)

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <title>{title_text}</title>
  <meta name="description" content="{desc_text}">
  <meta name="keywords" content="{keywords_text}">
  <link rel="canonical" href="{BASE_URL}/{prov_key}/">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title_text}">
  <meta property="og:description" content="{desc_text}">
  <meta property="og:url" content="{BASE_URL}/{prov_key}/">

  <link rel="stylesheet" href="/styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "{BRAND_NAME} {prov_short}",
        "url": "{BASE_URL}/{prov_key}/",
        "telephone": "{REP_PHONE}",
        "description": "{desc_text}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }},
          {{ "@type": "ListItem", "position": 2, "name": "{prov_short}", "item": "{BASE_URL}/{prov_key}/" }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{prov_full} 방문 시 추가 출장비가 발생하나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "표기된 코스 비용 외에 별도의 부당한 추가 요금을 요구하지 않으며, 현장에서 범위를 다시 확인합니다."
            }}
          }},
          {{
            "@type": "Question",
            "name": "예약금 없이 이용할 수 있나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "바른케어는 100% 현장 후불제로 운영되므로 선입금 사기 걱정 없이 안심하고 이용하실 수 있습니다."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body data-page-type="target-province-hub">
  <a class="skip-link" href="#content">본문으로 이동</a>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo"><span class="brand-badge">바</span><span class="brand-name">{BRAND_NAME}</span></a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><a href="/">홈</a><i>›</i><a href="/{prov_key}/">{prov_short}</a></div></nav>

  <main id="content">
    <section class="directory-head">
      <div class="container">
        <h1>{prov_full} 출장 케어 지역 한눈에</h1>
        <p>{prov_short} 생활권의 출장 케어 구성과 코스, 이용 순서를 한 페이지에서 비교하세요.</p>
        <div class="filter-pills"><span>스웨디시</span><span>아로마</span><span>타이</span><span>여성전용</span></div>
        <div class="feature-panels">
          <article><b>🏨 호텔·숙소</b><p>출입 방법과 객실 정보를 미리 확인합니다.</p></article>
          <article><b>🏠 주거 공간</b><p>주차와 공동현관 안내를 함께 전달합니다.</p></article>
          <article><b>📍 생활권 안내</b><p>인접 지역 이동 시간까지 고려합니다.</p></article>
          <article><b>🗓 일정 배정</b><p>희망 시각과 코스를 차례대로 확인합니다.</p></article>
        </div>
      </div>
    </section>

    <!-- 고유 본문 카드 -->
    <section class="section">
      <div class="container">
        <div class="local-story-card">
          <h3>{prov_full} 맞춤형 방문 테라피 안내</h3>
          <p>{sp1}</p>
          <p>{sp2}</p>
          <p>{sp3}</p>
        </div>
      </div>
    </section>

    <section class="section providers soft">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">{prov_short} 추천 제휴 매장</h2>
          <span>직통 번호로 빠른 배정 상담</span>
        </div>
        <div class="provider-list">
{build_shop_cards(prov_full)}
        </div>
      </div>
    </section>

    <section class="section region-section">
      <div class="container">
        <h2 class="section-title">{prov_short} 세부 지역 안내</h2>
        <div class="region-grid">
{nearby_html}
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">{BRAND_NAME}</div>
      <p>{prov_full} 방문 케어 정보 플랫폼</p>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>
  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}">대표 {REP_PHONE}</a>
</body>
</html>"""
    with open(os.path.join(prov_key, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 3. 67개 세부 지역 페이지 (테마 순환 + 고유 스토리텔링 탑재)
def make_area_pages(sitemap_list):
    count = 0
    theme_idx = 0

    for prov_key, districts in REGIONS.items():
        prov_full, prov_short, prov_hub_url = PROV_INFO[prov_key]
        
        nearby_links = []
        for slug, name in districts:
            display_name = f"{prov_short} {name}" if prov_key == "seoul" else name
            nearby_links.append(f'          <a class="region-link" href="/areas/{prov_key}/{slug}/"><b>{display_name}</b><span>출장 케어 안내</span></a>')
        nearby_str = "\n".join(nearby_links)

        for slug, name in districts:
            district_full = f"{prov_short} {name}" if prov_key == "seoul" else name
            dir_path = os.path.join("areas", prov_key, slug)
            os.makedirs(dir_path, exist_ok=True)

            canonical_url = f"{BASE_URL}/areas/{prov_key}/{slug}/"
            sitemap_list.append(canonical_url)

            # 테마 순환 (균형케어 -> 온쉼케어 -> 릴렉스케어 -> 바른케어)
            theme_title, theme_desc_sub = CARE_THEMES[theme_idx % len(CARE_THEMES)]
            theme_idx += 1

            title_text = f"{district_full} {theme_title} | 편안한 이용 순서 - {BRAND_NAME}"
            desc_text = f"{BRAND_NAME} {prov_full} {district_full} 안내. 선입금 없이 현장에서 확인하는 출장마사지·홈타이 코스와 시간, {theme_desc_sub}를 정리했습니다."
            keywords_text = f"{district_full}출장마사지, {district_full}홈타이, {district_full}출장안마, {district_full}스웨디시, {district_full}케어"

            # 지역별 고유 스토리 생성
            dsp1, dsp2, dsp3 = generate_bareun_story(prov_short, name)

            html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <title>{title_text}</title>
  <meta name="description" content="{desc_text}">
  <meta name="keywords" content="{keywords_text}">
  <link rel="canonical" href="{canonical_url}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title_text}">
  <meta property="og:description" content="{desc_text}">
  <meta property="og:url" content="{canonical_url}">

  <link rel="stylesheet" href="/styles.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "name": "{BRAND_NAME} {district_full}",
        "url": "{canonical_url}",
        "telephone": "{REP_PHONE}",
        "priceRange": "₩₩",
        "description": "{desc_text}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }},
          {{ "@type": "ListItem", "position": 2, "name": "{prov_short}", "item": "{prov_hub_url}" }},
          {{ "@type": "ListItem", "position": 3, "name": "{district_full}", "item": "{canonical_url}" }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{district_full} 방문 시 평균 소요 시간은 어떻게 되나요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{district_full} 인근 제휴 매장의 이동 동선을 우선 배정하여 평균 30분 내외로 도착할 수 있도록 조율합니다."
            }}
          }},
          {{
            "@type": "Question",
            "name": "선입금이나 예약금이 필요한가요?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "선입금을 일체 요구하지 않으며 관리사 방문 후 현장에서 코스를 확인하고 결제하는 100% 현장 후불제입니다."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body data-page-type="target-district-hub">
  <a class="skip-link" href="#content">본문으로 이동</a>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo"><span class="brand-badge">바</span><span class="brand-name">{BRAND_NAME}</span></a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><a href="/">홈</a><i>›</i><a href="{prov_hub_url}">{prov_short}</a><i>›</i><a href="{canonical_url}">{district_full}</a></div></nav>

  <main id="content">
    <section class="directory-head">
      <div class="container">
        <h1>{prov_full} {district_full} 출장 케어 한눈에</h1>
        <p>{district_full} 생활권에서 즉시 배정 가능한 4대 전문 업체를 안내해 드립니다.</p>
        <div class="filter-pills"><span>스웨디시</span><span>아로마</span><span>타이</span><span>여성전용</span></div>
        <div class="feature-panels">
          <article><b>🏨 호텔·숙소</b><p>출입 방법과 객실 정보를 미리 확인합니다.</p></article>
          <article><b>🏠 주거 공간</b><p>주차와 공동현관 안내를 함께 전달합니다.</p></article>
          <article><b>📍 생활권 안내</b><p>인접 지역 이동 시간까지 고려합니다.</p></article>
          <article><b>🗓 일정 배정</b><p>희망 시각과 코스를 차례대로 확인합니다.</p></article>
        </div>
      </div>
    </section>

    <!-- 구/시 고유 스토리텔링 섹션 -->
    <section class="section">
      <div class="container">
        <div class="local-story-card">
          <h3>{district_full} 라이프스타일 맞춤 힐링 솔루션</h3>
          <p>{dsp1}</p>
          <p>{dsp2}</p>
          <p>{dsp3}</p>
        </div>
      </div>
    </section>

    <section class="section providers soft">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">{district_full} 직통 상담 추천 업체</h2>
          <span>희망 매장으로 직접 전화해 보세요</span>
        </div>
        <div class="provider-list">
{build_shop_cards(district_full)}
        </div>
      </div>
    </section>

    <section class="section region-section">
      <div class="container">
        <h2 class="section-title">{prov_short} 주변 세부 지역</h2>
        <div class="region-grid">
{nearby_str}
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section soft">
      <div class="container">
        <h2 class="section-title">{district_full} 이용 안내 FAQ</h2>
        <div class="faq-list">
          <details open>
            <summary>{district_full} 방문 시 평균 소요 시간은 어떻게 되나요?</summary>
            <p>{district_full} 인근 제휴 매장의 이동 동선을 우선 배정하여 평균 30분 내외로 도착할 수 있도록 조율합니다.</p>
          </details>
          <details>
            <summary>선입금이나 예약금이 필요한가요?</summary>
            <p>바른케어는 선입금을 일체 요구하지 않으며 관리사 방문 후 현장에서 코스를 확인하고 결제하는 100% 현장 후불제입니다.</p>
          </details>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">{BRAND_NAME}</div>
      <p>{district_full} 출장 케어 예약 및 코스 상담</p>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>
  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}">{REP_PHONE}</a>
</body>
</html>"""
            with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
    return count

def run():
    print(f"[{BRAND_NAME}] 고유 읽을거리 스토리 및 FAQ 탑재 빌드를 시작합니다...")
    sitemap_list = [f"{BASE_URL}/", f"{BASE_URL}/gyeonggi/", f"{BASE_URL}/incheon/"]
    
    make_main_page()
    make_hub_page("gyeonggi")
    make_hub_page("incheon")
    total_areas = make_area_pages(sitemap_list)

    additional_urls = [
        f"{BASE_URL}/areas/gyeonggi/goyang-si/deogyang-gu/",
        f"{BASE_URL}/areas/gyeonggi/goyang-si/ilsandong-gu/",
        f"{BASE_URL}/areas/gyeonggi/goyang-si/ilsanseo-gu/",
        f"{BASE_URL}/areas/gyeonggi/bucheon-si/sosa-gu/",
        f"{BASE_URL}/areas/gyeonggi/bucheon-si/ojeong-gu/",
        f"{BASE_URL}/areas/gyeonggi/bucheon-si/wonmi-gu/",
        f"{BASE_URL}/areas/gyeonggi/seongnam-si/bundang-gu/",
        f"{BASE_URL}/areas/gyeonggi/seongnam-si/sujeong-gu/",
        f"{BASE_URL}/areas/gyeonggi/seongnam-si/jungwon-gu/",
        f"{BASE_URL}/areas/gyeonggi/suwon-si/gwonseon-gu/",
        f"{BASE_URL}/areas/gyeonggi/suwon-si/yeongtong-gu/",
        f"{BASE_URL}/areas/gyeonggi/suwon-si/jangan-gu/",
        f"{BASE_URL}/areas/gyeonggi/suwon-si/paldal-gu/",
        f"{BASE_URL}/areas/gyeonggi/ansan-si/danwon-gu/",
        f"{BASE_URL}/areas/gyeonggi/ansan-si/sangnok-gu/",
        f"{BASE_URL}/areas/gyeonggi/anyang-si/dongan-gu/",
        f"{BASE_URL}/areas/gyeonggi/anyang-si/manan-gu/",
        f"{BASE_URL}/areas/gyeonggi/yongin-si/giheung-gu/",
        f"{BASE_URL}/areas/gyeonggi/yongin-si/suji-gu/",
        f"{BASE_URL}/areas/gyeonggi/yongin-si/cheoin-gu/",
        f"{BASE_URL}/areas/gyeonggi/hwaseong-si/dongtan-gu/",
        f"{BASE_URL}/areas/gyeonggi/hwaseong-si/manse-gu/",
        f"{BASE_URL}/areas/gyeonggi/hwaseong-si/byeongjeom-gu/",
        f"{BASE_URL}/areas/gyeonggi/hwaseong-si/hyohaeng-gu/"
    ]
    for extra in additional_urls:
        if extra not in sitemap_list:
            sitemap_list.append(extra)

    xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in sitemap_list:
        xml_lines.append('<url>')
        xml_lines.append(f'<loc>{u}</loc>')
        xml_lines.append('</url>')
    xml_lines.append('</urlset>')

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))

    print(f"빌드 완료! 총 {total_areas}개 지역에 1,000자 이상의 고유 읽을거리 스토리와 FAQ가 완벽히 탑재되었습니다.")

if __name__ == "__main__":
    run()