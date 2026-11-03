# Custom educational self-reflection questionnaire; NOT clinically validated.
QUESTIONS=[
 {'id':'m1','category':'Mood','text':'During the past two weeks, how often have you felt down, low, or emotionally heavy?'},
 {'id':'m2','category':'Mood','text':'How often have you had less interest or enjoyment in activities you usually like?'},
 {'id':'a1','category':'Anxiety','text':'How often have you worried about several things and struggled to switch those thoughts off?'},
 {'id':'a2','category':'Anxiety','text':'How often have you felt tense, restless, or on edge without an obvious immediate reason?'},
 {'id':'s1','category':'Stress','text':'How often have everyday responsibilities felt so overwhelming that it was difficult to know where to start?'},
 {'id':'s2','category':'Stress','text':'How often have you felt unusually irritable or unable to unwind after a demanding day?'},
 {'id':'sl1','category':'Sleep','text':'How often has it been difficult to fall asleep, stay asleep, or get restful sleep?'},
 {'id':'sl2','category':'Sleep','text':'How often have you felt tired during the day even after having time to sleep?'},
 {'id':'c1','category':'Focus','text':'How often have you struggled to concentrate on reading, studying, conversations, or routine tasks?'},
 {'id':'c2','category':'Focus','text':'How often has it been difficult to make ordinary decisions or complete tasks you started?'},
 {'id':'f1','category':'Daily functioning','text':'How often have emotional difficulties interfered with your studies, work, or everyday responsibilities?'},
 {'id':'f2','category':'Daily functioning','text':'How often have you avoided friends, family, or activities because you did not feel up to them?'}]
def assess_answers(answers,safety):
    groups={}
    for q in QUESTIONS: groups.setdefault(q['category'],[]).append(answers[q['id']])
    breakdown={}
    for name,vals in groups.items():
        score=sum(vals); maximum=len(vals)*4; pct=round(score/maximum*100)
        level='Lower' if pct<25 else 'Mild' if pct<50 else 'Elevated' if pct<75 else 'Higher'
        note='Fewer frequent difficulties reported.' if pct<25 else 'Some difficulties may be present; notice whether they persist.' if pct<50 else 'This area may deserve extra attention.' if pct<75 else 'Frequent difficulties reported in this area.'
        breakdown[name]={'score':score,'maximum':maximum,'percent':pct,'level':level,'note':note}
    total=sum(x['score'] for x in breakdown.values()); maximum=sum(x['maximum'] for x in breakdown.values()); pct=round(total/maximum*100)
    overall='Lower reported difficulty' if pct<25 else 'Some areas to monitor' if pct<50 else 'Elevated indicators' if pct<75 else 'Higher indicators'
    summary='Your answers indicate relatively few frequent difficulties across the areas covered.' if pct<25 else 'Your answers indicate some recurring difficulties. Supportive habits and connection may help.' if pct<50 else 'Your answers indicate recurring difficulties. Consider speaking with a qualified counsellor or mental health professional.' if pct<75 else 'Your answers indicate frequent difficulties across several areas. Consider reaching out to a qualified mental health professional.'
    safety_message=None
    if safety=='yes': safety_message='You indicated thoughts of hurting yourself or not wanting to be here. Please reach out to a trusted person now and seek urgent professional help. If you may act on these thoughts or are in immediate danger, call India emergency number 112 or go to the nearest emergency department. Try not to stay alone.'
    elif safety=='unsure': safety_message='Because you are unsure about your safety, please speak with someone you trust and contact a qualified mental health professional promptly. If in immediate danger, call 112 in India or go to the nearest emergency department.'
    return {'overall':overall,'summary':summary,'percent':pct,'breakdown':breakdown,'safety_message':safety_message,'suggestions':['Keep a short daily note of mood, sleep and possible stress triggers.','Try a consistent sleep and wake time, where practical.','Break study or work into smaller tasks with short restorative breaks.','Stay connected with someone you trust.']}
