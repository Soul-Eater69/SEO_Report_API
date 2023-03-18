def performanceOrganizer(seo_obj):
    seo_data = dict()

    compression_data = seo_obj.get_compression_data()
    seo_data["compression_data"] = {
        "pass": 1,
        "required": 0,
        "data":compression_data,
        "display_title": "Device Rendering",
        "description": "This check visually demonstrates how your page renders on different devices. It is important that your page is optimized for mobile and tablet experiences as today the majority of web traffic comes from these sources.",
        "text": "",
        "expand_data": "The Title Tag is an important HTML element that tells users and Search Engines what the topic of the webpage is and the type of keywords the page should rank for. The Title will appear in the Header Bar of a user's browser. It is also one of the most important (and easiest to improve) On-Page SEO factors.\nWe recommend setting a keyword rich Title between 10–70 characters. This is often simple to enter into your CMS system or may need to be manually set in the header section of the HTML code."
    }



    return seo_data
