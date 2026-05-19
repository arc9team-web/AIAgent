import csv
import sys

# Data definition
data = [
    # URL 1
    {
        "url_no": 1,
        "title": "QAFD-RAG: 질문의 의미로 지식 그래프를 탐색하는 Graph 기반 RAG",
        "url": "https://www.samsungsds.com/kr/research-blog/qafd-rag-query-aware-flow-diffusion-graph-rag.html",
        "img_no": 1,
        "filename": "qafd-rag-thumb.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "QAFD-RAG 기술블로그 대표 썸네일 이미지 - 질문의 의미로 지식 그래프를 탐색하는 Graph 기반 RAG"
    },
    {
        "url_no": 1,
        "title": "QAFD-RAG: 질문의 의미로 지식 그래프를 탐색하는 Graph 기반 RAG",
        "url": "https://www.samsungsds.com/kr/research-blog/qafd-rag-query-aware-flow-diffusion-graph-rag.html",
        "img_no": 2,
        "filename": "260406_1_01.png",
        "current_alt": "세 가지 서로 다른 그래프 기반 RAG 방법(GraphRAG, LightRAG, QAFD-RAG)이 '애플에서 스티브 잡스의 제품을 소개하라'는 질의에 대해 데이터를 추출하는 방식을 비교한 시각화 자료입니다.",
        "type": "Type B (도식)",
        "improved_alt": "그림 1: GraphRAG, LightRAG, QAFD-RAG의 그래프 기반 검색 방식을 비교한 다이어그램. 사용자의 질문 “애플에서 스티브 잡스의 제품을 소개해줘”에 대해, GraphRAG는 관련·비관련 노드를 함께 포함한 큰 커뮤니티를 검색하고, LightRAG는 1-hop 이웃 노드를 중심으로 일부 불필요한 정보를 포함한다. 반면 QAFD-RAG는 질의 의미에 따라 그래프 경로 가중치를 조정해 Mac, macOS 등 관련 노드만 강조하고 Amazon River, Apple fruit 같은 비관련 노드는 억제한다. 노드 크기와 색상은 중요도, 간선 두께는 연관 강도를 나타낸다."
    },
    {
        "url_no": 1,
        "title": "QAFD-RAG: 질문의 의미로 지식 그래프를 탐색하는 Graph 기반 RAG",
        "url": "https://www.samsungsds.com/kr/research-blog/qafd-rag-query-aware-flow-diffusion-graph-rag.html",
        "img_no": 3,
        "filename": "260406_1_02.png",
        "current_alt": "QAFD-RAG 시스템의 작동 과정을 보여주는 순서도로, 문서를 지식 그래프(KG)로 만드는 '인덱싱 단계'와 질의에 따라 답을 생성하는 '질의 단계'로 구성됩니다.",
        "type": "Type B (도식)",
        "improved_alt": "그림 2: QAFD-RAG의 2단계 처리 구조를 설명한 다이어그램. 첫 단계에서는 문서를 청크로 분할하고 엔터티 및 관계를 추출해 지식 그래프(KG)를 생성한다. 두 번째 단계에서는 사용자 질의를 기반으로 시드 노드를 선택하고 Query-Aware Flow Diffusion을 적용해 관련 서브그래프를 추출한 뒤, 이를 프롬프트에 포함해 최종 응답을 생성한다."
    },
    
    # URL 2
    {
        "url_no": 2,
        "title": "더 짧아진 PQC 전자서명 – 비결은 '느슨한 벡터 커밋먼트'?",
        "url": "https://www.samsungsds.com/kr/research-blog/pqc-vector-semi-commitment.html",
        "img_no": 1,
        "filename": "card_list_img_보안논문_2.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "더 짧아진 PQC 전자서명 보안 논문 대표 썸네일 이미지"
    },

    # URL 3
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 1,
        "filename": "agentic-ai_thumb_418x365.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "한국정보처리학회 2025년 IT21 글로벌 컨퍼런스 키노트 스피치 리뷰 대표 썸네일"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 2,
        "filename": "250721_2_01.jpg",
        "current_alt": "250721_2_01_images",
        "type": "Type A (사진)",
        "improved_alt": "IT21 글로벌 컨퍼런스 키노트 스피치를 시작하며 청중에게 인사하고 있는 권영준 삼성SDS 연구소장의 모습"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 3,
        "filename": "250721_2_02.jpg",
        "current_alt": "250721_2_02_images",
        "type": "Type A (사진)",
        "improved_alt": "키노트 스피치 중 '창발(Emergence)' 개념에 대해 설명하고 있는 권영준 삼성SDS 연구소장"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 4,
        "filename": "250721_2_03.jpg",
        "current_alt": "250721_2_03_images",
        "type": "Type A (사진)",
        "improved_alt": "키노트 스피치를 경청하고 있는 IT21 컨퍼런스 청중들의 모습"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 5,
        "filename": "250721_2_04.jpg",
        "current_alt": "250721_2_04_images",
        "type": "Type A (사진)",
        "improved_alt": "키노트 스피치 마무리에 청중들에게 질문을 던지고 있는 권영준 삼성SDS 연구소장"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 6,
        "filename": "250721_2_05.png",
        "current_alt": "250721_2_05_images",
        "type": "Type A (사진)",
        "improved_alt": "'학습 데이터 Self-Curation을 통한 LLM 응답 품질 향상 연구'를 발표하는 이준호 프로(AI연구팀)"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 7,
        "filename": "250721_2_06.png",
        "current_alt": "250721_2_06_images",
        "type": "Type A (사진)",
        "improved_alt": "'PAISE: PIM을 활용한 LLM 추론 가속 스케줄링 엔진'을 발표하는 이효정 프로(클라우드연구팀)"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 8,
        "filename": "250721_2_07.png",
        "current_alt": "250721_2_07_images",
        "type": "Type A (사진)",
        "improved_alt": "'AI 기반의 테스트 자동생성 기술 연구 및 산업 현장 적용'을 발표하는 문석현 프로(보안연구팀)"
    },
    {
        "url_no": 3,
        "title": "AI의 새로운 지평: 어텐션, 창발, 그리고 Agentic AI",
        "url": "https://www.samsungsds.com/kr/research-blog/agentic-ai-emergence-attention.html",
        "img_no": 9,
        "filename": "250721_2_08.png",
        "current_alt": "250721_2_08_images",
        "type": "Type A (사진)",
        "improved_alt": "'프라이버시 강화 기술 및 응용 사례'를 발표하는 한규형 프로(보안연구팀)"
    },

    # URL 4
    {
        "url_no": 4,
        "title": "자바 앱이 갑자기 꺼진다면? 그건 NPE 때문입니다",
        "url": "https://www.samsungsds.com/kr/research-blog/npe-test-generation.html",
        "img_no": 1,
        "filename": "research-blog_thumb_02.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "NPE(Null Pointer Exception) 자동 탐지 기술 소개 보안 논문 대표 썸네일"
    },
    {
        "url_no": 4,
        "title": "자바 앱이 갑자기 꺼진다면? 그건 NPE 때문입니다",
        "url": "https://www.samsungsds.com/kr/research-blog/npe-test-generation.html",
        "img_no": 2,
        "filename": "250617_6_01.JPG",
        "current_alt": "250617_6_01 images",
        "type": "Type B (코드)",
        "improved_alt": "Apache Qpid Proton-j 프로젝트의 EncoderImpl.java 코드 예시로, calculateSize 메서드에서 t.getEncoding(k) 호출 시 NPE가 발생할 수 있는 지점을 보여줌"
    },
    {
        "url_no": 4,
        "title": "자바 앱이 갑자기 꺼진다면? 그건 NPE 때문입니다",
        "url": "https://www.samsungsds.com/kr/research-blog/npe-test-generation.html",
        "img_no": 3,
        "filename": "250617_6_02.JPG",
        "current_alt": "250617_6_02 images",
        "type": "Type B (코드)",
        "improved_alt": "Apache Qpid Proton-j 프로젝트의 EncoderImpl.java 코드 예시 - NPE 원인이 되는 deduceTypeFromClass 메서드의 AMQPType 반환 로직 부분"
    },
    {
        "url_no": 4,
        "title": "자바 앱이 갑자기 꺼진다면? 그건 NPE 때문입니다",
        "url": "https://www.samsungsds.com/kr/research-blog/npe-test-generation.html",
        "img_no": 4,
        "filename": "250617_6_03.jpg",
        "current_alt": "250617_6_03 images",
        "type": "Type B (도식)",
        "improved_alt": "NpeTest, EvoSuite, Randoop 도구별 산업용 암호화 라이브러리에서 발견된 NPE 개수를 비교한 벤다이어그램"
    },

    # URL 5
    {
        "url_no": 5,
        "title": "퍼블릭 클라우드에서 삼성 클라우드 플랫폼으로의 전환 성공 사례",
        "url": "https://www.samsungsds.com/kr/techreport/migration-from-public-cloud-to-samsung-cloud-migration.html",
        "img_no": 1,
        "filename": "Cloud_thumb_0918.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "퍼블릭 클라우드에서 삼성 클라우드 플랫폼(SCP)으로의 전환 성공 사례 클라우드 기술 백서 대표 썸네일"
    },
    {
        "url_no": 5,
        "title": "퍼블릭 클라우드에서 삼성 클라우드 플랫폼으로의 전환 성공 사례",
        "url": "https://www.samsungsds.com/kr/techreport/migration-from-public-cloud-to-samsung-cloud-migration.html",
        "img_no": 2,
        "filename": "cloud_featured_0811_1.jpg",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 기술 백서 본문 헤더 이미지(PC용) - 퍼블릭 클라우드에서 SCP로의 전환"
    },
    {
        "url_no": 5,
        "title": "퍼블릭 클라우드에서 삼성 클라우드 플랫폼으로의 전환 성공 사례",
        "url": "https://www.samsungsds.com/kr/techreport/migration-from-public-cloud-to-samsung-cloud-migration.html",
        "img_no": 3,
        "filename": "cloud_featured_0811.jpg",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 기술 백서 본문 헤더 이미지(모바일용) - 퍼블릭 클라우드에서 SCP로의 전환"
    },

    # URL 6
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 1,
        "filename": "0603_01_thumb.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "SCP를 활용한 클라우드 재해복구(DR) 구축 가이드 대표 썸네일"
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 2,
        "filename": "0603_01_pc.png",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 DR 구축 백서 본문 헤더 이미지(PC용)"
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 3,
        "filename": "0603_01_mo.png",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 DR 구축 백서 본문 헤더 이미지(모바일용)"
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 4,
        "filename": "img_techreport_repo1284063_01.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "[그림1] 대표적인 IT 서비스 중단 사건 3건 요약 - 데이터센터 화재(K 메신저, 5일), 인적 실수(CSP A사, 4시간), HW/SW 결함(국가 행정망, 3일)"
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 5,
        "filename": "img_techreport_repo1284063_02.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "[그림2] RPO(Recovery Point Objective)와 RTO(Recovery Time Objective) 개념도 - 재난재해 발생 시점 기준으로 데이터 손실 허용 시점과 서비스 복구 목표 시간을 표시"
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 6,
        "filename": "img_techreport_repo1284063_03.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 3: DR 레벨 비교 표. 가로축은 Mirror, Hot, Warm, Cold 등 DR 구성 수준이고, 세로축은 RTO, RPO, 가용성, 복구 방식, 비용, 적용 업무를 나타낸다. Mirror에서 Cold로 갈수록 복구 시간과 데이터 손실 허용 범위는 증가하고 비용은 감소한다. Mirror는 실시간 이중화와 자동 전환을 제공하며, Cold는 백업 기반의 저비용 복구 방식이다."
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 7,
        "filename": "img_techreport_repo1284063_04.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 4: Legacy DR과 Cloud DR 비교 표. 가로축은 Legacy와 Cloud 방식, 세로축은 구축 방식, 비용, 운영, 확장성, 모의훈련 등의 비교 항목이다. Cloud DR은 물리 장비 구축 부담이 적고 구축 기간과 유지 비용이 낮으며, 자원 확장과 테스트가 상대적으로 유연한 특징을 보인다."
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 8,
        "filename": "img_techreport_repo1284063_05.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 5: SCP DR 기능 지원 표. 가로축은 Compute, Networking, Storage, Database 영역이고, 세로축은 Virtual Server DR, VPC Peering, VPN, Storage 복제, DB Replica 등 DR 관련 기능이다. 인프라 전 영역에서 복제·연결·백업 기능을 제공하며, 서비스 유형별로 지원 가능한 DR 기능이 정리되어 있다."
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 9,
        "filename": "img_techreport_repo1284063_06.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 6: SCP DR 구축 Use Case 표. 가로축은 SCP to SCP, On-Premise 또는 타 CSP to SCP 구성이고, 세로축은 Mirror, Hot, Warm, Cold DR 지원 여부이다. Mirror는 지원되지 않으며 Hot, Warm, Cold 중심으로 DR 구성이 가능함을 보여준다."
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 10,
        "filename": "img_techreport_repo1284063_07.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 7: SCP 기반 Hot Level DR 구성도. 주 센터와 DR 센터를 VPC Peering으로 연결하고 Virtual Server, DBaaS, Storage 데이터를 비동기 복제하는 구조이다. 재해 발생 시 DR 센터 자원을 사용해 빠르게 서비스를 복구한다."
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 11,
        "filename": "img_techreport_repo1284063_08.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 8: SCP 기반 Cold Level DR 구성도. 운영 데이터를 Object Storage에 백업 후 DR 센터로 복제하며, 평상시 DR 서버는 중지 상태로 유지된다. 재해 시 백업 데이터를 기반으로 서버를 복구해 서비스를 재개한다."
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 12,
        "filename": "img_techreport_repo1284063_09.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 9: On-Premise 또는 타 CSP 연계 Hot Level DR 구성도. 전용회선과 Transit Gateway로 SCP DR 센터와 연결하고, OS·데이터·DB 복제 소프트웨어를 이용해 변경 데이터를 지속 복제하는 구조이다."
    },
    {
        "url_no": 6,
        "title": "Samsung Cloud Platform을 활용한 클라우드 DR 구축",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-dr-on-scp.html",
        "img_no": 13,
        "filename": "img_techreport_repo1284063_10.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "그림 10: On-Premise 또는 타 CSP 연계 Cold Level DR 구성도. 운영 환경 데이터를 Backup Server and Object Storage에 저장하고 DR 센터로 복제한다. 재해 시 DR 서버를 기동해 백업 데이터를 복원하는 백업 중심 구조이다."
    },

    # URL 7
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 1,
        "filename": "0822_01.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "삼성 클라우드 플랫폼 클라우드 데이터베이스(Database) 상품의 이해 클라우드 기술 백서 대표 썸네일"
    },
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 2,
        "filename": "01_w.jpg",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 데이터베이스 기술 백서 본문 헤더 이미지(PC용)"
    },
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 3,
        "filename": "01_m_1.jpg",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 데이터베이스 기술 백서 본문 헤더 이미지(모바일용)"
    },
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 4,
        "filename": "img_techreport_repo20_1.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "IDC 조사 결과 기반 데이터베이스 클라우드 마이그레이션 현황 그래프 - 적극 이행 중 63%, 3년 내 시작 계획 29%, 검토 중 8% (출처: IDC, 2020년 12월)"
    },
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 5,
        "filename": "img_techreport_repo20_2.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "SCP DB서비스 개요도 - RDB 7종(EPAS, PostgreSQL, MariaDB, MySQL, MS SQL Server, Tibero, Vertica) 및 NoSQL 2종(Redis, ElasticSearch)을 제공하는 자동화 기반 GUI 셀프 서비스 구성도"
    },
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 6,
        "filename": "img_techreport_repo20_3.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "DBMS 이중화 통합 아키텍처 구성도 - WEB/WAS와 Primary/Secondary VM DB, Quorum 서비스를 활용한 Split Brain 예방 구성 및 Synchronous Replication 구조"
    },
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 7,
        "filename": "img_techreport_repo20_4.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "삼성 클라우드 플랫폼 DB 서비스 주요 기능 인포그래픽 - DB Provisioning, Backup & Recovery, 가동 관리, HA 구성, Scale Out, Monitoring, Parameter Configuration, Audit, Minor Patch, Read Replica 등"
    },
    {
        "url_no": 7,
        "title": "삼성 클라우드 플랫폼, 클라우드 데이터베이스 상품의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/what-is-cloud-database.html",
        "img_no": 8,
        "filename": "img_techreport_repo20_5.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "SCP DB 서비스 적용 시 인건비 효율화 효과 비교 그래프 - 자동화 미적용 대비 가중치 81% 감소, 운영 DB 수량 1대→5대, 대당 인건비 5백만원→0.9백만원"
    },

    # URL 8
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 1,
        "filename": "03_thumb.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "클라우드 핀옵스(FinOps) 기술 백서 대표 썸네일 이미지"
    },
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 2,
        "filename": "03_1.png",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 핀옵스 기술 백서 본문 헤더 이미지(PC용)"
    },
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 3,
        "filename": "03_m.png",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 핀옵스 기술 백서 본문 헤더 이미지(모바일용)"
    },
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 4,
        "filename": "img_techreport_repo9_2.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "전 세계 클라우드 서비스 지출 규모를 나타낸 막대그래프. 가로축은 연도, 세로축은 지출 금액(십억 달러)이다. 시장 규모는 2019년 약 1,000억 달러 수준에서 2022년 약 2,000억 달러 이상으로 지속 증가하며, 특히 2020년 이후 성장 폭이 크게 확대되는 추세를 보여준다."
    },
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 5,
        "filename": "img_techreport_repo9_3.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "FinOps 조직 참여 구조도. Executive, Finance, Procurement, Product Owner, Engineering, Operations 등 다양한 조직이 중앙의 FinOps 기능과 연결되어 있다. 기술·재무·서비스 조직이 함께 비용 최적화를 수행하는 협업 구조를 나타낸다."
    },
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 6,
        "filename": "img_techreport_repo9_4.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "삼성SDS Cloud inOne FinOps 정책 설정 화면 캡쳐 - 자원 최적화 총점, 비용 최적화 총점, PRD/STG/DEV별 자원 최적화 정책 기준, Rightsizing 자원관리 및 Unused 자원관리 설정 UI"
    },
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 7,
        "filename": "img_techreport_repo9_5.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "삼성SDS Cloud inOne FinOps 정책 시뮬레이션 화면 캡쳐 - 자원 최적화 및 비용 최적화 설정 옵션, 정책 기준에 따른 시뮬레이션 결과 차트 표시 UI"
    },
    {
        "url_no": 8,
        "title": "소중한 자원이 낭비되지 않도록, 클라우드 핀옵스에 포커스",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-finops.html",
        "img_no": 8,
        "filename": "img_techreport_repo9_6.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "삼성SDS Cloud inOne FinOps 프로세스 설정 기능 화면 캡쳐 - 자원 최적화 추천 프로세스 5단계(Trigger, Notification, Review, Service Request, Completion) 흐름도"
    },

    # URL 9
    {
        "url_no": 9,
        "title": "클라우드 스토리지 기술의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-storage.html",
        "img_no": 1,
        "filename": "09_thumb.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "클라우드 스토리지(Cloud Storage) 기술의 이해 클라우드 기술 백서 대표 썸네일"
    },
    {
        "url_no": 9,
        "title": "클라우드 스토리지 기술의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-storage.html",
        "img_no": 2,
        "filename": "09_1.png",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 스토리지 기술 백서 본문 헤더 이미지(PC용)"
    },
    {
        "url_no": 9,
        "title": "클라우드 스토리지 기술의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-storage.html",
        "img_no": 3,
        "filename": "09_m.png",
        "current_alt": "(빈 값)",
        "type": "Type D (헤더)",
        "improved_alt": "클라우드 스토리지 기술 백서 본문 헤더 이미지(모바일용)"
    },
    {
        "url_no": 9,
        "title": "클라우드 스토리지 기술의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-storage.html",
        "img_no": 4,
        "filename": "img_techreport_repo3_2.png",
        "current_alt": "(빈 값)",
        "type": "Type B (도식)",
        "improved_alt": "스토리지 종류별 접근 방식 다이어그램 - Application에서 Local Disk(직접 접근), SAN(FC/iSCSI/FCoE - Block), NAS(NFS/SMB - File), Object(REST API - Object)로 연결되는 스토리지 계층 구조도"
    },
    {
        "url_no": 9,
        "title": "클라우드 스토리지 기술의 이해",
        "url": "https://www.samsungsds.com/kr/techreport/cloud-storage.html",
        "img_no": 5,
        "filename": "img_techreport_repo3_3.png",
        "current_alt": "(빈 값)",
        "type": "Type C (장식용)",
        "improved_alt": "alt=\"\" (장식용 이미지이므로 대체 텍스트 제외)"
    },

    # URL 10
    {
        "url_no": 10,
        "title": "업스테이지가 GPU 수급난 속에서 H100을 확보한 방법",
        "url": "https://www.samsungsds.com/kr/case-study/gpuaas-upstage.html",
        "img_no": 1,
        "filename": "customer_detail_new_sample_hero.png",
        "current_alt": "(빈 값)",
        "type": "Type D (썸네일)",
        "improved_alt": "업스테이지 고객 성공 스토리 대표 히어로 이미지 - 삼성 클라우드 플랫폼 GPUaaS 도입 사례"
    },
    {
        "url_no": 10,
        "title": "업스테이지가 GPU 수급난 속에서 H100을 확보한 방법",
        "url": "https://www.samsungsds.com/kr/case-study/gpuaas-upstage.html",
        "img_no": 2,
        "filename": "customer_detail_new_sample_01.png",
        "current_alt": "(빈 값)",
        "type": "Type A (사진)",
        "improved_alt": "[Figure 1] 업스테이지의 비즈니스와 핵심 기술에 대해 소개하고 있는 업스테이지 김민성 LLM 사업개발 팀장의 인터뷰 모습"
    },
    {
        "url_no": 10,
        "title": "업스테이지가 GPU 수급난 속에서 H100을 확보한 방법",
        "url": "https://www.samsungsds.com/kr/case-study/gpuaas-upstage.html",
        "img_no": 3,
        "filename": "customer_detail_new_sample_03.png",
        "current_alt": "(빈 값)",
        "type": "Type A (사진)",
        "improved_alt": "[Figure 3] 업스테이지의 글로벌 웹사이트 메인 페이지 캡쳐 화면"
    },
    {
        "url_no": 10,
        "title": "업스테이지가 GPU 수급난 속에서 H100을 확보한 방법",
        "url": "https://www.samsungsds.com/kr/case-study/gpuaas-upstage.html",
        "img_no": 4,
        "filename": "customer_detail_new_sample_03.png",
        "current_alt": "(빈 값)",
        "type": "Type C (장식용)",
        "improved_alt": "alt=\"\" (장식용 이미지이므로 대체 텍스트 제외)"
    },
    {
        "url_no": 10,
        "title": "업스테이지가 GPU 수급난 속에서 H100을 확보한 방법",
        "url": "https://www.samsungsds.com/kr/case-study/gpuaas-upstage.html",
        "img_no": 5,
        "filename": "customer_detail_new_sample_05.png",
        "current_alt": "(빈 값)",
        "type": "Type A (사진)",
        "improved_alt": "[Figure 4] 삼성 클라우드 플랫폼 GPUaaS를 업스테이지의 '엔진룸'에 비유하며 설명하고 있는 김민성 LLM 사업개발 팀장"
    },
    {
        "url_no": 10,
        "title": "업스테이지가 GPU 수급난 속에서 H100을 확보한 방법",
        "url": "https://www.samsungsds.com/kr/case-study/gpuaas-upstage.html",
        "img_no": 6,
        "filename": "customer_detail_new_sample_writer_img.png",
        "current_alt": "(빈 값)",
        "type": "Type A (사진)",
        "improved_alt": "본문 작성자 프로필 이미지 - 삼성SDS B2B 마케터 '보배'"
    }
]

