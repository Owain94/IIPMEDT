score = 0
kcal_score = 0

# Riks cuwle presets
# Score is perfect en kcal varieert.
if score >= 7.0 & (kcal_score > 0 & kcal_score < 100):
    # Ga naar rode vakje (links)
    pass

elif score >= 7.0 & (kcal_score >= 100 & kcal_score < 200):
    # Ga naar oranje vakje (links)
    pass

elif score >= 7.0 & (kcal_score >= 200 & kcal_score < 300):
    # Ga naar geel vakje (links)
    pass

elif score >= 7.0 & (kcal_score >= 300 & kcal_score < 400):
    # Ga naar groen vakje
    pass

elif score >= 7.0 & (kcal_score >= 400 & kcal_score < 500):
    # Ga naar geel vakje (rechts)
    pass

elif score >= 7.0 & (kcal_score >= 500 & kcal_score < 600):
    # Ga naar oranje vakje (rechts)
    pass

elif score >= 7.0 & kcal_score >= 600:
    # Ga naar rood vakje (rechts)
    pass

# Score is oke en kcal varieert.  Kan in geel komen
elif (score > 6.3 & score < 7.0) & (kcal_score > 0 & kcal_score < 100):
    # Ga naar rode vakje (links)
    pass

elif (score > 6.3 & score < 7.0) & (kcal_score >= 100 & kcal_score < 200):
    # Ga naar oranje vakje (links)
    pass

elif (score > 6.3 & score < 7.0) & (kcal_score >= 200 & kcal_score < 350):
    # a naar geel vakje (links)
    pass

elif (score > 6.3 & score < 7.0) & (kcal_score >= 350 & kcal_score < 500):
    # Ga naar geel vakje (rechts)
    pass

elif (score > 6.3 & score < 7.0) & (kcal_score >= 500 & kcal_score < 600):
    # Ga naar oranje vakje (rechts)
    pass

elif (score > 6.3 & score < 7.0) & kcal_score >= 600:
    # Ga naar rood vakje (rechts)
    pass

# Score is net voldoende en kcal varieert. Kan hoogstens in oranje komen
elif (score > 5.4 & score < 6.4) & (kcal_score >= 0 & kcal_score < 200):
    # Ga naar rode vakje (links)
    pass

elif (score > 5.4 & score < 6.4) & (kcal_score >= 200 & kcal_score < 350):
    # Ga naar oranje vakje (links)
    pass

elif (score > 5.4 & score < 6.4) & (kcal_score >= 350 & kcal_score < 600):
    # Ga naar oranje vakje (rechts)
    pass

elif (score > 5.4 & score < 6.4) & kcal_score >= 500:
    # Ga naar rood vakje (rechts)
    pass

# Score geeft lever schade en kcal varieert.
elif score < 5.5 & (kcal_score >= 0 & kcal_score < 350):
    # Ga naar rood vakje (links)
    pass

elif score < 5.5 & (kcal_score >= 350 & kcal_score):
    # Ga naar rood vakje (rechts)
    pass