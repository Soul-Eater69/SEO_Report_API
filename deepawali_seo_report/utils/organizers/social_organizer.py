from deepawali_seo_report.utils.lib import gradeCalculator


def socialOrganizer(seo_obj):
    seo_data = dict()

    facebook_data = seo_obj.has_facebook()
    seo_data["facebook_data"] = {
        "pass": 1 if facebook_data else 0,
        "required": 1,
        "display_title": "Facebook Connected",
        "priority": 2,
        "recommendation": "Make sure to add a Facebook Page link on your website.",
        "description": "Facebook Page found as a link on your page." if facebook_data else "No associated Facebook Page found as a link on your page.",
        "text": "",
        "expand_data": "Creating Social Profiles as well as linking to these from your website can help to build trust in your business and provide other mediums to nurture your customer relationships.\n\nWe recommend creating all common Social Profiles and linking to these from your website. Most CMS systems will offer fields to enter your Social Profile URLs and will display these in a button row section in the footer."
    }

    facebookGraph_data = seo_obj.get_open_graphs()
    seo_data["facebookGraph_data"] = {
        "pass": 1 if len(facebookGraph_data) > 0 else 0,
        "required": 1,
        "priority": 2,
        "recommendation": "Use Open Graph tags to provide information about the content.",
        "display_title": "Facebook Open Graph Tags",
        "description": "Your page is using Facebook Open Graph Tags." if len(facebookGraph_data) > 0 else "Your page is not using Facebook Open Graph Tags.",
        "data": facebookGraph_data,
        "text": "",
        "expand_data": "Facebook Open Graph Tags are a type of structured data that can be placed on your page to control what is shown when your page is shared on Facebook. You can indicate exactly what content should appear in a sharing snippet's title, description, imagery and other information. This is useful when pages like your homepage, products or articles are shared, and effective sharing can drive traffic and conversions. You may want to ensure that the content presented is correct and has the highest chance of attracting visitors. If you don't define specific content, Facebook may decide automatically which pieces of text and imagery are displayed which may not always be correct or appealing.\n\nWe recommend defining as many of Facebook's Open Graph fields as possible, and inserting this code into the HTML of your page. Facebook has a helper tool for creating this content, or sometimes it can be written automatically with the help of a CMS plugin."
    }

    facebookPixel_data = seo_obj.get_facebook_pixel()
    seo_data["facebookPixel_data"] = {
        "pass": 1 if facebookPixel_data else 0,
        "required": 1,
        "priority": 2,
        "recommendation": "Consider Adding Facebook's Pixel to your page.",
        "display_title": "Facebook Pixel",
        "description": "Facebook's Pixel is a useful piece of analytics code that allows you to retarget visitors if you decide to run Facebook Ads in future.",
        "text": "We have detected a Facebook Pixel on your page." if facebookPixel_data else "We have not detected a Facebook Pixel on your page.",
        "expand_data": "Facebook Pixel is a piece of analytics code that allows Facebook to capture and analyse visitor information from your site. This allows you to retarget these visitors with Facebook messaging in future, or build new 'lookalike' audiences similar to your existing visitors.\n\nIn can be a good idea to install a Facebook Pixel if you intend to do any Facebook related marketing in the future in order to prepare audience data."
    }

    twitter_data = seo_obj.has_twitter()
    seo_data["twitter_data"] = {
        "pass": 1 if twitter_data else 0,
        "required": 1,
        "priority": 2,
        "recommendation": "Create and link your Twitter profile.",
        "display_title": "Twitter Connected",
        "description": "",
        "text": "Associated Twitter profile found as a link on your page." if twitter_data else "No associated Twitter profile found as a link on your page.",
        "expand_data": ""
    }

    twitterCards_data = seo_obj.get_twitter_cards()
    seo_data["twitterCards_data"] = {
        "pass": 1 if len(twitterCards_data) > 0 else 0,
        "required": 1,
        "display_title": "Twitter Cards",
        "priority": 2,
        "recommendation": "Use Twitter Card tags to provide information.",

        "description": "",
        "data": twitterCards_data,
        "text": "Your page is using Twitter Cards." if len(twitterCards_data) > 0 else "Your page is not using Twitter Cards.",
        "expand_data": ""
    }

    instagram_data = seo_obj.has_instagram()
    seo_data["instagram_data"] = {
        "pass": 1 if instagram_data else 0,
        "required": 1,
        "display_title": "Instagram Connected",
        "priority": 2,
        "recommendation": "Create and link your Instagram account to your website.",
        "description": "",
        "text": "Your page has a link to an Instagram profile." if instagram_data else "Your page does not have a link to an Instagram profile.",
        "expand_data": ""
    }

    linkedin_data = seo_obj.has_linkedin()
    seo_data["linkedin_data"] = {
        "pass": 1 if linkedin_data else 0,
        "required": 1,
        "priority": 2,
        "recommendation": "Create and link your LinkedIn profile to your website.",
        "display_title": "LinkedIn Connected",
        "description": "",
        "text": "Your page has a link to a LinkedIn profile." if linkedin_data else "Your page does not have a link to a LinkedIn profile.",
        "expand_data": ""
    }

    youtube_data = seo_obj.get_youtube_data()
    print("Youtube\n\n\n\n\n\n\n", youtube_data)
    seo_data["youtube_data"] = {
        "pass": 1 if youtube_data["hasYoutube"] else 0,
        "required": 1,
        "display_title": "YouTube Connected",
        "priority": 2,
        "recommendation": " Create and link your YouTube channel to your website.",
        "description": "",
        "data": youtube_data,
        "text": "Your page has a link to a YouTube channel." if youtube_data["hasYoutube"] else "Your page does not have a link to a YouTube channel.",
        "expand_data": ""
    }

    for i in seo_data:
        seo_data[i]["category"] = "Social"

    grade, percentage, grade_title, grade_text = gradeCalculator(
        seo_data, "Social")
    seo_data["percentage"] = percentage
    seo_data["grade"] = grade
    seo_data["grade_title"] = grade_title
    seo_data["grade_text"] = grade_text

    return seo_data
