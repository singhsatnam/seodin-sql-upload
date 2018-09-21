import api

def main():
    data_study = {
        "author": "Aiko Yamashita",
        "description": "Context: Code smells are assumed to indicate bad design",# that leads to less maintainable code. However, this assumption has not been investigated in controlled studies with professional software developers. Aim: This paper investigates the relationship between code smells and maintenance effort. Method: Six developers were hired to perform three maintenance tasks each on four functionally equivalent Java systems originally implemented by different companies. Each developer spent three to four weeks. In total, they modified 298 Java files in the four systems. An Eclipse IDE plug-in measured the exact amount of time a developer spent maintaining each file. Regression analysis was used to explain the effort using file properties, including the number of smells. Result: None of the 12 investigated smells was significantly associated with increased effort after we adjusted for file size and the number of changes; Refused Bequest was significantly associated with decreased effort. File size and the number of changes explained almost all of the modeled variation in effort. Conclusion: The effects of the 12 smells on maintenance effort were limited. To reduce maintenance effort, a focus on reducing code size and the work practices that limit the number of changes may be more beneficial than refactoring code smells.",
        "id": "",
        "title": "Quantifying the effect of code smells on maintenance effort",
        "license": ""
    }
    api.request("Study", 'studies', data_study)