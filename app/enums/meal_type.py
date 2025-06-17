import enum

class MealTypeEnum(str, enum.Enum):
    BREAKFAST = "Desayuno"
    MID_MORNING = "Media mañana"
    LUNCH = "Almuerzo"
    AFTERNOON_SNACK = "Merienda"
    DINNER = "Cena"