# Attempt to write to Excel using pandas / openpyxl if installed
excel_success = False
try:
    import pandas as pd
    df = pd.DataFrame(data)
    # Rename columns for presentation
    df.columns = [
        "URL 번호",
        "페이지 제목",
        "URL 주소",
        "이미지 번호",
        "이미지 파일명",
        "현재 Alt 값",
        "이미지 분류 타입",
        "개선된 대체텍스트"
    ]
    df.to_excel("samsung_sds_alt_text_report.xlsx", index=False)
    excel_success = True
    print("XLSX generated successfully.")
except Exception as e:
    print(f"Failed to generate XLSX: {e}", file=sys.stderr)

# Always write to CSV with UTF-8 BOM so it opens correctly in Excel
try:
    with open("samsung_sds_alt_text_report.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "URL 번호",
            "페이지 제목",
            "URL 주소",
            "이미지 번호",
            "이미지 파일명",
            "현재 Alt 값",
            "이미지 분류 타입",
            "개선된 대체텍스트"
        ])
        for row in data:
            writer.writerow([
                row["url_no"],
                row["title"],
                row["url"],
                row["img_no"],
                row["filename"],
                row["current_alt"],
                row["type"],
                row["improved_alt"]
            ])
    print("CSV generated successfully.")
except Exception as e:
    print(f"Failed to generate CSV: {e}", file=sys.stderr)
