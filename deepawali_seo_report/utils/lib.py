def getGradeText(section, grade):
    if section == "On-Page SEO":
        if grade == "A+":
            return 'Congratulations! Your page is perfectly optimized for On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. Keep up the good work!'
        elif grade == "A":
            return 'Your page is highly optimized for On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. You can continue to improve your page by ensuring to fix the below suggestions.'
        elif grade == "A-":
            return 'Your page is well optimized for On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. You can consider fixing the below suggestions to improve it further.'
        elif grade == "B+":
            return 'Your page is mostly optimized for On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. You can continue to improve your page by ensuring to fix the below suggestions.'
        elif grade == "B-":
            return 'Your page is slightly optimized for On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. You can continue to improve your page by ensuring HTML Tag Content is completed correctly and text content is well aligned with chosen keywords.'
        elif grade == "C+":
            return 'Your page needs improvement in terms of On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. We recommend addressing the below suggestions.'
        elif grade == "C":
            return 'Your page is poorly optimized for On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. You can consider fixing the below suggestions to improve it further.'
        elif grade == "D+":
            return 'Your page needs major improvement in terms of On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. We recommend addressing the below suggestions.'
        elif grade == "D":
            return 'Your page is severely lacking in On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. You can consider fixing the below suggestions to improve it further.'
        else:
            return 'Your page has very poor On-Page SEO performance. On-Page SEO is important to ensure Search Engines can understand your content appropriately and help it rank for relevant keywords. We recommend addressing the below suggestions to improve it significantly.'

    elif section == "Performance":
        if grade == "A+":
            return 'Congratulations! Your page is blazing fast and perfectly optimized for performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). Keep up the good work!'
        elif grade == "A":
            return 'Your page is highly optimized for performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). You can continue to improve your page by fixing the below suggestions.'
        elif grade == "A-":
            return 'Your page is well optimized for performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        elif grade == "B+":
            return 'Your page is mostly optimized for performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). You can continue to improve your page by fixing the below suggestions.'
        elif grade == "B-":
            return 'Your page is slightly optimized for performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        elif grade == "C+":
            return 'Your page needs improvement in terms of performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). We recommend addressing the below suggestions.'
        elif grade == "C":
            return 'Your page is poorly optimized for performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        elif grade == "D+":
            return 'Your page needs major improvement in terms of performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). We recommend addressing the below suggestions.'
        elif grade == "D":
            return 'Your page is severely lacking in performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        else:
            return 'Your page has very poor performance. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). We recommend addressing the below suggestions to improve it significantly.'

    elif section == "Social":
        if grade == "A+":
            return "Great job! You have a strong social presence and engagement with your audience. Keep up the excellent work."
        elif grade == "A":
            return "Your social presence is very strong and engaging. However, there are a few areas where you can make improvements to further grow your audience and engagement."
        elif grade == "A-":
            return "Your social presence is strong and engaging, but there is room for improvement. Consider making some changes to further grow your audience and engagement."
        elif grade == "B+":
            return "Your social presence is good, but there is room for improvement in terms of engagement and interaction with your audience."
        elif grade == "B-":
            return "Your social presence is okay, but there is definitely room for improvement in terms of engagement and interaction with your audience."
        elif grade == "C+":
            return "Your social presence is lacking in engagement and interaction with your audience. Consider making some changes to improve your social media strategy."
        elif grade == "C":
            return "Your social presence needs improvement in terms of engagement and interaction with your audience. Consider making some changes to your social media strategy."
        elif grade == "D+":
            return "Your social presence is very weak and lacking in engagement with your audience. It's important to improve your social media strategy to better connect with your followers."
        elif grade == "D":
            return "Your social presence is extremely weak and needs significant improvement in terms of engagement and interaction with your audience."
        else:
            return "Your social presence is non-existent or extremely weak. It's important to develop a strong social media strategy to better connect with your audience and increase brand awareness."

    elif section == "Usability":
        if grade == "A+":
            return 'Congratulations! Your page is highly usable across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). Keep up the good work!'
        elif grade == "A":
            return 'Your page is generally usable across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). You can continue to improve your page by fixing the below suggestions.'
        elif grade == "A-":
            return 'Your page is mostly usable across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        elif grade == "B+":
            return 'Your page is somewhat usable across devices, but there is room for improvement. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). You can continue to improve your page by fixing the below suggestions.'
        elif grade == "B-":
            return 'Your page is lacking in usability across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        elif grade == "C+":
            return 'Your page has significant usability issues across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). We recommend addressing the below suggestions.'
        elif grade == "C":
            return 'Your page has usability issues across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        elif grade == "D+":
            return 'Your page has major usability issues across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). We recommend addressing the below suggestions.'
        elif grade == "D":
            return 'Your page has severe usability issues across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). You can consider fixing the below suggestions to improve it further.'
        else:
            return 'Your page has very poor usability across devices. Usability is important to maximize your available audience and minimize user bounce rates (which can indirectly affect your search engine rankings). We recommend addressing the below suggestions to improve it significantly.'


# Your page's performance has some issues and room for improvement. Performance is important to ensure a good user experience, and reduced bounce rates (which can also indirectly affect your search engine rankings). We recommend addressing the highlighted factors below.

def gradeCalculator(seo_data, section):
    score = 0
    total_items = 0

    for i in seo_data.items():
        total_items += 1
        if i[1]["required"] and i[1]["pass"]:
            score += 1

    percentage = (score / total_items) * 100

    grade = ""

    if percentage >= 95:
        grade = "A+"
        grade_title = f'Your {section} is Excellent'
        grade_text = getGradeText(section, grade)

    elif percentage >= 90:
        grade = "A"
        grade_title = f'Your {section} is Very good'
        grade_text = getGradeText(section, grade)

    elif percentage >= 85:
        grade = "A-"
        grade_title = f'Your {section} is good'
        grade_text = getGradeText(section, grade)

    elif percentage >= 80:
        grade = "B+"
        grade_title = f'Your {section} could be better'
        grade_text = getGradeText(section, grade)

    elif percentage >= 70:
        grade = "B-"
        grade_title = f'Your {section} could be better'
        grade_text = getGradeText(section, grade)

    elif percentage >= 60:
        grade = "C+"
        grade_title = f'Your {section} is poor'
        grade_text = getGradeText(section, grade)

    elif percentage >= 50:
        grade = "C-"
        grade_title = f'Your {section} is poor'
        grade_text = getGradeText(section, grade)

    elif percentage >= 40:
        grade = "D+"
        grade_title = f'Your {section} is very poor'
        grade_text = getGradeText(section, grade)

    elif percentage >= 30:
        grade = "D-"
        grade_title = f'Your {section} is very poor'
        grade_text = getGradeText(section, grade)

    else:
        grade = "F"
        grade_title = f'Your {section} needs a lot of improvements'
        grade_text = getGradeText(section, grade)

    return (grade, percentage, grade_title, grade_text)
