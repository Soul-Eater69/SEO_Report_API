from deepawali_seo_report.utils.lib import gradeCalculator


def usabilityOrganizer(seo_obj):
    seo_data = dict()

    desktop_rendering = seo_obj.get_screenshot(1)
    mobile_rendering = seo_obj.get_screenshot(0)
    seo_data["device_rendering"] = {
        "pass": 1,
        "required": 0,
        "mobile_screenshot": mobile_rendering["screenshot_image"],
        "desktop_screenshot": desktop_rendering["screenshot_image"],
        "display_title": "Device Rendering",
        "description": "This check visually demonstrates how your page renders on different devices. It is important that your page is optimized for mobile and tablet experiences as today the majority of web traffic comes from these sources.",
        "text": "",
        "expand_data": "The Title Tag is an important HTML element that tells users and Search Engines what the topic of the webpage is and the type of keywords the page should rank for. The Title will appear in the Header Bar of a user's browser. It is also one of the most important (and easiest to improve) On-Page SEO factors.\nWe recommend setting a keyword rich Title between 10–70 characters. This is often simple to enter into your CMS system or may need to be manually set in the header section of the HTML code."
    }

    mobile_vitals = seo_obj.get_vitals(0)
    passed = True if mobile_vitals["lcp"] <= 2.5 and mobile_vitals["fid"] <= 100 and mobile_vitals["cls"] <= 0.1 else False
    seo_data["mobile_vitals"] = {
        "pass": 1 if passed else 0,
        "required": 1,
        "vitals": mobile_vitals,
        "priority": 1,
        "recommendation": "Optimize for Core Web Vitals.",
        "display_title": "Google's Core Web Vitals",
        "description": "This check visually demonstrates how your page renders on different devices. It is important that your page is optimized for mobile and tablet experiences as today the majority of web traffic comes from these sources.",
        "text": "Your page has passed Google's Core Web Vitals assessment." if passed else "Your page has failed Google's Core Web Vitals assessment.",
        "expand_data": "Core Web Vitals are UI Metrics designed by Google that measure the overall quality of user experience on your site. They assess things such as the appearance of content, interactivity of the page and visual stability from the moment of page load. Core Web Vitals are gathered from real world usage data of a website (hence some smaller websites that haven't been well sampled may not return an appropriate result). Google has made Core Web Vitals a ranking factor for pages with increasing importance.\nTo improve your Core Web Vitals scores, you may need to read Google's documentation on the topic and follow the recommendations provided in the Google's PageSpeed Insights assessment."
    }

    mobile_viewport = seo_obj.get_mobile_viewport()
    seo_data["mobile_viewport"] = {
        "pass": 1 if mobile_viewport else 0,
        "required": 1,
        "priority": 2,
        "recommendation": "Make use of Movile Viewports in HTML.",
        "display_title": "Use of Mobile Viewports",
        "description": "",
        "text": "Your page specifies a viewport matching the device's size, allowing it to render appropriately across devices." if mobile_viewport else "Your page does not specify a viewport matching the device's size.",
        "expand_data": "The Viewport is a Meta Tag within the page's HTML which gives the browser instructions for how to control the page's dimensions and scaling. Setting the Viewport is particularly important for mobile and tablet device responsiveness, as without it, the page can appear incorrectly sized and require zooming or scrolling to view content.\nMake sure you include one Meta Viewport tag in the Head section of page HTML."
    }

    mobile_pagespeed, passed = seo_obj.get_lab_data(0)
    mobile_opportunities = seo_obj.get_opportunities(0)
    seo_data["mobile_pagespeed"] = {
        "pass": 1 if passed else 0,
        "required": 1,
        "display_title": "Google's PageSpeed Insights - Mobile",
        "insights": mobile_pagespeed,
        "priority": 1,
        "recommendation": "Optimize your page for Mobile PageSpeed Insights.",
        "opportunities": mobile_opportunities,
        "description": "Note that this evaluation is being performed from US servers and the results may differ slightly from an evaluation carried out from Google's PageSpeed Web Interface as that reporting localizes to the region in which you are running the report.\n\nGoogle has indicated that the performance of a webpage is becoming more important from a user and subsequently ranking perspective.",
        "text": "Your page specifies a viewport matching the device's size, allowing it to render appropriately across devices." if mobile_viewport else "Your page does not specify a viewport matching the device's size.",
        "expand_data": "The Viewport is a Meta Tag within the page's HTML which gives the browser instructions for how to control the page's dimensions and scaling. Setting the Viewport is particularly important for mobile and tablet device responsiveness, as without it, the page can appear incorrectly sized and require zooming or scrolling to view content.\nMake sure you include one Meta Viewport tag in the Head section of page HTML."
    }

    desktop_pagespeed, passed = seo_obj.get_lab_data(1)
    desktop_opportunities = seo_obj.get_opportunities(1)
    seo_data["desktop_pagespeed"] = {
        "pass": 1 if passed else 0,
        "required": 1,
        "display_title": "Google's PageSpeed Insights - Desktop",
        "insights": desktop_pagespeed,
        "opportunities": desktop_opportunities,
        "priority": 1,
        "recommendation": "Optimize your page for Desktop PageSpeed Insights.",
        "description": "Note that this evaluation is being performed from US servers and the results may differ slightly from an evaluation carried out from Google's PageSpeed Web Interface as that reporting localizes to the region in which you are running the report.\n\nGoogle has indicated that the performance of a webpage is becoming more important from a user and subsequently ranking perspective.",
        "text": "Your page specifies a viewport matching the device's size, allowing it to render appropriately across devices." if mobile_viewport else "Your page does not specify a viewport matching the device's size.",
        "expand_data": "The Viewport is a Meta Tag within the page's HTML which gives the browser instructions for how to control the page's dimensions and scaling. Setting the Viewport is particularly important for mobile and tablet device responsiveness, as without it, the page can appear incorrectly sized and require zooming or scrolling to view content.\nMake sure you include one Meta Viewport tag in the Head section of page HTML."
    }

    flash_data = seo_obj.flash_used()
    seo_data["flash_data"] = {
        "pass": 1 if not flash_data else 0,
        "required": 1,
        "display_title": "Flash Used?",
        "priority": 2,
        "recommendation": "Remove any Flash elements on the page.",
        "description": "",
        "text": "No Flash content has been identified on your page." if not flash_data else "Flash content has been identified on your page.",
        "expand_data": "Flash is an old embedded website technology that was frequently used in heavily animated features such as games and videos. However, Flash is not supported by all mobile devices and is not easily read by search engines. Improvements to HTML and CSS and the increased speed of modern web browsers have made it possible to implement many similar features with standard web technologies.\n\nIf Flash is detected on your site, you should carefully consider whether it is necessary due to the several drawbacks."
    }

    iframes_data = seo_obj.get_iframes()
    seo_data["iframes_data"] = {
        "pass": 1 if not iframes_data else 0,
        "required": 1,
        "priority": 2,
        "recommendation": "Remove any iframes on the page.",
        "display_title": "iFrames Used?",
        "description": "iFrames are discouraged as they can complicate navigation of content in mobile and have historically been harder to index for search engines.",
        "text": "Your page does not appear to be using iFrames." if not iframes_data else "Your page appears to be using iFrames.",
        "expand_data": "iFrames are a HTML tag that allow you to embed other webpages inside your page in a small frame. They generally represent an older coding practice and are discouraged as they can complicate navigation, particularly in mobile, and are harder for search engines to index.\n\nWe recommend removing any iFrames if they don't serve a critical purpose, or could be replaced with more natural navigation. However, some coding libraries like Google Tag Manager may still rely on iFrames as part of their internal functionality to load external pages and code files, so you may need to evaluate your usage of them on a case by case basis."
    }

    favicon_data = seo_obj.get_fav_icon()
    seo_data["favicon_data"] = {
        "pass": 1 if favicon_data else 0,
        "required": 1,
        "display_title": "Favicon",
        "priority": 2,
        "recommendation": "Include a favicon to improve the visual appearance.",
        "description": "",
        "text": "Your page has specified a favicon." if favicon_data else "Your page has not specified a favicon.",
        "expand_data": "A favicon is a small icon that serves as branding for your website. It's main purpose is to help visitors locate your page easier when they have multiple tabs open. It adds legitimacy to your site and helps boost your online branding as well as trust from potential consumers.\n\nEither use an online Favicon builder tool, or a graphic designer to build your Favicon, and load them into your website or CMS"
    }

    email_data = seo_obj.get_emails()
    seo_data["email_data"] = {
        "pass": 1 if not email_data else 0,
        "required": 1,
        "display_title": "Email Privacy",
        "priority": 2,
        "recommendation": "Do not specify any email addresses on your page.",
        "description": "",
        "text": "No email addresses have been found in plain text on your page." if not email_data else "Email addresses have been found in plain text on your page.",
        "expand_data": "Email addresses shown in clear text on your website can be easily scraped by bots, leading to inclusion in spam mailing lists.\nWe recommend removing any plain text email addresses and replacing them with contact forms, images, or less obvious text like 'email at website'."
    }

    for i in seo_data:
        seo_data[i]["category"] = "Usability"

    grade, percentage, grade_title, grade_text = gradeCalculator(
        seo_data, "Usability")
    seo_data["percentage"] = percentage
    seo_data["grade"] = grade
    seo_data["grade_title"] = grade_title
    seo_data["grade_text"] = grade_text

    return seo_data
