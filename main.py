from transformers import pipeline

classifier = pipeline("zero-shot-classification")
print()
print(classifier(["Російські безпілотники вдарили по Львову та Дублянам Львівської області", 
                  "Окупанти скинули авіабомбу на Оріхів: зруйновано цілий під'їзд, є постраждала",
                  "Російська авіація завдала удару по Оріхову, щонайменше 1 людина поранена"],
                  candidate_labels = ["drone"]))