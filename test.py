# This Python file uses the following encoding: utf-8

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from summarizer import Summarizer
import sys
import base64

model = Summarizer()
print("1")

text = "최근 중국에서 폐 페스트 환자가 발생해 혹여나 우리나라에서도 전염 사례가 발생하지 않을까 걱정하는 사람들이 많다. ‘흑사병’으로도 잘 알려진 페스트는 페스트균(Yersinia pestis)에 의해 발생하는 급성 열성 감염병이다. 주된 전파 경로는 페스트균을 가지고 있는 쥐벼룩이 사람을 물어서 전파된다고 알려져 있으나 다른 소형 포유동물과의 접촉에 의한 전파도 알려져 있다. 중세 유럽에서 크게 유행해 많은 사망자가 발생했으며 때문에 당시에는 역병(plague)으로도 불렸다. 국내에서는 질병 통계를 수집한 이후 발병이 보고되지 않았으나 2010년대에도 아시아, 아프리카, 아메리카 대륙에서 부분적으로 발생하고 있다. 2012년 미국에서는 감염된 길고양이에 물려서 발생했다고 추정하는 림프절 페스트 환자 사례 보고가 있었다. 올해에는 몽골에서 설치류의 생간을 먹은 사람이 페스트가 발병해 사망했다. 특히 올해 초 한국인 관광객도 예방적으로 격리되어 국내 유입에 대한 우려가 더욱 크다. 페스트에 걸리면 갑작스런 발열이 큰 특징이며 증상에 따라 세 가지 형태로 구분한다.림프절 페스트는 감염된 포유동물이나 벼룩에 물려서 발생하는 경우가 많으며 일반적으로 2일~6일의 잠복기 이후 오한, 38도 이상의 발열, 근육통, 관절통, 두통 등의 증상이 나타난다. 증상 발생 후 24시간 이내에 페스트균이 들어간 신체 부위의 국소 림프절 부위에 통증이 생긴다. 벼룩이 주로 다리를 물기 때문에 흔히 허벅지나 서혜부의 림프절에 침범된다. 치료하면 증상이 빠르게 호전되는데 치료를 하지 않는 경우에는 병이 치명적인 상태로 급속히 진행돼 사망에 이를 수도 있다.림프절 페스트로 진단된 환자 중 20% 정도는 패혈성 페스트다. 증상은 발열, 구역, 구토, 복통, 설사 등 일반적인 패혈증과 같다. 출혈성 반점, 상처 부위의 출혈, 범발성 혈관내 응고증에 의한 말단부의 괴사, 치료가 잘 되지 않는 저혈압, 신장 기능의 저하, 쇼크 등의 증상이 나타날 수 있다. 이러한 패혈성 페스트 환자에서는 말단부의 흑색 괴사가 외견상 쉽게 관찰돼 페스트가 흑사병(black death)이라고도 불린 유래가 됐다.폐 페스트는 가장 중한 형태의 감염병이다. 감염된 환자나 동물의 호흡기 분비물에 비산에 의한 비말 감염이 가능하다고 알려져 있다. 잠복기는 대개 3일~5일이고 급작스럽게 발생하는 오한, 발열, 두통, 전신 무력감의 증상을 동반한다. 빠른 호흡, 호흡 곤란, 기침, 가래, 흉통 등의 호흡기 증상이 발생한다. 질병 이틀째부터는 객혈 증상, 호흡 부전, 심혈관계 부전, 허탈 등의 증상이 나타날 수 있다. 치료하더라도 예후가 좋지 못하다고 알려져 있으며 최근 중국에서 발생한 사례도 폐 페스트로 확인되어 추후 전파에 대한 우려가 큰 상황이다. 페스트는 혈액이나 림프액, 가래 등을 받아 페스트균 배양 검사를 시행해 확진하며 항생제를 투여해 치료한다. 발병 초기에 치료를 시작할 경우에는 효과적인 치료가 가능하다고 알려져 있으므로 조기에 정확하게 진단하는 것이 중요하다. 페스트의 치료에 사용할 수 있는 항생제는 겐타마이신, 스트렙토마이신, 독시사이클린, 레보플록사신 등이 있다. 서울대병원 감염내과 전강일 교수는 “우리나라에서는 최근 페스트가 발생하고 있지 않으며 해외에서도 발생빈도가 흔하지는 않은 병이다. 하지만 내국인들이 흔히 여행을 가게 되는 북미나 중국 내륙에서도 페스트 발병 사례 보고가 있어 해외여행을 하기 전에는 여행 예정 지역에서 최근 발생한 질병에 대한 정보를 확인할 필요가 있다”고 당부했다. 아울러 “페스트는 조기 진단하면 현재 흔히 사용하는 항생제로 효과적인 치료가 가능하지만 진단이 늦어지면 사망률이 매우 높아져 조기 진단이 중요하다. 수 시간 내외에 증상이 급격히 진행된 사례들이 있어 특히 위험지역을 여행하고 페스트와 비슷한 증상이 나타나면 반드시 의심해 조기에 치료를 시작해야 한다”고 조언했다."
result = model(text)
summary = "".join(result)
print(summary)