# https://nornickel-hackathon.ru/

Хакатон Норникель: Интеллектуальные горизонты. Трек по задаче: Грязные дела


Некоторые возможные направления работы:   
   
0. Подходы других:  
  
- Soiling Detection / Сontamination  
- https://developer.nvidia.com/blog/?p=13906  
- https://sh-tsang.medium.com/review-soilingnet-soiling-detection-on-automotive-surround-view-cameras-34a108b3506f (https://drive.google.com/drive/folders/1q51oyvx2_SFPts2XgSnKnaVc8ijZ6tKs)  
- https://arxiv.org/pdf/1905.01492 https://arxiv.org/pdf/2007.00801 https://github.com/valeoai/WoodScape?tab=readme-ov-file  
  
1. Данные:   
   
- улучшение существующей разметки   
- поиск открытых реальных данных для решения подобной задачи (Soiling Detection dataset https://drive.google.com/drive/folders/1q51oyvx2_SFPts2XgSnKnaVc8ijZ6tKs и другие)  
- сбор своих реальных данных в "полевых условиях" для решения задачи   
- скрап данных из интернета или из GPT -like для решения подобной задачи    
- поиск классических подходов для генерации синтетики (как raindrop, но другие)   
- поиск нейросетевых подходов    
для генерации синтетики (conditional GAN -like, pix2pix -like, подходы из https://habr.com/ru/companies/nornickel/articles/676296/ или более современные подходы)   
- другое?   
   
2. Алгоритм:   
   
- настройка правильной валидации   
- проверка классических эвристик   
- подбор архитектуры dl модели   
- аугментации  
- лоссы   
- доп штрафы с кастомной логикой (как тут для пузырьков? https://habr.com/ru/companies/ods/articles/705020/)  
- какой- то претрейн на других данных или на себе    
https://docs.lightly.ai/self-supervised-learning/getting_started/main_concepts.html   
- ансамбли подходов   
- другое?
