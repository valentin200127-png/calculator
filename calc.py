print("=" * 50)
print("      🏥 КАЛЬКУЛЯТОР ИНДЕКСА МАССЫ ТЕЛА (ИМТ)")
print("=" * 50)

try:
    weight = float(input("Введите ваш вес (кг): "))
    height = float(input("Введите ваш рост (м): "))
    
    if weight <= 0 or height <= 0 or height > 3:
        print("❌ Ошибка: введите корректные значения!")
        exit()
        
    bmi = weight / (height ** 2)
    
    print("\n" + "─" * 50)
    print(f"📊 Ваш ИМТ: {bmi:.2f}")
    
    # Определение категории
    if bmi < 16:
        category, color, emoji = "Выраженный дефицит веса", "🔴", "НЕМЕДЛЕННО обратитесь к врачу!"
    elif bmi < 18.5:
        category, color, emoji = "Недостаточный вес", "🟡", "Начните правильно питаться"
    elif bmi < 25:
        category, color, emoji = "Нормальный вес ✅", "🟢", "Отличный результат! Продолжайте!"
    elif bmi < 30:
        category, color, emoji = "Избыточный вес", "🟠", "Скорректируйте рацион и добавьте спорт"
    elif bmi < 35:
        category, color, emoji = "Ожирение I степени", "🔶", "Рекомендуется консультация диетолога"
    else:
        category, color, emoji = "Ожирение II-III степени", "🔴", "СРОЧНО обратитесь к врачу!"
    
    print(f"{emoji} Категория: {category}")
    print(f"💡 Рекомендация: {emoji}")
    
    # Идеальный вес
    ideal_min = 18.5 * (height ** 2)
    ideal_max = 24.9 * (height ** 2)
    print(f"⚖️  Идеальный вес для вашего роста: {ideal_min:.1f} - {ideal_max:.1f} кг")
    
    # Разница с идеалом
    if weight < ideal_min:
        print(f"📈 Вам нужно набрать примерно {ideal_min - weight:.1f} кг")
    elif weight > ideal_max:
        print(f"📉 Вам нужно сбросить примерно {weight - ideal_max:.1f} кг")
    else:
        print("✨ Ваш вес в идеальном диапазоне!")
        
except ValueError:
    print("❌ Ошибка: пожалуйста, вводите только числа!")